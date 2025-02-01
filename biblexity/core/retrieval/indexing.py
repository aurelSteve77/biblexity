import os.path
import logging
from typing import List

import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document

from biblexity.configuration import project_configuration
from biblexity.core.bible_data import BibleDataManager, VerseItem
from biblexity.models import get_embedding_model
from biblexity.utils import uniq_id, SingletonMeta

logger = logging.getLogger('biblexity')

class Indexer(metaclass=SingletonMeta):

    COLLECTION_NAME: str = 'biblexity_verses'

    def __init__(self):
        self.persistent_client = chromadb.PersistentClient(path=project_configuration.persistant_chroma_dir)
        self.verses_collection = self.persistent_client.get_or_create_collection(self.COLLECTION_NAME)
        self.embedding_model = get_embedding_model()

        self.vector_store = Chroma(
            client=self.persistent_client,
            collection_name=self.COLLECTION_NAME,
            embedding_function=self.embedding_model
        )

        self.load_or_create_store()

    def load_or_create_store(self, force=False):
        if not os.path.exists(project_configuration.persistant_chroma_dir) or force:
            logger.info('Create store')
            self.create_store()


    def create_store(self):
        verses = BibleDataManager().get_all_verses()
        verses_documents = [ Document(page_content=verse.text, metadata=verse.model_dump(), id=idx) for idx, verse in enumerate(verses) ]
        uuids = [uniq_id() for _ in range(len(verses_documents))]
        self.vector_store.add_documents(documents=verses_documents, ids=uuids)


    def query(self, query: str, k=5) -> List[VerseItem]:
        results = self.vector_store.similarity_search(
            query,
            k=k
        )
        print(f"===========> {results}")
        verses_list = []
        for res in results:
            verse = VerseItem(**res.metadata)
            verses_list.append(verse)

        return verses_list







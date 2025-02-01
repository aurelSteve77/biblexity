from typing import List

from fastapi import APIRouter

from biblexity.api.io_types import QuestionPayload
from biblexity.core.bible_data import BibleDataManager, VerseItem
from biblexity.core.retrieval.indexing import Indexer


router = APIRouter(
    prefix='/indexer',
    tags=['verses']
)

@router.post('/launch')
def launch_indexer():
    Indexer().load_or_create_store()
    return {"message": 'Indexation launched'}

@router.post('/question')
def ask_question(question: QuestionPayload) -> List[VerseItem]:
    return Indexer().query(question.query)
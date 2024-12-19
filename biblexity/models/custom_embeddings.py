from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings


class CustomEmbeddings(Embeddings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CustomOllamaEmbeddings(OllamaEmbeddings, CustomEmbeddings):

    def __init__(self, model_name: str):
        super().__init__(
            model=model_name
        )

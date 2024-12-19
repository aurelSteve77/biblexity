from biblexity.configuration import project_configuration
from biblexity.models.custom_embeddings import CustomEmbeddings, CustomOllamaEmbeddings
from biblexity.models.custom_llms import CustomChatModel, CustomChatOllama


def get_chat_model() -> CustomChatModel:
    return CustomChatOllama(
        model_name=project_configuration.llm_model
    )

def get_embedding_model() -> CustomEmbeddings:
    return CustomOllamaEmbeddings(model_name=project_configuration.embedding_model)

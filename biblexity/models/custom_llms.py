from langchain_core.language_models import BaseChatModel
from langchain_ollama.chat_models import ChatOllama

class CustomChatModel(BaseChatModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_temperature(self,  temperature: float):
        pass

    def set_max_tokens(self, max_tokens: int):
        pass


class CustomChatOllama(ChatOllama, CustomChatModel):

    def __init__(self, model_name, temperature: float = 0.5, max_tokens: int = 3000):
        super().__init__(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )
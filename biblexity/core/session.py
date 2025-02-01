from typing import List, Dict

from pydantic import BaseModel, Field

from biblexity.core.agent_query import AgentQuery, AgentQueryResponse
from biblexity.core.bible_data import VerseItem
from biblexity.models import get_chat_model
from biblexity.utils import uniq_id, SingletonMeta


class Message(BaseModel):
    role: str
    content: str

class VerseChunk(BaseModel):
    start_verse: VerseItem
    end_verse: VerseItem

class QuestionResponse(BaseModel):
    text: str = Field(description='response text')
    reference_verses: List[VerseChunk]


class Session:
    def __init__(self, session_id: str):
        self.id = session_id
        self.messages : List[Message] = []
        self.version = None
        self.agent_query = AgentQuery(llm_model=get_chat_model())

    def ask_question(self, query: str) -> AgentQueryResponse:
        return self.agent_query.run(query=query)


class SessionManager(metaclass=SingletonMeta):

    def __init__(self):
        self._session_dict: Dict[str, Session] = {}


    def create_session(self) -> Session:
        session_id = uniq_id()
        session = Session(session_id=session_id)
        self._session_dict[session_id] = session
        return session

    def get_session(self, session_id: str) -> Session:
        return self._session_dict.get(session_id, None)

session_manager = SessionManager()

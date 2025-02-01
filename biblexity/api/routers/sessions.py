from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from biblexity.core.agent_query import AgentQueryResponse
from biblexity.core.retrieval.indexing import Indexer
from biblexity.core.session import session_manager

router = APIRouter(
    prefix='/session',
    tags=['verses']
)

class SessionIdOutput(BaseModel):
    session_id: str

class QuestionQuery(BaseModel):
    session_id: str
    question: str

class QuestionOutput(BaseModel):
    session_id: str
    response: str

@router.post('/init-session')
def init_session() -> SessionIdOutput:
    session = session_manager.create_session()
    return SessionIdOutput(session_id = session.id)

@router.post('/question')
def init_session(question_query: QuestionQuery) -> AgentQueryResponse:
    session = session_manager.get_session(session_id=question_query.session_id)
    response = session.ask_question(query=question_query.question)
    return response
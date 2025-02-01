from pydantic import BaseModel


class QuestionPayload(BaseModel):
    query: str
    version: str = 'BDS'

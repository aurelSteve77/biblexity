from typing import List, Dict

from jinja2 import Template
from langchain_core.messages import ChatMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel

from biblexity.core.bible_data import VerseItem
from biblexity.core.prompt_reader import PromptReader
from biblexity.core.retrieval.indexing import Indexer
from biblexity.models import CustomChatModel
from biblexity.utils import render_template


class AgentQueryResponse(BaseModel):
    response: str
    relevant_verses: List[VerseItem]

class AgentQuery:
    NAME: str = 'agent_query'

    def __init__(self, llm_model: CustomChatModel):
        self.llm_model = llm_model
        self.llm_model.set_temperature(0.5)
        self.indexer = Indexer()
        self.messages_history: List[ChatMessage] = []
        self.prompts = PromptReader().read_agent_prompt(self.NAME)
        self.prompt_template = ChatPromptTemplate.from_messages([
            ('system', self.prompts['system']),
            MessagesPlaceholder('chat_history'),
            ('user', '{query}')
        ])
        self.chain = self.prompt_template | self.llm_model
        self.nb_chunks = 5

    def render_query(self, query: str, docs: List[Dict]):
        query_context = {
            'question': query,
            'documents': docs
        }
        rendered = render_template(self.prompts['query'], context=query_context)
        return rendered

    def get_relevant_context(self, query: str):
        relevant_documents = self.indexer.query(query=query, k=self.nb_chunks)
        return relevant_documents

    def run(self, query: str) -> AgentQueryResponse:

        # get relevant documents
        relevant_documents = self.get_relevant_context(query)

        # build the payload
        relevant_documents_dict = [ {'id': idx, **doc.model_dump() } for idx, doc in enumerate(relevant_documents) ]
        query_str = self.render_query(query=query, docs=relevant_documents_dict)
        payload = {
            'chat_history': self.messages_history,
            'query': query_str
        }

        # call the model
        res = self.chain.invoke(payload)
        response = res.content

        self.messages_history.append(
            HumanMessage(content=query_str),
        )
        self.messages_history.append(
            AIMessage(content=response),
        )

        response_item = AgentQueryResponse(
            response = response,
            relevant_verses = relevant_documents
        )

        return response_item



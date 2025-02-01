from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from typing import cast

import chainlit as cl
from openai import base_url, api_key

from biblexity.core.session import session_manager



@cl.on_message
async def main(message: cl.Message):
    session = cl.user_session.get('session')
    response = session.ask_question(message.content)

    elements = [
        cl.Text(name='verse', content=verse.render(), display='page') for verse in response.relevant_verses
    ]

    msg = cl.Message(content=response.response, elements=elements, metadata=response.model_dump())
    await msg.send()

@cl.on_chat_start
async def init():
    session = session_manager.create_session()
    cl.user_session.set("session", session)

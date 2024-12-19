from fastapi import FastAPI
from chainlit.utils import mount_chainlit

app = FastAPI(
    title='Biblexity',
    description='Query bible in natural language'
)

app.get("/app")
def read_main():
    return {'message': 'Hello Salut les amis'}

mount_chainlit(app=app, target='biblexity/chainlit/cl_app.py', path='/chainlit')

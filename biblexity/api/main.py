from fastapi import FastAPI
from uvicorn import run
from chainlit.utils import mount_chainlit
from biblexity.configuration import project_configuration
from biblexity.api.routers import verses, query, sessions

app = FastAPI(
    title='Biblexity',
    description='Query bible in natural language',
    docs_url=f"{project_configuration.api_context_path}/docs"
)


app.include_router(verses.router, prefix=project_configuration.api_context_path)
app.include_router(query.router, prefix=project_configuration.api_context_path)
app.include_router(sessions.router, prefix=project_configuration.api_context_path)

app.get("/app")
def read_main():
    return {'message': 'Hello Salut les amis'}

mount_chainlit(app=app, target='biblexity/chainlit/cl_app.py', path=f'{project_configuration.api_context_path}/chainlit')


def main():
    run('biblexity.api.main:app', port=project_configuration.api_port, reload=True)
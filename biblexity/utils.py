from typing import Dict
from uuid import uuid4

from jinja2 import Template


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def uniq_id() -> str:
    return str(uuid4())

def get_file_name(path) -> str:
    # remove parent folders
    filename = path.rsplit('/', 1)[-1]

    # remove extension
    filename = filename.rsplit('.', 1)[0]

    return filename

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def render_template(template_str: str, context: Dict) -> str:
        template = Template(template_str)
        rendered = template.render(**context)
        return rendered
import os
from pathlib import Path
from typing import Dict

from biblexity.utils import get_file_name, SingletonMeta, read_file


class PromptReader(metaclass=SingletonMeta):
    EXTENSION = '.prt'
    BASE_FOLDER = Path(__file__).parent.parent.parent / "resources/prompts"

    def __init__(self):
        self._agents_prompts: Dict[str, Dict] = {} # dict containing the agents prompts dicts


    def read_agent_prompt(self, agent_name: str):
        if not agent_name in self._agents_prompts:
            agent_prompts = {}
            agent_folder = os.path.join(self.BASE_FOLDER, agent_name)
            for file in os.scandir(agent_folder):
                if file.name.endswith(self.EXTENSION):
                    content = read_file(file.path)
                    prompt_name = get_file_name(file.name)
                    agent_prompts[prompt_name] = content

            self._agents_prompts[agent_name] = agent_prompts

        return self._agents_prompts[agent_name]
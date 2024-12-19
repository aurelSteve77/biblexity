import os
import yaml
import configparser
from pathlib import Path
from dotenv import load_dotenv

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Configuration(metaclass=SingletonMeta):

    BASE_FOLDER_PATH: str = Path(__file__).parent.parent
    CONFIG_PATH: str = BASE_FOLDER_PATH / "configs/app.conf"
    ENV_PATH: str = BASE_FOLDER_PATH / "configs/.env"

    def __init__(self):

        # load dotenv
        if os.path.exists(self.ENV_PATH):
            load_dotenv(self.ENV_PATH)

        # read config from file
        self.config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation(),
            defaults=os.environ  # Makes env variables available as ${DEFAULT:VAR_NAME}
        )
        self.config.read(self.CONFIG_PATH)
        self.read_variables()


    def read_variables(self):

        # api
        self.api_context_path = self.get_var(section='api', var_name='context_path', type=str)
        self.api_port = self.get_var(section='api', var_name='port', type=int)
        self.api_description = self.get_var(section='api', var_name='description', type=str)

        # models
        self.llm_url = self.get_var(section='models', var_name='llm_url', type=str)
        self.llm_model = self.get_var(section='models', var_name='llm_model', type=str)
        self.embedding_url = self.get_var(section='models', var_name='embedding_url', type=str)
        self.embedding_model = self.get_var(section='models', var_name='embedding_model', type=str)


    def get_var(self, section: str, var_name: str, default_value=None, type = str):
        # get the variables
        var = self.config.get(section, var_name)
        if not var:
            return default_value
        return type(var)


project_configuration = Configuration()

import json
from pathlib import Path
from typing import Dict

class Config:
    @staticmethod
    def load():
        if not Path("config.json").exists():
            raise FileNotFoundError(
                "Copy and edit the config-sample.json file into config.json .")

        with open("config.json", "r") as f:
            config_data = json.load(f)
        
        return config_data


def _sqlite_config(config: Dict):
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': config['db']['name'],
        }
    }
    
def _postgre_config(config: Dict):
    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config['db']['name'],
            'USER': config['db']['user'],
            'PASSWORD': config['db']['password'],
            'HOST': config['db']['host'],
            'PORT': config['db']['port'],
        }
    }


class DbConfigFactory:
    _db_config_builders = {
        'sqlite': _sqlite_config,
        'postgre': _postgre_config,
    }
    
    @staticmethod
    def build(config: Dict):    
        db_type = config['db']['type']
        
        if db_type not in DbConfigFactory._db_config_builders:
            raise Exception(f"Invalid database type \"{config['db']['type']}\"")
        
        return DbConfigFactory._db_config_builders[db_type](config)       


        


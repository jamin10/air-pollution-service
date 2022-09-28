from dataclasses import dataclass
import os

from apt import ProblemResolver

class ConfigError(Exception):
    pass

@dataclass
class Config:
    db_username: str
    db_password: str
    api_Key_geodb: str
    api_key_open_weather: str

    def validate(self):
        # Todo: Make this validation throw Exception if Config is not present
        if self.db_username == None:
            raise ConfigError("db_username is not set")

        if self.db_password == None:
           raise ConfigError("db_password is not set")
        
        if self.api_Key_geodb == None:
            raise ConfigError("api_Key_geodb is not set")

        if self.api_key_open_weather == None:
            raise ConfigError("api_key_open_weather is not set")

        

def load_config():
    config = Config(
        os.environ.get("DB_USERNAME"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("API_KEY_GEODB"),
        os.environ.get("API_KEY_OPEN_WEATHER")
    )
    config.validate()
    return config

    # Todo: Pass these as environment variables 
    # GeoDB_API_key = 'b29f2328d6mshfe5d6639483b6a2p166f69jsn5c93c74e7d77'
    # OW_API_key = '371506301b2009441f3135528150fb96'
    # username = 'postgres'
    # password = 'postgres'
    #return dataclass called config 
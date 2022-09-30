from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv() # Load environ variables from .env 

class ConfigError(Exception):
    pass

@dataclass
class Config:
    db_name: str
    db_username: str
    db_password: str
    host: str
    port_id: int
    api_Key_geodb: str
    api_key_open_weather: str

    def validate(self):
        # Validation to throw exception if config value is missing 
        if self.db_name is None:
            raise ConfigError("db_name is not set")
        if self.db_username is None:
            raise ConfigError("db_username is not set")
        if self.db_password is None:
           raise ConfigError("db_password is not set")
        if self.db_password is None:
           raise ConfigError("db_password is not set")
        if self.host is None:
           raise ConfigError("host is not set")
        if self.port_id is None:
            raise ConfigError("port_id is not set")
        if self.api_Key_geodb is None:
           raise ConfigError("api_Key_geodb is not set")
        if self.api_key_open_weather is None:
            raise ConfigError("api_key_open_weather is not set")

        
def load_config():
    # Create Congif dataclass from enironment variables 
    config = Config(
        os.environ.get("DB_NAME"),
        os.environ.get("DB_USERNAME"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("HOST"),
        os.environ.get("PORT_ID"),
        os.environ.get("API_KEY_GEODB"),
        os.environ.get("API_KEY_OPEN_WEATHER")
    )
    
    config.validate()

    return config

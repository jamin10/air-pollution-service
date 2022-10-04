from dataclasses import dataclass, fields
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
    api_key_geodb: str
    api_key_open_weather: str

    def validate(self):
        # Validation to throw exception if config value is missing 
        for field in fields(self):
            if getattr(self, field.name) is None:
                raise ConfigError(f"{field.name} is not set")
        
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

from dataclasses import dataclass
import os 
from pydantic import ValidationError
from src.utils.logger import get_logger
from src.exception import MissingConfigError

logger = get_logger(__name__)
@dataclass
class Config:
    openai_api_key : str 
    model: str
def require_env(key: str) -> str:
    key_value = os.getenv(key)
    if key_value is None or key_value == "": 
        logger.warning(f" environment value is missing {key_value}")
        raise MissingConfigError(f" environment value is missing {key_value}")

    return key_value
def load_config() -> Config:
    openai_api_key = require_env("OPENAI_API_KEY")
    model = require_env("MODEL")
    return Config(openai_api_key=openai_api_key, model=model)
    
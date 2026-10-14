from openai import OpenAI
from src.config import Config
import openai

def create_client(config: Config) -> OpenAI:
    return OpenAI(api_key=config.openai_api_key)
def check_first_api_response(client: OpenAI, config: Config) -> bool:
    try:
        client.chat.completions.create(
            model= config.model,
            messages=[
                {"role":"system","content":"ping"}
            ]
        )
    except openai.AuthenticationError:
        return False
    return True
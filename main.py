from src.models.llm import check_first_api_response, create_client
from src.config import load_config
from src.utils.logger import get_logger
from src.exception import MissingConfigError
from src.desk_service.services import handle_message
from src.utils.history import trim_history
import openai

def main() -> None:
    logger = get_logger(__name__)
    logger.info("App Started..")
    try:
        config = load_config()
        model = config.model
    except MissingConfigError as e:
        logger.error(f"API Key Error Check OPEAI_API_KEY {e}")
    client = create_client(config)
    
    if not check_first_api_response(config=config, client=client):
         logger.error("Authentication failed — check OPENAI_API_KEY.")
    else:
        logger.info("App is working...")
    print ("RepaiDesk send a message or type /quit to exit.")
    history = []
    while True:
        user_input = input("User: ")
        if user_input == "/quit":
            break
        try:
            handle_message(client=client, history=history, message=user_input, model=model)
        except openai.AuthenticationError as e:
            logger.error("API key stopped working mid session.")
            print("Login failed - check OPENAI_API_KEY in your .env")
        except openai.RateLimitError as e:
            logger.warning("Rate limited after the client's retries.")
            print("We are busy right now -wait a moment and try again.")
        except openai.BadRequestError as e:
            print("That message was too long to handle - please shorten it.")
if __name__ == "__main__":
    main()

from openai import OpenAI
from src.models.llm import create_client
from src.config import load_config
from src.utils.logger import get_logger
from src.agents.router import decide
from src.agents.intake import intake_agent
from src.agents.concierge import concierge_agent

def handle_message(client: OpenAI, history: list[dict], message: str, model: str) -> None:
    logger = get_logger(__name__)
    decision = decide(client=client, message=message, model=model)
    if decision.agent == "intake":
        ticket = intake_agent(client=client, message=message, model=model)
        
        if ticket is None:
            logger.warning(" intake agent did not assigned any ticket.")
        else:
            logger.info(f"ticket: {ticket.device} / {ticket.urgency}")
            print(ticket)
    else:
        concierge_agent(client=client, history=history, message=message, model=model)


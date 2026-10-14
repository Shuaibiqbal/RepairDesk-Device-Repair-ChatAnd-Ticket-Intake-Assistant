from openai import OpenAI
from src.utils.logger import get_logger
from src.schemas import RepairTicket
from src.utils.prompt import load_prompt
from pydantic import ValidationError

def intake_agent(client: OpenAI, message: str, model: str) -> RepairTicket:
    logger = get_logger(__name__)
    messages = [
        {"role":"system", "content": load_prompt("intake")},
        {"role":"user", "content": message}
    ]
    try:
        completion = client.beta.chat.completions.parse(
            model=model, 
            messages=messages,
            response_format=RepairTicket
        )
        reply = completion.choices[0].message
    except ValidationError as e:
        f"Intake output did not match RepairTicket: {e}"
        return None
    return reply.parsed

from openai import OpenAI
from src.schemas import RouteDecision
from src.utils.prompt import load_prompt
from pydantic import ValidationError
from src.utils.logger import get_logger

def decide(client: OpenAI, message: str, model: str) -> RouteDecision:
    logger = get_logger(__name__)
    messages = [
        {"role":"system", "content": load_prompt("router")},
        {"role": "user", "content": message}
    ]
    decision = RouteDecision(
        agent= "concierge", reason="router did not decide your message"
    )
    try:
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=messages,
            response_format=RouteDecision
        )
        reply = completion.choices[0].message

        if reply.parsed is not None:
            decision = reply.parsed
    except ValidationError as e:
        logger.info(f"router did not find any decision: {e}")
    return decision
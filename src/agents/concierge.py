from openai import OpenAI
from src.utils.logger import get_logger

def concierge_agent(client: OpenAI, history: list[dict], message: str, model: str)-> str:
    history.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model=model,
        messages=history,
        stream=True
    )
    full_reply = ""
    
    for chunk in stream:
        piece = chunk.choices[0].delta.content
        if piece:
            # print("\n piece: ",piece)
            full_reply += piece
            print(piece, end="", flush=True)
    print()
    history.append({"role":"assistant","content":full_reply})
    return full_reply
        
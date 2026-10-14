
def estimate_token(history: list[dict], MAX_HISTORY_TOKEN: int) -> list[dict]:
    count_tokens = 0
    for message in history:
        count_tokens += message["content"]
    if count_tokens > MAX_HISTORY_TOKEN:
        del history[-1]
    return history

def trim_history(history: list[dict], MAX_HISTORY_TOKEN: int = 300):
    
    history = trim_history(history, MAX_HISTORY_TOKEN)
    return history 

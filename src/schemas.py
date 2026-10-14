
from typing import Literal

from pydantic import BaseModel

class RouteDecision(BaseModel):
    agent: str
    reason: str
class RepairTicket(BaseModel):
    customer_name: str | None
    device: Literal["phone", "laptop", "computer", "other"]
    urgency: Literal["low", "medium", "high"]
    summary: str
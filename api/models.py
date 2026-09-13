from pydantic import BaseModel

class TicketQuery(BaseModel):
    record_id: str

class TicketResponse(BaseModel):
    record_id: str
    status: str
    resolution_time_hours: int
    escalation_score: float


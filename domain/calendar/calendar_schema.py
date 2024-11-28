from pydantic import BaseModel
from datetime import date


# Pydantic schemas
class EventCreate(BaseModel):
    date: date
    event_type: str
    location: str
    duration: str
    notes: str


class EventUpdate(BaseModel):
    date: date
    event_type: str
    location: str
    duration: str
    notes: str

class EventResponse(EventCreate):
    id: int

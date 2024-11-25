from pydantic import BaseModel
from datetime import date


# Pydantic schemas
class EventCreate(BaseModel):
    date: date
    event_name: str
    location: str
    duration: str


class EventUpdate(BaseModel):
    date: date
    event_name: str
    location: str
    duration: str


class EventResponse(EventCreate):
    id: int

from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    id: str
    title: str
    location: str
    date: date
    is_open: bool = True

class EventCreate(BaseModel):
    title: str
    location: str
    date: date
    is_open: bool = True

class EventUpdate(EventCreate):
    pass
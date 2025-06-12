# schemas/event.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class EventBase(BaseModel):
    title: str
    location: str
    date: date

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    is_open: Optional[bool] = True

class Event(EventBase):
    id: int
    is_open: bool = True

    class Config:
        orm_mode = True

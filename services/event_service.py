# services/event_service.py

from schemas import event as event_schema
from typing import List, Optional
import itertools

# In-memory storage
_events: List[event_schema.Event] = []
_event_id_counter = itertools.count(1)

def create_event(event_create: event_schema.EventCreate) -> event_schema.Event:
    new_event = event_schema.Event(
        id=next(_event_id_counter),
        title=event_create.title,
        location=event_create.location,
        date=event_create.date,
        is_open=True
    )
    _events.append(new_event)
    return new_event

def get_all_events() -> List[event_schema.Event]:
    return _events

def get_event(event_id: int) -> Optional[event_schema.Event]:
    return next((event for event in _events if event.id == event_id), None)

def update_event(event_id: int, event_update: event_schema.EventUpdate) -> Optional[event_schema.Event]:
    event = get_event(event_id)
    if event:
        event.title = event_update.title
        event.location = event_update.location
        event.date = event_update.date
        event.is_open = event_update.is_open if event_update.is_open is not None else event.is_open
        return event
    return None

def delete_event(event_id: int) -> bool:
    global _events
    event = get_event(event_id)
    if event:
        _events = [e for e in _events if e.id != event_id]
        return True
    return False

def close_event_registration(event_id: int) -> Optional[event_schema.Event]:
    event = get_event(event_id)
    if event:
        event.is_open = False
        return event
    return None

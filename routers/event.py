# routes/event.py

from fastapi import APIRouter, HTTPException
from typing import List
from schemas import event as event_schema
from services import event_service

router = APIRouter()

@router.post("/", response_model=event_schema.Event, status_code=201)
def create_event(event: event_schema.EventCreate):
    return event_service.create_event(event)

@router.get("/", response_model=List[event_schema.Event])
def get_events():
    return event_service.get_all_events()

@router.get("/{event_id}", response_model=event_schema.Event)
def get_event(event_id: int):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=event_schema.Event)
def update_event(event_id: int, event_update: event_schema.EventUpdate):
    updated_event = event_service.update_event(event_id, event_update)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int):
    success = event_service.delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return

@router.post("/{event_id}/close", response_model=event_schema.Event)
def close_event_registration(event_id: int):
    updated_event = event_service.close_event_registration(event_id)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

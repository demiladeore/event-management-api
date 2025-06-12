# routes/registration.py

from fastapi import APIRouter, HTTPException
from typing import List
from schemas import registration as registration_schema
from services import registration_service

router = APIRouter()

@router.post("/", response_model=registration_schema.Registration, status_code=201)
def register_user_for_event(registration: registration_schema.RegistrationCreate):
    result = registration_service.register_user_for_event(registration)
    if result is None:
        raise HTTPException(status_code=400, detail="Registration failed (check constraints).")
    return result

@router.post("/{registration_id}/mark_attendance", response_model=registration_schema.Registration)
def mark_attendance(registration_id: int):
    updated_registration = registration_service.mark_attendance(registration_id)
    if not updated_registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return updated_registration

@router.get("/", response_model=List[registration_schema.Registration])
def get_all_registrations():
    return registration_service.get_all_registrations()

@router.get("/user/{user_id}", response_model=List[registration_schema.Registration])
def get_user_registrations(user_id: int):
    return registration_service.get_user_registrations(user_id)

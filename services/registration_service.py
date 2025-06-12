# services/registration_service.py

from schemas import registration as registration_schema
from typing import List, Optional
import itertools
from datetime import datetime

from services import user_service, event_service

# In-memory storage
_registrations: List[registration_schema.Registration] = []
_registration_id_counter = itertools.count(1)

def register_user_for_event(registration_create: registration_schema.RegistrationCreate) -> Optional[registration_schema.Registration]:
    # Validate user
    user = user_service.get_user(registration_create.user_id)
    if not user or not user.is_active:
        return None

    # Validate event
    event = event_service.get_event(registration_create.event_id)
    if not event or not event.is_open:
        return None

    # Check for existing registration (user cannot register twice for same event)
    for reg in _registrations:
        if reg.user_id == registration_create.user_id and reg.event_id == registration_create.event_id:
            return None

    # All validations passed → create registration
    new_registration = registration_schema.Registration(
        id=next(_registration_id_counter),
        user_id=registration_create.user_id,
        event_id=registration_create.event_id,
        registration_date=datetime.now(),
        attended=False
    )
    _registrations.append(new_registration)
    return new_registration

def mark_attendance(registration_id: int) -> Optional[registration_schema.Registration]:
    registration = get_registration(registration_id)
    if registration:
        registration.attended = True
        return registration
    return None

def get_all_registrations() -> List[registration_schema.Registration]:
    return _registrations

def get_user_registrations(user_id: int) -> List[registration_schema.Registration]:
    return [reg for reg in _registrations if reg.user_id == user_id]

def get_registration(registration_id: int) -> Optional[registration_schema.Registration]:
    return next((reg for reg in _registrations if reg.id == registration_id), None)

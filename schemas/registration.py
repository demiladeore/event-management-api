# schemas/registration.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    attended: Optional[bool] = False

class Registration(RegistrationBase):
    id: int
    registration_date: datetime
    attended: bool = False

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import date

class Registration(BaseModel):
    id: str
    user_id: str
    event_id: str
    registration_date: date
    attended: bool = False
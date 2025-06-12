# schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    is_active: Optional[bool] = True

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True

from pydantic import BaseModel
# from typing import Annotated

class User(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool = True

class UserCreate(BaseModel):
    name: str
    email: str
    is_active: bool = True

class UserUpdate(BaseModel):
    name: str
    email: str
    is_active: bool = True

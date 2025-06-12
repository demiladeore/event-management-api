# routes/user.py

from fastapi import APIRouter, HTTPException
from typing import List
from schemas import user as user_schema
from services import user_service

router = APIRouter()

@router.post("/", response_model=user_schema.User, status_code=201)
def create_user(user: user_schema.UserCreate):
    return user_service.create_user(user)

@router.get("/", response_model=List[user_schema.User])
def get_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=user_schema.User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user_update: user_schema.UserUpdate):
    updated_user = user_service.update_user(user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return

@router.post("/{user_id}/deactivate", response_model=user_schema.User)
def deactivate_user(user_id: int):
    updated_user = user_service.deactivate_user(user_id)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

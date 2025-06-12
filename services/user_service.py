# services/user_service.py

from schemas import user as user_schema
from typing import List, Optional
import itertools

# In-memory storage
_users: List[user_schema.User] = []
_user_id_counter = itertools.count(1)

def create_user(user_create: user_schema.UserCreate) -> user_schema.User:
    new_user = user_schema.User(
        id=next(_user_id_counter),
        name=user_create.name,
        email=user_create.email,
        is_active=True
    )
    _users.append(new_user)
    return new_user

def get_all_users() -> List[user_schema.User]:
    return _users

def get_user(user_id: int) -> Optional[user_schema.User]:
    return next((user for user in _users if user.id == user_id), None)

def update_user(user_id: int, user_update: user_schema.UserUpdate) -> Optional[user_schema.User]:
    user = get_user(user_id)
    if user:
        user.name = user_update.name
        user.email = user_update.email
        user.is_active = user_update.is_active if user_update.is_active is not None else user.is_active
        return user
    return None

def delete_user(user_id: int) -> bool:
    global _users
    user = get_user(user_id)
    if user:
        _users = [u for u in _users if u.id != user_id]
        return True
    return False

def deactivate_user(user_id: int) -> Optional[user_schema.User]:
    user = get_user(user_id)
    if user:
        user.is_active = False
        return user
    return None

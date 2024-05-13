import uuid
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    phone_number: int
    username: str
    bot_status: Optional[bool] = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    phone_number: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.shemas import UserRead, UserCreate
from bot_add.router import router as bot_router



app = FastAPI(
    title="bot app"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(bot_router)
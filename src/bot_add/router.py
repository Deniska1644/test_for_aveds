from fastapi import APIRouter, Depends
from auth.models import User
from auth.base_config import fastapi_users
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import update, values
from auth.models import user as user_model




router = APIRouter(
    prefix="/bot"
)

curent_user = fastapi_users.current_user()


@router.post("/activate")
async def activate_bot(
    user:User = Depends(curent_user),
    tg_name:str = "None", 
    session:AsyncSession = Depends(get_async_session)):
    stmt = update(user_model).where(user_model.c.id == user.id).values(bot_status=True,tg_name = tg_name)
    await session.execute(stmt)
    await session.commit()
    return {"status":"success"}
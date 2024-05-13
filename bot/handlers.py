from email import message
from enum import verify
from aiogram import Router
from aiogram.types import Message
from db import session
from models import user
from sqlalchemy import select

router = Router()


@router.message()
async def message_handler(msg: Message):
    username = msg.from_user.username
    async with session() as ses: 
        query = select(user).where(user.c.tg_name == username)
        result = await ses.execute(query)
        verify = result.fetchone()

    if verify is None:
        await msg.answer('вы не зарегестрированны')
    elif verify[8] != True:
        await msg.answer('у вас не активен бот')
    else:
        text = len(msg.text)
        await msg.answer(f"Вы отправили сообщение длиной: {text} символов")




        

        # text = len(msg.text)
        # await msg.answer(f"Вы отправили сообщение длиной: {text} символов")
    
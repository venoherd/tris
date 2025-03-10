import asyncio

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime, time, timedelta

router_time = Router(name="Xronos")

#таймер сообщений
async def wait_until(target_time: time):
    now = datetime.now().time()
    now_datetime = datetime.now()
    target_datetime = datetime.combine(now_datetime.date(), target_time)
    if now > target_time:
        target_datetime += timedelta(days=1)

    wait_seconds = (target_datetime - now_datetime).total_seconds()
    print(wait_seconds)
    await asyncio.sleep(wait_seconds)

#команда для чего она?)
@router_time.message(Command("noti"))
async def noti(message: Message):
    print("жди")
    ttime=datetime.now()+timedelta(seconds=10) #тут указать время
    await wait_until(target_time=ttime.time())
    await message.reply("текст сообщения")
    #можно чо угодно добавить
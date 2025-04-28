import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram import F

import aiosqlite

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import router
from aiogram.filters import CommandStart, Command
from dotenv import dotenv_values

from bot_cfg import bot
from rep_man.rep_man import router_man
from data.keyboards_callback import router_boards_callback
from data.talkusers import router_dic
from data.time import router_time
from data.slashes import router_sla


from data.slashes import info, help, hello


dp = Dispatcher()

dp.include_router(router_time)
dp.include_router(router_sla)
dp.include_router(router_man)
dp.include_router(router_boards_callback)
dp.include_router(router_dic)


#команда старт
@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Привет, вспомогательный бот Trisservice готов к работе! Для вывода меню проблем напишите - проблемы" )


#обработка текстовых запросов



#запуск бота
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls


    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
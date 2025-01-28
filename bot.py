import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import dotenv_values


dp = Dispatcher()

#команда старт
@dp.message(CommandStart())
async def check_user_id(message: types.Message):
    if not await users(message.from_user.id):
        await message.reply("У вас нет доступа к этому боту.")
        return
    await message.reply("Добро пожаловать!")

# вайтлист (база данных)

ALLOWED_USERS = [431862198, 5570684597]
#отвечает за запуск бота


#функия доступа к базе данных
async def users(id):
    return id in [431862198, 5570684597]

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    token=dotenv_values(".env")
    bot = Bot(token=token["token"])

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
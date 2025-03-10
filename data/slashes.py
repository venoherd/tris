from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router_sla = Router(name='Bred')

#другие команды
@router_sla.message(Command("help"))
async def help(message: Message):
    await message.answer("Если у вас возникла какая-то проблема, напишите в чат - проблема указать с чем, например: проблема локер")

@router_sla.message(Command("info"))
async def info(message: Message):
    await message.answer("а тут будет важная информация")

@router_sla.message(Command("hello"))
async def hello(message: Message):
    await message.answer("Доброе утро!")




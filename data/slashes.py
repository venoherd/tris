from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from data.keyboards import all_page_one

router_sla = Router(name='Bred')

#другие команды
@router_sla.message(Command("help"))
async def help(message: Message):
    await message.reply("Если у вас возникла какая-то проблема, напишите в чат - проблема, далее выберете с чем ваша проблема и найдите ее в списке! ")

@router_sla.message(Command("info"))
async def info(message: Message):
    await message.answer("а тут будет важная информация")

@router_sla.message(Command("hello"))
async def hello(message: Message):
    await message.answer("Доброе утро! Готовы приступить к работе?")

@router_sla.message(Command("problems"))
async def rpoblem_main(message: Message):
    await message.answer("Ниже представлен список всех проблем",reply_markup=all_page_one,)



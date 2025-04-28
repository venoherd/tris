from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from data.db_tools import output_mains, output_par, output_recall
from data.keyboards import create_keyboards, create_keyboards_fi

router_sla = Router(name='Bred')

#другие команды
@router_sla.message(Command("help"))
async def help(message: Message):
    await message.reply("Если у вас возникла какая-то проблема, напишите в чат - проблема, далее выберете с чем ваша проблема и найдите ее в списке! ")

@router_sla.message(Command("info"))
async def info(message: Message):
    await message.reply("Тут все еще нет важной информации...")

@router_sla.message(Command("hello"))
async def hello(message: Message):
    await message.reply("Доброе утро! Готовы приступить к работе?")



#тут создается все!
@router_sla.message(Command("problems"))
async def rpoblem_main(message: Message):
    id_message, text_message, id_parents = await output_mains("main_m")
    keyboard_buttons = await output_par(id_message)

    recallback = "main_m"
    if id_parents is not None:
        recallback = await output_recall(id_parents)

    keyboard = await create_keyboards_fi(keyboard_buttons, recallback)

    await message.reply(text_message, reply_markup=keyboard)



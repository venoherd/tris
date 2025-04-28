from aiogram import Router, F
from aiogram.types import  CallbackQuery, Message


from data.keyboards import create_keyboards, create_keyboards_fi
from data.db_tools import output_words, output_keyboards, output_mains, output_par, output_recall

router_boards_callback= Router(name='Dobi')



#обработчки коллбеков
@router_boards_callback.callback_query(F.data.split()[0] == "problem")
async def search(call: CallbackQuery):
    name_problem = call.data.split()[1]
    manual = await output_words(name_problem)
    buttons = await output_keyboards(name_problem)
    keyboard = await create_keyboards(buttons)
    if manual:
        await call.message.edit_text(manual,reply_markup=keyboard)

#обработчик пронто


# обработчик основы main_m
@router_boards_callback.callback_query()
async def all_menu(call: CallbackQuery):
        id_message,text_message, id_parents = await output_mains(call.data)
        keyboard_buttons = await output_par(id_message)

        recallback = "menu"
        if id_parents is not None:
            recallback = await output_recall(id_parents)

        keyboard = await create_keyboards_fi(keyboard_buttons,recallback)

        await call.message.edit_text(text_message, reply_markup=keyboard)
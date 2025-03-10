from aiogram import Router, F
from aiogram.types import  CallbackQuery, Message

from data.keyboards import last_page_locer
from data.db_tools import output_words


router_boards_callback= Router(name='Dobi')

#обработчки коллбеков
@router_boards_callback.callback_query(F.data.split()[0] == "problem")
async def search(call: CallbackQuery):
    name_problem = call.data.split()[1]
    manual = await output_words(name_problem)
    if manual:
        await call.message.edit_text(manual,reply_markup =last_page_locer)

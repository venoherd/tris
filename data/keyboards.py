from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router_boards = Router(name='jon')




#создание клавиатуры
async def create_keyboards(buttons: list) -> InlineKeyboardMarkup:
    keyboards_list = []
    for button_info in buttons:
        keyboards_list.append([InlineKeyboardButton(text=button_info[0], callback_data=button_info[1])])

    return InlineKeyboardMarkup(inline_keyboard=keyboards_list)

#
async def create_keyboards_fi(buttons: list, recallback: str) -> InlineKeyboardMarkup:
    keyboards_list = []
    for button_info in buttons:
        keyboards_list.append([InlineKeyboardButton(text=button_info[0], callback_data=button_info[1])])
    keyboards_list.append(
        [InlineKeyboardButton(text="Вернуться", callback_data=recallback)]
    )
    return InlineKeyboardMarkup(inline_keyboard=keyboards_list)


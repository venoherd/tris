from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder


# это я поменял: создаём клавиатуру через InlineKeyboardBuilder
def get_confirm_keyboard(message_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text=" Да", callback_data=f"forward_yes:{message_id}")
    builder.button(text=" Нет", callback_data=f"forward_no:{message_id}")
    builder.adjust(2)
    return builder.as_markup()
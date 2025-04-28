import json
import os
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums.chat_type import ChatType
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_cfg import bot, FILE_WAY as DATA_FILE
from rep_man.db_tools import create_muns, output_muns
from rep_man.keyboard_rep import get_confirm_keyboard

router_man = Router(name='Brd')


#чат откуда воруем
TARGET_THREAD_ID = "-1002280840951"
#все штуки
thread_messages = {}

#файл сохраннения
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"source": None, "targets": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

data = load_data()

#функция выдачи
@router_man.message(Command("send"))
async def muns_drop(message: Message):
   for tups in await output_muns(message.text.split()[1]):
       try:
           await bot.copy_message(
               chat_id=message.chat.id,
               from_chat_id=data.get("source")[0],
               message_id=int(tups[0]),
               message_thread_id=message.message_thread_id
           )
       except Exception as e:
           await message.answer(f"Ошибка при отправке в {message.chat.id}: {e}")



# это я поменял: команда /mother — установить чат-источник
@router_man.message(F.text.startswith("/mother"))
async def set_source_chat(message: Message):
    data["source"] = [message.chat.id, message.message_thread_id]
    save_data(data)
    await message.reply(
        f"Источник установлен: {message.chat.id} (тема {message.message_thread_id})"
        if message.message_thread_id else f"Источник: {message.chat.id} (без темы)"
    )

# это я поменял: команда /kid — добавить чат-приемник
@router_man.message(F.text.startswith("/kid"))
async def add_target_chat(message: Message):
    target = [message.chat.id, message.message_thread_id]
    if target not in data["targets"]:
        data["targets"].append(target)
        save_data(data)
        await message.reply(
            f"Добавлен получатель: {message.chat.id} (тема {message.message_thread_id})"
            if message.message_thread_id else f"Добавлен получатель: {message.chat.id} (без темы)"
        )
    else:
        await message.reply("Этот чат уже добавлен в список получателей.")
#сборка
@router_man.message(F.chat.type == ChatType.SUPERGROUP)
async def ask_to_forward(message: Message):
    source = data.get("source")
    if source and [message.chat.id, message.message_thread_id] == source:
        if message.text:
            teg = message.text.split("#")[1]
        elif message.caption:
            teg = message.caption.split("#")[1]
        m_id=message.message_id
        await create_muns(m_id, teg)
        await bot.send_message(
            chat_id=message.chat.id,
            text="Вы хотите переслать это сообщение в чаты?",
            reply_to_message_id=message.message_id,
            reply_markup=get_confirm_keyboard(message.message_id)
        )


# это я поменял: обработка нажатия кнопки
@router_man.callback_query(F.data.startswith("forward_"))
async def handle_forward_callback(callback: CallbackQuery):
    action, original_message_id = callback.data.split(":")
    original_message_id = int(original_message_id)

    if action == "forward_yes":

        for chat_id, thread_id in data.get("targets", []):
            try:
                await bot.copy_message(
                    chat_id=chat_id,
                    from_chat_id=callback.message.chat.id,
                    message_id=original_message_id,
                    message_thread_id=thread_id
                )
            except Exception as e:
                await callback.message.answer(f"Ошибка при отправке в {chat_id}: {e}")
        await callback.answer("Сообщение отправлено", show_alert=False)

    elif action == "forward_no":
        await callback.answer("Отправка отменена", show_alert=False)

    await callback.message.edit_reply_markup(reply_markup=None)


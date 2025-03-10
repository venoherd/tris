import asyncio

import aiosqlite
from aiogram import Router
from aiogram.types import Message


router_dic = Router(name='Dero')


#добавление и удаление
async def create_talku(keyword, backword):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO talkuser (key, back) VALUES (?, ?)",
            (keyword.lower(), backword)
        )
        await db.commit()

async def delete_talku(keyword):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            f"DELETE FROM talkuser WHERE key = '{keyword}'",
        )
        await db.commit()


#вывод данных из таблицы
async def output_word(keyword):
    async with aiosqlite.connect("database.db") as db:
        async with db.execute (
            f"SELECT back FROM talkuser WHERE key = '{keyword}'",

        ) as cursor:
            backword = await cursor.fetchone()
            if backword is None:
                return False

            return backword[0]


#вывод всего
async def allprint():
    async with aiosqlite.connect("database.db") as db:
        async with db.execute (
            f"SELECT key, back FROM talkuser",
        ) as cursor:
            backword = await cursor.fetchall()
            if backword is None:
                return False
            for ans in backword:
                print (ans[0], "|", ans[1])


#тут будет обработчик обычных сообщений
@router_dic.message()
async def handle_text_messages(message: Message):
    print (message.text)
    responses = await output_word(message.text.lower())
    if responses:
        await message.reply(str(responses))


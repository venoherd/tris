
import aiosqlite
import asyncio

from data.db_tools import create_output_keywords
from data.talkusers import create_talku, delete_talku, allprint, output_word

#таблица для проблем
async def create_all():
    async with aiosqlite.connect("keyboards.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            id_parents INTEGER,
            callback TEXT NOT NULL, 
            FOREIGN KEY (id_parents) REFERENCES problems (id) ON DELETE CASCADE

            )
        """)

# таблица для кейбордов
async def create_tables():
    async with aiosqlite.connect("keyboards.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS keyboards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS buttons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                keyboard_id INTEGER NOT NULL,
                text TEXT NOT NULL,
                callback_data TEXT NOT NULL,
                FOREIGN KEY (keyboard_id) REFERENCES keyboards (id) ON DELETE CASCADE
            )
        """)

        await db.commit()

asyncio.run(create_tables())


#таблица для ответов
async def output_search():
    async  with aiosqlite.connect("keyboards.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS keywords_inst (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
           name_problem TEXT unique,
           manual TEXT,
            keyboard_id INTEGER NOT NULL,
            FOREIGN KEY (keyboard_id) REFERENCES keyboards (id) ON DELETE CASCADE
                         
             )
         """)
        await db.commit()



asyncio.run(output_search())
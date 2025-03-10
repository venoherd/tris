
import aiosqlite
import asyncio

from data.db_tools import create_output_keywords
from data.talkusers import create_talku, delete_talku, allprint, output_word


#таблица для вайтлиста
async def create_users():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE
            )
        """)
        await db.commit()
#таблица данных по квартире
async def create_apartment():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS apartment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                creator_id INTEGER, 
                apartment_number TEXT,
                address TEXT,
                time_create DATETIME DEFAULT current_timestamp,
                last_update DATETIME DEFAULT current_timestamp,
                status TEXT,
                FOREIGN KEY(creator_id) REFERENCES users(id)
            )
        """)
        await db.commit()
#таблица данных по комнатам
async def create_rooms():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                apartment_id INTEGER,
                room_number INTEGER,
                time_create DATETIME DEFAULT current_timestamp,
                creator_id INTEGER,
                FOREIGN KEY(apartment_id) REFERENCES apartment(id), 
                FOREIGN KEY(creator_id) REFERENCES users(id)
            )
        """)
        await db.commit()
#Таблица по вопросам
async def create_question():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT,
                answers TEXT,
                tags TEXT
            )
        """)
        await db.commit()

#Связанная таблица
async def create_answers():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
             CREATE TABLE IF NOT EXISTS answers (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 room_id INTEGER,
                 question_id INTEGER, 
                 answer INTEGER,
                 data TEXT NULL,
                 FOREIGN KEY(room_id) REFERENCES rooms(id),
                 FOREIGN KEY(question_id) REFERENCES question(id)
             )
         """)
        await db.commit()

#Таблица для запросов
async def create_talkuser():
    async  with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS talkuser (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT unique, 
            back TEXT  
             )
         """)
        await db.commit()


#таблица для кейбордов
async def output_keywords():
    async  with aiosqlite.connect("COCACOLA.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS keywords_inst (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
           name_problem TEXT unique,
           manual TEXT              
             )
         """)
        await db.commit()



asyncio.run(create_output_keywords("locer_2","Локер не открывается \n \n1. Отправьте в чат фото локера издалека, чтобы супервайзер убедилась в том, что вы открываете наш локер. \n \n2. Одновременно сами убедитесь, что локер наш. \nСравните фото локера и расположение локера в программе в блоке \"как войти в квартиру\" \n \n3. Нужно поболтать локер, чтобы по звуку  понять есть ли ключи внутри \n \n4. Гости могут разместить ключи внутри локера неверно, из-за чего могут заблокировать локер, для этого нужно стукнуть локер \n \n5. Если не помогло, нужно перевернуть локер и открывать его в перевёрнутом положении"))
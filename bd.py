import aiosqlite
import asyncio

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
#
async def create_rooms():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE
            )
        """)
        await db.commit()
#
async def create_qus():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE
            )
        """)
        await db.commit()

#
async def create_ans():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
             CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER UNIQUE
             )
         """)
        await db.commit()

asyncio.run(create_apartment())
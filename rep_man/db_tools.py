import aiosqlite
import asyncio

async def create_muns(tg_m_id, teg):
    async with aiosqlite.connect("keyboards.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO muns (tg_m_id, teg) VALUES (?, ?)",
            (tg_m_id, teg)
        )
        await db.commit()
 #выкидываем
async def output_muns(name_teg):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute (
            f"SELECT tg_m_id, teg FROM muns WHERE teg = '{name_teg}'",

        ) as cursor:
            manual = await cursor.fetchall()
            if manual is None:
                return False

            return manual
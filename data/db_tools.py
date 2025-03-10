import aiosqlite
import asyncio

#заполнение базы с проблемами
async def create_output_keywords(name_problem, manual):
    async with aiosqlite.connect("COCACOLA.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO keywords_inst (name_problem, manual) VALUES (?, ?)",
            (name_problem.lower(), manual)
        )
        await db.commit()

#берем данные из таблицы
async def output_words(name_problem):
    async with aiosqlite.connect("COCACOLA.db") as db:
        async with db.execute (
            f"SELECT manual FROM keywords_inst WHERE name_problem = '{name_problem}'",

        ) as cursor:
            manual = await cursor.fetchone()
            if manual is None:
                return False

            return manual[0]


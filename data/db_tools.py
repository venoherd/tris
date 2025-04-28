import aiosqlite
import asyncio

#создание клавиатуры
async def insert_keyboard(name: str):
    async with aiosqlite.connect("keyboards.db") as db:
        await db.execute("INSERT INTO keyboards (name) VALUES (?)", (name,))
        await db.commit()

#добавление кнопок
async def insert_button(keyboard_name: str, text: str, callback_data: str):
    async with aiosqlite.connect("keyboards.db") as db:
        # Получаем ID клавиатуры
        async with db.execute("SELECT id FROM keyboards WHERE name = ?", (keyboard_name,)) as cursor:
            keyboard_id = await cursor.fetchone()
            if not keyboard_id:
                print("Клавиатура не найдена!")
                return

            keyboard_id = keyboard_id[0]

        # Добавляем кнопку
        await db.execute("INSERT INTO buttons (keyboard_id, text, callback_data) VALUES (?, ?, ?)",
                         (keyboard_id, text, callback_data))
        await db.commit()


#заполнение базы с проблемами
async def create_output_keywords(name_problem, manual):
    async with aiosqlite.connect("COCACOLA.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO keywords_inst (name_problem, manual) VALUES (?, ?)",
            (name_problem.lower(), manual)
        )
        await db.commit()

#удаление коллбеков





#eey2
async def output_par(id: int):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute(
                f"SELECT name, callback FROM problems p WHERE p.id_parents = '{id}';",

        ) as cursor:
            children = await cursor.fetchall()
            if children is None:
                return None

            return children

#eey
async def output_mains(name_callback):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute (
            f"SELECT id, text, id_parents FROM problems WHERE callback = '{name_callback}'",

        ) as cursor:
            manual = await cursor.fetchone()
            if manual is None:
                return False

            return manual

#берем данные из таблицы
async def output_words(name_problem):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute (
            f"SELECT manual FROM keywords_inst WHERE name_problem = '{name_problem}'",

        ) as cursor:
            manual = await cursor.fetchone()
            if manual is None:
                return False

            return manual[0]

async def output_keyboards(name_problem):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute (
            f" SELECT b.text,b.callback_data FROM keywords_inst ki JOIN buttons b on b.keyboard_id = ki.keyboard_id WHERE ki.name_problem = '{name_problem}'",

        ) as cursor:
            buttons = await cursor.fetchall()
            if buttons is None:
                return False

            return buttons

async def output_recall(id_parents):
    async with aiosqlite.connect("keyboards.db") as db:
        async with db.execute (
            f"SELECT callback FROM problems WHERE id = '{id_parents}'",

        ) as cursor:
            eee = await cursor.fetchone()
            if eee is None:
                return False

            return eee[0]



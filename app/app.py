from flask import Flask, render_template, request, jsonify
import asyncio
import aiosqlite

app = Flask(__name__)

# Путь к вашей базе данных
DB_PATH = r"C:\Users\Venoherd\OneDrive\Dokumente\GitHub\tris\database.db"


# Ваша асинхронная функция для добавления данных в базу
async def create_talku(keyword, backword):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO talkuser (key, back) VALUES (?, ?)",
            (keyword.lower(), backword)
        )
        await db.commit()
    return f"Данные добавлены: {keyword}, {backword}"


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/bot.html')
def bot():
    return render_template('bot.html')

@app.route('/talk', methods=['POST'])
def talk():
    keyword = request.form.get('keyword')
    backword = request.form.get('backword')

    # Запускаем асинхронную функцию
    result = asyncio.run(create_talku(keyword, backword))

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)

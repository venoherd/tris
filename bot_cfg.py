from aiogram import Bot
from dotenv import dotenv_values

token = dotenv_values(".env")
bot = Bot(token=token["token"])

FILE_WAY = "C:/Users/Venoherd/OneDrive/Dokumente/GitHub/tris/cuccu.json"
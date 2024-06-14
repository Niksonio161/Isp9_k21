from data import config
from aiogram import Bot, types, Dispatcher
import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_admin_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Пользователи')]
])

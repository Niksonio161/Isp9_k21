from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_user_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='Профиль'), KeyboardButton(text='Выбрать компьютер')],
    [KeyboardButton(text='Купить часы')]
])

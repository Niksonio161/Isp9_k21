from loader import dp

from aiogram import types


@dp.message_handler(text='Выбрать компьютер')
async def choose_computer(message: types.Message):
    await message.answer('Функция в разработке')
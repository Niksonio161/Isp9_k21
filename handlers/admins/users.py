from aiogram import types

from loader import dp, cursor


@dp.message_handler(text='Пользователи')
async def us(message: types.Message):
    tg_user_id = message.from_user.id
    is_admin = cursor.execute(f'''SELECT is_admin FROM users WHERE telegram_id = {tg_user_id}''').fetchall()[0]
    if is_admin:
        users = cursor.execute('''SELECT * FROM users''').fetchall()
        message_send = 'Пользователи:\n\n'
        for user in users:
            uid, full_name, phone_number, _, balance, hours, points, _, _ = user
            message_send += (f'UID: {uid}\nИмя: {full_name}\nНомер телефона: {phone_number}\nБаланс: '
                             f'{balance}\nКупленные часы: {hours}\nБонусные баллы: {points}\n\n')
        await message.answer(message_send)

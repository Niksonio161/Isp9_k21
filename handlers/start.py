from aiogram import types

from loader import dp, cursor,conn

from keyboards import contact_keyboard, start_user_kb, start_admin_kb


@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=await contact_keyboard())


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    tg_user_id = message.from_user.id
    user = cursor.execute(f'''SELECT uid FROM users WHERE telegram_id = {tg_user_id}''').fetchall()
    if user:
        await message.answer('Привет admin', reply_markup=start_admin_kb)
    else:
        try:
            cursor.execute(f"""insert into users(full_name, phone_number, user_name, balance, hours, points,
            is_admin, telegram_id) values('{contact.full_name}', '{contact.phone_number}', '{message.from_user.username}',
            0, 0, 0, False, {contact.user_id});""")
            conn.commit()
            await message.answer("Добро пожаловать в PC clube", reply_markup=start_user_kb)
        except:
            await message.answer("Вы уже зарегестррированы", reply_markup=start_user_kb)

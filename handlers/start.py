from aiogram import types

from loader import dp, cursor,conn

from keyboarts import contact_keyboard


@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=await contact_keyboard())


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact

    try:
        cursor.execute(f"""insert into users(full_name, phone_number, user_name, balance, points,
        is_admin, telegram_id) values('{contact.full_name}', '{contact.phone_number}', '{message.from_user.username}',
        0, 0, False, {contact.user_id});""")
        conn.commit()
        await message.answer("Добро пожаловать в PC clube")
    except:
        await message.answer("вы уже зарегестррированы")

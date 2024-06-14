from loader import dp, cursor
from keyboards.inlines import plans_ikb
from aiogram import types


@dp.message_handler(text='Купить часы')
async def buy_hour(message: types.Message):
    await message.answer('Выберите сколько часов хотите купить', reply_markup=plans_ikb)


@dp.callback_query_handler(lambda x: x.data.startswith('hour_'))
async def choose_hour(call: types.CallbackQuery):
    kol_vo = call.data.split('_')[1]
    tg_user_id = call.from_user.id
    balance = cursor.execute(f'''SELECT balance FROM users WHERE telegram_id = {tg_user_id}''').fetchall()[0][0]
    hours = cursor.execute(f'''SELECT hours FROM users WHERE telegram_id = {tg_user_id}''').fetchall()[0][0]
    if kol_vo == '1':
        if int(balance) < 110:
            await call.message.answer('У вас недостаточно средств, пополните баланс')
        else:
            cursor.execute(f'''UPDATE users SET hours = {int(hours) + 1} WHERE telegram_id = {tg_user_id}''')
            cursor.execute(f'''UPDATE users SET balance = {int(balance) - 110} WHERE telegram_id = {tg_user_id}''')
            await call.message.answer('Часы успешно куплены')
    elif kol_vo == '3':
        if int(balance) < 300:
            await call.message.answer('У вас недостаточно средств, пополните баланс')
        else:
            cursor.execute(f'''UPDATE users SET hours = {int(hours) + 3} WHERE telegram_id = {tg_user_id}''')
            cursor.execute(f'''UPDATE users SET balance = {int(balance) - 300} WHERE telegram_id = {tg_user_id}''')
            await call.message.answer('Часы успешно куплены')
    elif kol_vo == '5':
        if int(balance) < 500:
            await call.message.answer('У вас недостаточно средств, пополните баланс')
        else:
            cursor.execute(f'''UPDATE users SET hours = {int(hours) + 5} WHERE telegram_id = {tg_user_id}''')
            cursor.execute(f'''UPDATE users SET balance = {int(balance) - 500} WHERE telegram_id = {tg_user_id}''')
            await call.message.answer('Часы успешно куплены')
    elif kol_vo == '10':
        if int(balance) < 900:
            await call.message.answer('У вас недостаточно средств, пополните баланс')
        else:
            cursor.execute(f'''UPDATE users SET hours = {int(hours) + 10} WHERE telegram_id = {tg_user_id}''')
            cursor.execute(f'''UPDATE users SET balance = {int(balance) - 900} WHERE telegram_id = {tg_user_id}''')
            await call.message.answer('Часы успешно куплены')

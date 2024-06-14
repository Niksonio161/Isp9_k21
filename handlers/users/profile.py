from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import TEST_PAY
from keyboards.inlines import balance_ikb, cancel_balance_ikb
from loader import dp, cursor, bot, conn
from states import AddBalance


@dp.callback_query_handler(text='balance_cancel', state=AddBalance)
async def canc(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Отменено')


@dp.message_handler(text='Профиль')
async def profile(message: types.Message):
    tg_user_id = message.from_user.id
    user = cursor.execute(f'''SELECT * FROM users WHERE telegram_id = {tg_user_id}''').fetchall()
    if user:
        uid, full_name, phone_number, _, balance, hours, points, _, _ = user[0]
        await message.answer(f'UID: {uid}\n'
                             f'Имя: {full_name}\n'
                             f'Номер телефона: {phone_number}\n'
                             f'Баланс: {balance}\n'
                             f'Купленные часы: {hours}\n'
                             f'Бонусные баллы: {points}', reply_markup=balance_ikb)


@dp.callback_query_handler(text='add_balance')
async def add_balance(call: types.CallbackQuery):
    await call.message.answer('Введите сумма платежа', reply_markup=cancel_balance_ikb)
    await AddBalance.sum.set()


@dp.message_handler(content_types=['text'], state=AddBalance.sum)
async def sm_balance(message: types.Message, state: FSMContext):
    if message.text.isdigit() and int(message.text) > 99:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title='Пополнение баланса',
            description='Добро пожаловать в компьютерный клуб "PC Clube"💻 Cпасибо, что Вы с нами! ❤️',
            payload=f'Pay',
            provider_token=TEST_PAY,
            currency='rub',
            photo_url='https://i.yapx.cc/VP1Ff.jpg',
            photo_height=512,  # !=0/None, иначе изображение не покажется
            photo_width=512,
            photo_size=512,
            prices=[
                types.LabeledPrice(
                    label='Пополнение баланса',
                    amount=int(message.text) * 100
                )
            ]
        )
        await state.finish()
    else:
        await message.answer('Некорректная сумма попробуйте снова', reply_markup=cancel_balance_ikb)


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    tg_user_id = message.from_user.id
    amount = message.successful_payment.to_python()['total_amount'] // 100
    balance = cursor.execute(f'''SELECT balance FROM users WHERE telegram_id = {tg_user_id}''').fetchall()[0][0]
    cursor.execute(f'''UPDATE users SET balance = {amount + balance} WHERE telegram_id = {tg_user_id}''')
    conn.commit()
    await message.answer('Баланс пополнен')


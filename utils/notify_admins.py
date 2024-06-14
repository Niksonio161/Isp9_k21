from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id=2095407388, text='Bot Started')
    await dp.bot.send_message(chat_id=981197616, text='Bot Started')


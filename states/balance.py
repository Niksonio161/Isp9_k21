from aiogram.dispatcher.filters.state import StatesGroup, State


class AddBalance(StatesGroup):
    sum = State()

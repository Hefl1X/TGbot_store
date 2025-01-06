from aiogram.fsm.state import State, StatesGroup


class AdminState(StatesGroup):
    newsletter = State()
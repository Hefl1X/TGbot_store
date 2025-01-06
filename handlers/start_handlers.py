from aiogram import types, Router
from aiogram.filters import Command


start_handler_router = Router(name=__name__)
from database_query.datab import add_user
from bot_config import admin_id

@start_handler_router.message(Command('start'))
async def start_command(message):
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    kb = [
        [types.KeyboardButton(text='каталог')],
        [types.KeyboardButton(text='профиль'), types.KeyboardButton(text='тех.поддержка')],
        [types.KeyboardButton(text='о нас')]]
    
    if message.from_user.id in admin_id:
        kb[-1] +=  [types.KeyboardButton(text='админ-панель')]
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
        await message.answer('Добро пожаловать в магазин!', reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
        await message.answer('Добро пожаловать в магазин!', reply_markup=keyboard)
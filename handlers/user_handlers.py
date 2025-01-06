from aiogram import F, types, Router


user_handler_router = Router(name=__name__)

@user_handler_router.message(F.text == 'каталог')
@user_handler_router.callback_query(F.data == 'back')
async def catalog(message):
    kb = [
        [types.InlineKeyboardButton(text='Курс по Python', callback_data='Python'),types.InlineKeyboardButton(text='Курс по Aiogram', callback_data='Aiogram' ) ],
        [types.InlineKeyboardButton(text='Курс по Telebot', callback_data='Telebot'),types.InlineKeyboardButton(text='Курс по Django', callback_data='Django')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    if isinstance(message, types.Message):
        await message.answer(text='выберите товар', reply_markup=keyboard)
    else:
        await message.message.edit_text(text='выберите товар', reply_markup=keyboard)
        
        
        

@user_handler_router.callback_query(F.data == 'Python')
@user_handler_router.callback_query(F.data == 'Aiogram')
@user_handler_router.callback_query(F.data == 'Telebot')
@user_handler_router.callback_query(F.data == 'Django')
async def course(call):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='купить', callback_data='buy'), types.InlineKeyboardButton(text='назад', callback_data='back')]
        ])
    if call.data == 'Python':
        await call.message.answer('Начальный курс по программирыванию на Python', reply_markup=kb)
    elif call.data == 'Aiogram':
        await call.message.edit_text('Начальный курс по программирыванию на Aiogram', reply_markup=kb)
    elif call.data == 'Telebot':
        await call.message.edit_text('Начальный курс по программирыванию на Telebot', reply_markup=kb)
    elif call.data == 'Django':
        await call.message.edit_text('Начальный курс по программирыванию на Django', reply_markup=kb)

@user_handler_router.callback_query(F.data == 'buy')
async def buy(call):
    await call.message.edit_text(f'вы купили курс!')

@user_handler_router.message(F.text == 'профиль')
async def profile(message):
    await message.answer(f'''Имя: {message.from_user.username}
Id: {message.from_user.id}
Баланс: 1000000000000000 RUB''')

@user_handler_router.message(F.text == 'тех.поддержка')
async def support(message):
    await message.answer('https://t.me/Hefl1X')
    
    
@user_handler_router.message(F.text == 'о нас')
async def about_us(message):
    await message.answer(text='тестовый бот')

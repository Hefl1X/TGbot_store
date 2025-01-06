import asyncio
from aiogram import F, types, Router
from states.admin_states import AdminState
from filters.admin_filter import IsAdmin
from database_query.datab import get_all_user_id, get_user_count

admin_handler_router = Router(name=__name__)



@admin_handler_router.message(F.text == 'админ-панель', IsAdmin())
async def admin_panel(message):
    kb = [
        [types.InlineKeyboardButton(text='статистика', callback_data='statistic'), types.InlineKeyboardButton(text='рассылка', callback_data='mailing')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Welcome to the admin-panel!', reply_markup=keyboard)


@admin_handler_router.callback_query(F.data == 'statistic', IsAdmin())
async def statistic(call):
    count_users = await get_user_count()
    await call.message.answer(f'Всего пользователей в боте: {count_users}')


@admin_handler_router.callback_query(F.data == 'mailing', IsAdmin())
async def mailing(call, state):
    kb = [
        [types.InlineKeyboardButton(text='отменить', callback_data='close')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await call.message.edit_text('РАССЫЛКА\n\nВведите сообщение,которое будет отправлено пользователям:', reply_markup=keyboard)
    await state.set_state(AdminState.newsletter)
    


@admin_handler_router.callback_query(AdminState.newsletter)
async def mailing_send_callback(call, state):
    await state.clear()
    await call.message.answer('Рассылка отменена')
    

@admin_handler_router.message(AdminState.newsletter)
async def mailing_send(message, state, bot):
    users_id = await get_all_user_id()
    msg = message.text
    count = 0
    await state.clear()
    for user_id in users_id:
        try:
            await bot.send_message(user_id, msg)
            await asyncio.sleep(0.3)
            count += 1
        except:
            pass
    user_count = len(users_id)
    await message.answer(f'Рассылка завершена.\nСообщений дошло: {count} из {user_count}')

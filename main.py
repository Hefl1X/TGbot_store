import asyncio
from aiogram import Dispatcher, Bot, Router
from bot_config import bot_token
from handlers.admin_handlers import admin_handler_router
from handlers.start_handlers import start_handler_router
from handlers.user_handlers import user_handler_router

dp = Dispatcher()
router = Router()



async def main():
    bot = Bot(token=bot_token)
    dp.include_routers(start_handler_router, user_handler_router, admin_handler_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



    
if __name__ == "__main__":
    asyncio.run(main())
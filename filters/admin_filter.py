from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject
from bot_config import admin_id


class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject):
        return obj.from_user.id in admin_id
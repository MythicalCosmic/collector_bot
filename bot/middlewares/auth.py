from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from database.database import async_session
from utils.helpers import get_or_create_user


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        if isinstance(event, Message) and event.from_user:
            async with async_session() as session:
                user = await get_or_create_user(session, event.from_user)

                data["user"] = user
                data["session"] = session

                result = await handler(event, data)
                return result

        return await handler(event, data)

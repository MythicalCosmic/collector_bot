"""
Main bot entry point
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from core.config import config
from core.logging import setup_logging
from database.database import init_db, engine
from bot.handlers import register_handlers
from bot.middlewares.auth import AuthMiddleware
from bot.middlewares.throttling import ThrottlingMiddleware

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(AuthMiddleware())

    try:
        await init_db()
        logger.info("Database initialized")

        register_handlers(dp)
        logger.info("Handlers registered")

        logger.info("Bot started")
        await dp.start_polling(bot)

    finally:
        logger.info("Shutting down...")

        await bot.session.close()     # 👈 VERY IMPORTANT
        await engine.dispose()        # 👈 VERY IMPORTANT

        logger.info("Resources cleaned up")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")

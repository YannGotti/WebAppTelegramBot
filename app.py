from loader import bot, storage
from services.service import *


async def on_shutdown(dp):
    await storage.close()
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, skip_updates=True)
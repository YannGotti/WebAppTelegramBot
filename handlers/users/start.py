from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import markups as nav
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
from loader import dp, bot
from services.service import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not userExists(message.from_user.id):
        addUser(message.from_user.id)
    await message.answer("Салам")



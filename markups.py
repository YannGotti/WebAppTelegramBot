from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test", 
    web_app=WebAppInfo(url="https://nyavro.github.io/index2.html")))
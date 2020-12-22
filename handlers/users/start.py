from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from re import compile

# "t.me/bot?start=deep_link"
# "/start deep_link"

@dp.message_handler(CommandStart(deep_link=compile(r'\d\d\d')), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
# from filters import IsPrivate
from loader import dp
from re import compile

# "t.me/bot?start=deep_link"
# "/start deep_link"

@dp.message_handler(CommandStart(deep_link=compile(r'\d\d\d')))
async def bot_start(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке\n'
                         f'В вашей команде есть дип линк\n'
                         f'вы передали аргумент {deep_link_args}.\n')

@dp.message_handler(CommandStart(deep_link=None))
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    deep_link = f'http://t.me{bot_user.username}?start=123'
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде нет диплинка. \n'
                         f'Ваша диплинк сслыка - {deep_link}')

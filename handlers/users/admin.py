from aiogram import types
from filters import IsPrivate
from loader import dp

from data.config import admins


# только слово secret и только от пользователей-админов попадает
# user_id=32131654 можно передать айди напрямую
@dp.message_handler(IsPrivate(), text='secret', user_id=admins)
async def admin_chat_secret(message:types.Message):
    await message.answer('"Это секретное сообщение вызванное одним из админов')

from aiogram import types
from loader import dp

# варианта два - либо через декоратор регистрировать хендлеры
# либо через registration
@dp.message_handler()
# по умолчанию только текстовые сообщения летят сюда
# если нужны другие типы то нужно указать явно
# @dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.answer(message.text)

    # получим chat_id и text
    chat_id = message.from_user.id
    text = message.text

# получим объект бота из диспатчера
# bot = dp.bot
# получим объект бота из контекста
# from aiogram import Bot
# bot = Bot.get_current()
# получим объект бота из модуля loader

from loader import bot

# Отправим сообщение пользователю (1 вариант)
await bot.send_message(chat_id=chat_id, text=text)
# используем встроенный метод answer / reply
# await message.answer(text=text)

# порядок хендлеров в коде имеет значение




from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


# инстанс класса бот импортированный из аиограма
# для запросов из API
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# переменная для хранения данных в машине состояний
storage = MemoryStorage()
# обработчик апдейтов
dp = Dispatcher(bot, storage=storage)


# dp.loop
# dp.bot
# dp.storage

# подгружаем переменные

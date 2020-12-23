from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_bot_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
    ])

# async def set_bot_commands(dp):
#     await dp.bot.set_bot_commands()


# async def set_bot_commands(dp):
#     return None
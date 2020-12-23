from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

# чтобы делать свои фильтры нужно импортнуть BoundFilter


class IsPrivate(BoundFilter):

    async def check(self, message: type.Message):
        return message.chat.type == types.ChatType.PRIVATE
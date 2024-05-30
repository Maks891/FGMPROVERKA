from aiogram import types, Dispatcher
import commands.property.db as db
from commands.db import url_name
from commands.main import win_luser
from bot import bot
from assets.antispam import antispam
from commands.pet.lists import *


@antispam
async def pet_list(message: types.Message):
    name = await url_name(message.from_user.id)
    await message.answer(f'''{name}, доступные вертолёты:
1. Бомж
2. Валера
3. Иди нахуй

🛒 Для покупки вертолёта введите "Купить вертолет [номер]"''')






@antispam
async def my_pet(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[5] == 0:
        await message.answer(f'{name}, к сожалению у вас нет своего пита {rloser}')
        return

    hdata = pet.get(data[5])
    await bot.send_photo(chat_id=message.chat.id, photo=hdata[1], caption=f'{name}, ваш дом "{hdata[0]}"')



def reg(dp: Dispatcher):
    dp.register_message_handler(pet_list, lambda message: message.text.lower().startswith(('питы', 'пит')))
    
    dp.register_message_handler(my_pet, lambda message: message.text.lower().startswith(('мой пит', 'мой пит')))
    

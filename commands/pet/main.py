from aiogram import types, Dispatcher
import commands.property.db as db
from commands.db import url_name
from commands.main import win_luser
from bot import bot
from assets.antispam import antispam
from commands.property.lists import *


@antispam
async def helicopters_list(message: types.Message):
    name = await url_name(message.from_user.id)
    await message.answer(f'''{name}, доступные вертолёты:
🚁 1. Воздушный шар - 100.000$
🚁 2. RotorWay Exec 162F - 3.500.000$
🚁 3. Robinson R44 - 10.000.000$
🚁 4. Hiller UH-12C - 30.000.000$
🚁 5. AW119 Koala - 63.400.000$
🚁 6. MBB BK 117 - 150.000.000$
🚁 7. Eurocopter EC130 - 350.000.000$
🚁 8. Leonardo AW109 Power - 750.000.000$
🚁 9. Sikorsky S-76 - 1.240.000.000$
🚁 10. Bell 429WLG - 8.890.000.000$
🚁 11. NHI NH90 - 88.330.000.000$
🚁 12. Kazan Mi-35M - 225.750.000.000$
🚁 13. Bell V-22 Osprey - 945.300.000.000$

🛒 Для покупки вертолёта введите "Купить вертолет [номер]"''')


@antispam
async def my_helicopter(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[1] == 0:
        await message.answer(f'{name}, к сожалению у вас нет вертолёта {rloser}')
        return

    hdata = helicopters.get(data[1])

    txt = f'''{name}, информация о вашем вертолёте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await bot.send_photo(chat_id=message.chat.id, photo=hdata[3], caption=txt)


@antispam
async def my_phone(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[4] == 0:
        await message.answer(f'{name}, к сожалению у вас нет телефона {rloser}')
        return

    hdata = phones.get(data[4])
    await bot.send_photo(chat_id=message.chat.id, photo=hdata[1], caption=f'{name}, ваш телефон "{hdata[0]}"')


@antispam
async def my_car(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[2] == 0:
        await message.answer(f'{name}, к сожалению у вас нет автомобиля {rloser}')
        return

    hdata = cars.get(data[2])

    txt = f'''{name}, информация о вашем автомобиле "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}
⏱ Разгон до 100 за {hdata[3]} сек'''

    await bot.send_photo(chat_id=message.chat.id, photo=hdata[4], caption=txt)


@antispam
async def my_house(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[5] == 0:
        await message.answer(f'{name}, к сожалению у вас нет своего дома {rloser}')
        return

    hdata = house.get(data[5])
    await bot.send_photo(chat_id=message.chat.id, photo=hdata[1], caption=f'{name}, ваш дом "{hdata[0]}"')


@antispam
async def my_yahta(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[3] == 0:
        await message.answer(f'{name}, к сожалению у вас нет своей яхты {rloser}')
        return

    hdata = yahts.get(data[3])

    txt = f'''{name}, информация о вашей яхте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await bot.send_photo(chat_id=message.chat.id, photo=hdata[3], caption=txt)


@antispam
async def my_plane(message: types.Message):
    name = await url_name(message.from_user.id)
    rwin, rloser = await win_luser()
    data = await db.get_property(message.from_user.id)
    if data[6] == 0:
        await message.answer(f'{name}, к сожалению у вас нет своего самолёта {rloser}')
        return

    hdata = planes.get(data[6])

    txt = f'''{name}, информация о вашем самолёте "{hdata[0]}"
⛽️ Максимальная скорость: {hdata[1]} км/ч
🐎 Лошадиных сил: {hdata[2]}'''

    await bot.send_photo(chat_id=message.chat.id, photo=hdata[3], caption=txt)


def reg(dp: Dispatcher):
    dp.register_message_handler(helicopters_list, lambda message: message.text.lower().startswith(('вертолеты', 'вертолёты')))
    dp.register_message_handler(cars_list, lambda message: message.text.lower().startswith('машины'))
    dp.register_message_handler(yahta_list, lambda message: message.text.lower().startswith('дома'))
    dp.register_message_handler(phone_list, lambda message: message.text.lower().startswith('телефоны'))
    dp.register_message_handler(plane_list, lambda message: message.text.lower().startswith(('самолеты', 'самолёты')))

    dp.register_message_handler(my_helicopter, lambda message: message.text.lower().startswith(('мой вертолет', 'мой вертолёт')))
    dp.register_message_handler(my_phone, lambda message: message.text.lower().startswith('мой телефон'))
    dp.register_message_handler(my_car, lambda message: message.text.lower().startswith('моя машина'))
    dp.register_message_handler(my_house, lambda message: message.text.lower().startswith('мой дом'))
    dp.register_message_handler(my_yahta, lambda message: message.text.lower().startswith('моя яхта'))
    dp.register_message_handler(my_plane, lambda message: message.text.lower().startswith(('мой самолет', 'мой самолёт')))

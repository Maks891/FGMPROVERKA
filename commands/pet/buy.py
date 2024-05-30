from aiogram import types, Dispatcher
import commands.property.db as db
from commands.db import url_name, get_balance
from commands.main import win_luser
from commands.property.lists import *
from assets.antispam import antispam


@antispam
async def buy_helicopter(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[1] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = helicopters.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[4]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили вертолёт "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'helicopter', hdata[4])


@antispam
async def buy_phone(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[4] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = phones.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[2]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили телефон "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'phone', hdata[2])


@antispam
async def buy_car(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[2] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = cars.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[5]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили машину "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'car', hdata[5])


@antispam
async def buy_house(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[4] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = house.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[2]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили дом "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'house', hdata[2])


@antispam
async def buy_yahta(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[3] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = yahts.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[4]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили яхту "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'yahta', hdata[4])


@antispam
async def buy_plane(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    balance = await get_balance(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[6] != 0:
        await message.answer(f'{name}, у вас уже есть данный тип имущества {rloser}')
        return

    try:
        num = int(message.text.split()[2])
    except:
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    hdata = planes.get(num, 'no')
    if hdata == 'no':
        await message.answer(f'{name}, вы не ввели число имущества или привелегии которое хотите купить {rloser}')
        return

    if balance < hdata[4]:
        await message.answer(f'{name}, у вас недостаточно денег для покупки имущества {rloser}')
        return

    await message.answer(f'{name}, вы успешно купили самолёт "{hdata[0]}" 🎉')
    await db.buy_property(user_id, num, 'plane', hdata[4])



@antispam
async def sell_yahta(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[3] == 0:
        await message.answer(f'{name}, у вас нет данного имущества {rloser}')
        return

    hdata = yahts.get(data[3])
    summ = int(hdata[4] * 0.75)
    summ2 = '{:,}'.format(summ).replace(',', '.')

    await message.answer(f'{name}, вы успешно продали яхту за {summ2}$ 🎉')
    await db.sell_property(user_id, 'yahta', summ)


@antispam
async def sell_plane(message: types.Message):
    user_id = message.from_user.id
    name = await url_name(user_id)
    rwin, rloser = await win_luser()
    data = await db.get_property(user_id)

    if data[6] == 0:
        await message.answer(f'{name}, у вас нет данного имущества {rloser}')
        return

    hdata = planes.get(data[6])
    summ = int(hdata[4] * 0.75)
    summ2 = '{:,}'.format(summ).replace(',', '.')

    await message.answer(f'{name}, вы успешно продали самолёт за {summ2}$ 🎉')
    await db.sell_property(user_id, 'plane', summ)


def reg(dp: Dispatcher):
    dp.register_message_handler(buy_pet, lambda message: message.text.lower().startswith(('купить питомца', 'купить питомец')))
    
    dp.register_message_handler(sell_pet, lambda message: message.text.lower().startswith(('продать питомца', 'продать питомец')))

from _decimal import Decimal
from commands.db import register_users, getname, getonlibalance, getidname, getads
from commands.main import geturl
from commands.main import win_luser
from commands.ore.db import *


async def sellbtc(message):
    await register_users(message)
    user_name = await getname(message)
    user_id = message.from_user.id
    btc = await getbtc(message)
    url = await geturl(user_id, user_name)
    result = await win_luser()
    rwin, rloser = result

    try:
        summ_btc = int(message.text.split()[2])
    except:
        summ_btc = btc
    summ_btc = Decimal(summ_btc)

    kurs = await getkurs()
    summ = summ_btc * kurs
    summ2 = '{:,}'.format(summ).replace(',', '.')
    summ_btc2 = '{:,}'.format(summ_btc).replace(',', '.')

    if btc >= summ_btc:
        if btc - summ_btc >= 0 and summ_btc > 0:
            await sellbtc_db(summ, summ_btc, user_id)
            await message.answer(f'{url}, вы успешно продали {summ_btc2} BTC за {summ2}$ {rwin}', parse_mode='html')
        else:
            await message.answer(f'{url}, нельзя продавать отрицательно или же нулевое количество BTC {rloser}',
                                 parse_mode='html')
    else:
        await message.answer(f'{url}, вы не можете продать столько BTC {rloser}', parse_mode='html')


async def buybtc(message):
    await register_users(message)
    user_name = await getname(message)
    user_id = message.from_user.id
    balance = await getonlibalance(message)
    url = await geturl(user_id, user_name)
    result = await win_luser()
    rwin, rloser = result

    try:
        summ_btc = int(message.text.split()[2])
    except:
        await message.answer(f'{url}, вы не ввели количество BTC которое хотите купить {rloser}', parse_mode='html')
        return
    summ_btc = Decimal(summ_btc)

    kurs = await getkurs()
    summ = summ_btc * kurs
    summ2 = '{:,}'.format(summ).replace(',', '.')
    summ_btc2 = '{:,}'.format(summ_btc).replace(',', '.')

    if balance >= summ:
        if summ_btc > 0:
            await bybtc_db(summ, summ_btc, user_id)
            await message.answer(f'{url}, вы успешно купили {summ_btc2} BTC за {summ2}$ {rwin}', parse_mode='html')
        else:
            await message.answer(f'{url}, нельзя покупать отрицательно или же нулевое количество BTC {rloser}',
                                 parse_mode='html')
    else:
        await message.answer(f'{url}, у вас недостаточно денег для покупки BTC {rloser}', parse_mode='html')


async def btc_kurs(message):
    await register_users(message)
    user_name = await getname(message)
    user_id = message.from_user.id
    url = await geturl(user_id, user_name)
    kurs = await getkurs()
    ads = await getads(message)
    kurs = '{:,}'.format(kurs).replace(',', '.')
    await message.answer(f'{url}, на данный момент курс 1 BTC составляет - {kurs}$ 🌐\n\n{ads}', parse_mode='html',
                         disable_web_page_preview=True)

from commands.earnings.garden.db import *
from commands.db import register_users, getname, getonlibalance, getidname
from commands.main import geturl
from commands.main import win_luser


async def potions_list(message):
    id = message.from_user.id
    name = await getname(message)
    url = await geturl(id, name)
    await register_users(message)
    await message.answer(f'''{url}, доступные зелья:
🍸 1. Чай: 40 зёрен
Прибыль: 1 энергия

🍸 2. Чефир: 240 зёрен
Прибыль: 5 энергии

🍸 3. Кофе: 520 зёрен
Прибыль: 10 энергии

🍸 4. Энергетик: 1.120 зёрен
Прибыль: 20 энергии

🍸 5. Крепкий кофе: 2.400 зёрен
Прибыль: 40 энергии

🍸 6. Настойка из вишни: 3.000 зёрен
Прибыль: 50 энергии

🍸 7. Сыворотка из плазмы: 30.000 зёрен
Прибыль: 400 энергии

🛒 Для покупки зелья введите "Создать зелье [номер]"
⛔ При покупке зелья энергия начисляется сразу.''', parse_mode='html')


async def bay_potions(message):
    id = message.from_user.id
    name = await getname(message)
    url = await geturl(id, name)
    await register_users(message)
    result = await win_luser()
    rwin, rloser = result
    corn = await getcorn(id)
    try:
        n = int(message.text.split()[2])
    except:
        await message.answer(f'{url}, вы не ввели номер зелья которое хотите сделать {rloser}', parse_mode='html')
        return

    if n == 1:
        name = 'Чай'
        summ = 1
        st = 40
    elif n == 2:
        name = 'Чефир'
        summ = 5
        st = 240
    elif n == 3:
        name = 'Кофе'
        summ = 10
        st = 520
    elif n == 4:
        name = 'Энергетик'
        summ = 20
        st = 1120
    elif n == 5:
        name = 'Крепкий кофе'
        summ = 40
        st = 2400
    elif n == 6:
        name = 'Настойка из вишни'
        summ = 50
        st = 3000
    elif n == 7:
        name = 'Сыворотка из плазмы'
        summ = 400
        st = 30000
    else:
        await message.answer(f'{url}, вы ввели неверный номер зелья которое хотите купить {rloser}', parse_mode='html')
        return

    if corn < st:
        await message.answer(f'{url}, у вас недостаточно зёрен для создания данного зелья {rloser}', parse_mode='html')
        return

    await message.answer(f'{url}, Wizzi_, вы успешно создали "{name}", вам начислено {summ} энергии {rloser}', parse_mode='html')
    await buy_postion_db(summ, st, id)

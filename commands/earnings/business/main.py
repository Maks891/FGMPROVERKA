from commands.earnings.business.db import *
from commands.db import register_users, getname, getonlibalance, getidname
from commands.main import geturl
from commands.main import win_luser
from commands.assets.kb import help_bsKB

async def business_list(message):
    id = message.from_user.id
    name = await getname(message)
    url = await geturl(id, name)
    await register_users(message)
    await message.answer(f'''{url}, теперь ты можешь принимать решения сам и влиять на свой бизнес.

🪓 Для начала я проведу тебе маленький инструктаж по поводу данных бизнесов, ты не можешь просто купить бизнес и начать зарабатывать на нём. Теперь вам предоставлена возможность самому влиять на доход, увеличить территорию бизнеса, закупать продукты и платить налоги в казну штата.

🏗 Для начала вам потребуется построить площадку для того чтобы возвести на ней свой бизнес. Для этого используйте команду "Построить бизнес", после этого вами будет куплена маленькая территория под бизнес.

💫 Далее вы можете при помощи команд управлять бизнесом, увеличивать его доход, покупать улучшения и прочее. Чтобы узнать все команды введите команду "Помощь" и выберите соответствующую кнопку.''', parse_mode='html')

async def my_business(message):
    id = message.from_user.id
    name = await getname(message)
    url = await geturl(id, name)
    result = await win_luser()
    rwin, rloser = result
    business, balance, nalogs, territory, bsterritory = await getbusiness(id)
    dox = 90000000 * bsterritory / 15
    balance = int(balance)
    nalogs = int(nalogs)
    dox = int(dox)
    balance = '{:,}'.format(balance).replace(',', '.')
    nalogs = '{:,}'.format(nalogs).replace(',', '.')
    territory = '{:,}'.format(territory).replace(',', '.')
    bsterritory = '{:,}'.format(bsterritory).replace(',', '.')
    dox = '{:,}'.format(dox).replace(',', '.')
    await register_users(message)
    if business == 0:
        await message.answer(f'{url}, у вас нет своего бизнеса чтобы построить введите команду "Построить бизнес" {rloser}', parse_mode='html')
    else:
        await message.answer(f'''{url}, информация о вашем бизнесе "Бизнес":
🧱 Территория: {territory} м²
🏢 Территория бизнеса: {bsterritory} м²
💸 Налоги: {nalogs}$/5.000.000$
💰 Прибыль: {balance}$
💷 Доход: {dox}$''', parse_mode='html', reply_markup=help_bsKB)

async def buy_business(message):
    id = message.from_user.id
    name = await getname(message)
    url = await geturl(id, name)
    ferm = await getbusiness(id)
    result = await win_luser()
    rwin, rloser = result
    if ferm == 1:
        await message.answer(f'{url}, у вас уже есть построенная территория под бизнес. Чтобы узнать подробнее, введите "Мой бизнес" {rloser}', parse_mode='html')
    else:
        balance = await getonlibalance(message)
        if balance < 500000000:
            await message.answer(f'{url}, у вас недостаточно денег для постройки территории бизнеса. Её стоимость 500 млн$ {rloser}', parse_mode='html')
        else:
            await buy_business_db(id)
            await message.answer(f'{url}, вы успешно построили свой бизнес для подробностей введите "Мой бизнес" {rwin}', parse_mode='html')

async def buy_territory(call):
    id = call.from_user.id
    name = await getidname(id)
    url = await geturl(id, name)
    business = await getbusiness(id)
    result = await win_luser()
    rwin, rloser = result
    if business == 0:
        await call.message.answer(f'{url}, у вас нету своего бизнеса чтобы увеличивать его территорию {rloser}', parse_mode='html')
    else:
        territory = await getterritory(id)
        ch = 22000000 * (1 + 0.15) ** (territory - 4)
        ch = int(ch)
        ch2 = '{:,}'.format(ch).replace(',', '.')
        balance = await getonlibalance(call)
        if balance < ch:
            await call.message.answer(f'{url}, у вас недостаточно денег на балансе чтобы увеличить территорию бизнеса {rloser}', parse_mode='html')
        else:
            await buy_territory_db(id, ch)
            await call.message.answer(f'{url}, вы успешно увеличили территорию бизнеса на 1 м² за {ch2}$ {rwin}', parse_mode='html')

async def buy_bsterritory(call):
    id = call.from_user.id
    name = await getidname(id)
    url = await geturl(id, name)
    business = await getbusiness(id)
    result = await win_luser()
    rwin, rloser = result
    if business == 0:
        await call.message.answer(f'{url}, у вас нет своего бизнеса чтобы увеличить бизнес {rloser}', parse_mode='html')
    else:
        territory = await getterritory(id)
        bsterritory = await getbsterritory(id)
        if territory <= bsterritory:
            await call.message.answer(f'{url}, чтобы увеличить бизнес для начала увеличьте его территорию {rloser}', parse_mode='html')
            return
        ch = 22000000 * (1 + 0.15) ** (bsterritory - 1)
        ch = int(ch)
        ch2 = '{:,}'.format(ch).replace(',', '.')
        balance = await getonlibalance(call)
        if balance < ch:
            await call.message.answer(f'{url}, у вас недостаточно денег на балансе чтобы увеличить бизнес {rloser}', parse_mode='html')
        else:
            await buy_bsterritory_db(id, ch)
            await call.message.answer(f'{url}, вы успешно увеличили бизнес на 1 м² за {ch2}$ {rwin}', parse_mode='html')

async def snyt_pribl_business(call):
    id = call.from_user.id
    name = await getidname(id)
    url = await geturl(id, name)
    business = await getbusiness(id)
    result = await win_luser()
    rwin, rloser = result
    if business == 0:
        await call.message.answer(f'{url}, у вас нет своего бизнеса чтобы собирать с него приыбль {rloser}', parse_mode='html')
    else:
        balance = await get_business_balance(id)
        balance2 = '{:,}'.format(balance).replace(',', '.')
        if balance == 0:
            await call.message.answer(f'{url}, на данный момент на балансе вашего бизнеса нет прибыли {rloser}', parse_mode='html')
        else:
            await snyt_pribl_bs_db(id, balance)
            await call.message.answer(f'{url}, вы успешно сняли {balance2}$ с баланса вашего бизнеса {rwin}', parse_mode='html')

async def oplata_nalogov_business(call):
    id = call.from_user.id
    name = await getidname(id)
    url = await geturl(id, name)
    business = await getbusiness(id)
    result = await win_luser()
    rwin, rloser = result
    if business == 0:
        await call.message.answer(f'{url}, у вас нет своего бизнеса чтобы платить за него налоги {rloser}', parse_mode='html')
    else:
        nalogs = await get_business_nalogs(id)
        nalogs2 = '{:,}'.format(nalogs).replace(',', '.')
        balance = await getonlibalance(call)
        if balance < nalogs:
            await call.message.answer(f'{url}, у вас недостаточно денег чтоб оплатить налоги {rloser}', parse_mode='html')
            return
        if nalogs == 0:
            await call.message.answer(f'{url}, у вас нет налогов чтобы их оплатить {rwin}', parse_mode='html')
        else:
            await oplata_nalogs_bs_db(id, nalogs)
            await call.message.answer(f'{url}, вы успешно оплатили налоги на сумму {nalogs2}$ с вашего игрового баланса {rwin}', parse_mode='html')

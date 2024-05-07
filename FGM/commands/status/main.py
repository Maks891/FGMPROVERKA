from commands.db import register_users, getname, getstatus
from commands.main import geturl
from commands.status.db import *

async def status_list(message):
    await register_users(message)
    name = await getname(message)
    await message.answer(f'''{name}, доступные статусы в игре:

1️⃣ Standart VIP:
- Повышенный процент в банке
- Увеличенный шанс победы в играх
- Увеличен процент в депозите до 8%
- Уменьшен налог при снятии депозита до 4.5%
- Увеличен лимит передачи другим игрокам до 300.000.000.000.000$ в сутки
- Красивая отметка в профиле
- Возможность установить более длинный ник
- Время до получения ежедневного бонуса уменьшено в два раза
- Увеличена максимальная энергия до 25
- Увеличено количество открываемых кейсов до 20

2️⃣ Gold VIP:
- Увеличен шанс в играх
- Увеличен процент в депозите до 10%
- Уменьшен налог при снятии депозита до 3.5%
- Возможность установить ещё длинее ник
- Уникальный золотой ежедневный бонус
- Увеличен лимит передачи другим игрокам до 750.000.000.000.000$ в сутки
- Увеличена максимальная энергия до 50
- Увеличено количество открываемых кейсов до 40

3️⃣ Platinum VIP:
- Увеличен лимит передачи другим игрокам до 1.000.000.000.000.000$ в сутки
- Повышенный процент выигрыша в играх
- Увеличен процент в депозите до 12%
- Уменьшен налог при снятии депозита до 3%
- Увеличена максимальная энергия до 75
- Красивая отметка в профиле
- Опыт и добыча увеличена в два раза
- Увеличено количество открываемых кейсов до 60

4️⃣ Администратор:
- Выдача денег в сутки - 150.000.000.000.000
- Увеличен процент в депозите до 15%
- Уменьшен налог при снятии депозита до 2.5%
- Возможность просматривать профили других игроков
- Максимальная энергия увеличенная до 100
- Красивая отметка в профиле
- Увеличен лимит передачи другим игрокам до 30.000.000.000.000.000$ в сутки
- Увеличено количество открываемых кейсов до 250''', parse_mode='html')


async def donat_list(message):
    await register_users(message)
    name = await getname(message)
    user_id = message.from_user.id
    url = await geturl(user_id, name)
    ecoins = await getecoins(user_id)
    await message.answer(f'''{url}, наш магазин:

💵 Текущий курс: 1 RUB = 1 B-Coin
💸 Валюта: 1 B-Coin можно обменять на 1.000.000.000.000$

🪙 Обмен коинов на валюту: Обменять [количество]

🏆 Привилегии:
1️⃣ Standart VIP | 250 B-Coin
2️⃣ Gold VIP | 500 B-Coin
3️⃣ Platinum VIP | 750 B-Coin
4️⃣ Admin Status | 1.500 B-Coin

🔝Покупка: Купить привилегию [номер]

⚡ Энергия:
    - 20 энергии | 15 B-Coin 
     🔝 Покупка: Купить флягу 1
    - 60 энергии | 35 B-Coin
     🔝 Покупка: Купить флягу 2

🚧 Лимит:
 - 75.000.000.000.000 | 100 B-Coin
🔝 Покупка: Купить лимит 1

💰Ваш баланс: {ecoins} B-Coin
📲 Пополнить баланс: нельзя''', parse_mode='html')


async def my_status(message):
    await register_users(message)
    name = await getname(message)
    user_id = message.from_user.id
    url = await geturl(user_id, name)
    status = await getstatus(user_id)
    if status == 0:
        await message.answer(f'{url}, к сожалению вы не владеете какими либо привилегиями. Подробнее - Донат',
                             parse_mode='html')
    elif status == 1:
        await message.answer(f'''{url}, информация о привилегии:

🏆 Статус: Standart VIP
🏦 Процент вклада: 8%
💸 Лимит передачи: 300.000.000.000.000$/сутки

Подробнее об плюшках можно узнать введя команду "Статусы"''',
                             parse_mode='html')

    elif status == 2:
        await message.answer(f'''{url}, информация о привилегии:

🏆 Статус: Gold VIP
🏦 Процент вклада: 10%
💸 Лимит передачи: 750.000.000.000.000$/сутки

Подробнее об плюшках можно узнать введя команду "Статусы"''',
                             parse_mode='html')

    elif status == 3:
        await message.answer(f'''{url}, информация о привилегии:

🏆 Статус: Platinum VIP
🏦 Процент вклада: 12%
💸 Лимит передачи: 1.000.000.000.000.000$/сутки

Подробнее об плюшках можно узнать введя команду "Статусы"''',
                             parse_mode='html')

    elif status == 4:
        await message.answer(f'''{url}, информация о привилегии:

🏆 Статус: Администратор
🏦 Процент вклада: 15%
💸 Лимит передачи: 30.000.000.000.000.000$/сутки

Подробнее об плюшках можно узнать введя команду "Статусы"''',
                             parse_mode='html')

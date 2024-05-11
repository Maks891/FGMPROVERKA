from commands.db import getname, getstatus
from commands.main import geturl
from commands.status.db import *
import config as cfg


async def status_list(message):
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
📲 Пополнить баланс: {cfg.admin_username}''', parse_mode='html')


async def my_status(message):
    name = await getname(message)
    user_id = message.from_user.id
    url = await geturl(user_id, name)
    status = await getstatus(user_id)
    privileges = {
        0: "к сожалению вы не владеете какими либо привилегиями",
        1: "🏆 Статус: Standart VIP\n🏦 Процент вклада: 8%\n💸 Лимит передачи: 300.000.000.000.000$/сутки",
        2: "🏆 Статус: Gold VIP\n🏦 Процент вклада: 10%\n💸 Лимит передачи: 750.000.000.000.000$/сутки",
        3: "🏆 Статус: Platinum VIP\n🏦 Процент вклада: 12%\n💸 Лимит передачи: 1.000.000.000.000.000$/сутки",
        4: "🏆 Статус: Администратор\n🏦 Процент вклада: 15%\n💸 Лимит передачи: 30.000.000.000.000.000$/сутки"
    }

    await message.answer(f'{url}, информация о привилегии:\n{privileges[status]}\nПодробнее об плюшках можно узнать введя команду "Статусы"', parse_mode='html')

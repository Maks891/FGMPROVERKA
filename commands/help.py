from aiogram import types
from assets.antispam import antispam
from commands.db import getinlinename
import commands.assets.kb as kb
import config as cfg
from bot import bot, dp
from datetime import datetime, timedelta


help_msg = {}


def antispam_help(func):
    async def wrapper(call: types.CallbackQuery):
        chat_id = call.message.chat.id
        msg_id = call.message.message_id

        data = help_msg.get(chat_id, 'no')
        dt = int(datetime.now().timestamp())

        if data != 'no':
            if int(data[0]) == int(msg_id):
                if int(dt - 120) < int(data[1]):
                    if (int(dt) - int(data[1])) > 2:
                        help_msg[chat_id] = (msg_id, dt)
                        await func(call)
                    else:
                        await bot.answer_callback_query(call.id, text='⏳ Не так быстро! (2 сек)')
                    return

        try: await bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except: pass

    return wrapper


@antispam
async def help_cmd(message):
    dt = int(datetime.now().timestamp())
    mid = message.message_id + 1
    help_msg[message.chat.id] = (mid, (dt - 2))

    await message.answer(f'''Игрок, выберите категорию:
   1️⃣ Основное
   2️⃣ Игры
   3️⃣ Развлекательное
   4️⃣ Кланы

💬 Так же у нас есть общая беседа №1 и общая беседа №2
🆘 По всем вопросам - {cfg.admin_username}''', reply_markup=kb.help_menu())


@antispam_help
async def help_back(call):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
Игрок, выберите категорию:
   1️⃣ Основное
   2️⃣ Игры
   3️⃣ Развлекательное
   4️⃣ Кланы

💬 Так же у нас есть общая беседа №1 и общая беседа №2
🆘 По всем вопросам - {cfg.admin_username}''', reply_markup=kb.help_menu())


@antispam_help
async def help_osn(call):
    name = await getinlinename(call)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
{name}, основные команды:
💡 Разное:
   📒 Профиль
   💫 Мой лимит
   👑 Рейтинг
   👑 Продать рейтинг
   ⚡ Энергия
   ⛏ Шахта
   🚗 Машины
   📱 Телефоны
   ✈ Самолёты
   🛥 Яхты
   🚁 Вертолёты
   🏠 Дома
   💸 Б/Баланс
   📦 Инвентарь
   📊 Курс руды
   🏢 Ограбить мэрию
   💰 Банк [положить/снять] [сумма/всё]
   💵 Депозит [положить/снять] [сумма/всё]
   🤝 Дать [сумма]
   🌐 Биткоин курс/купить/продать [кол-во]
   ⚱ Биткоины
   💈 Ежедневный бонус
   💷 Казна
   💢 Сменить ник [новый ник]
   👨 Мой ник - узнать ник
   ⚖ РП Команды - узнать РП команды
   🏆 Мой статус
   🔱 Статусы️
   💭 !Беседа - беседа бота''', reply_markup=kb.help_back())


@antispam_help
async def help_game(call):
    name = await getinlinename(call)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
{name}, игровые команды:
🚀 Игры:
   🎮 Спин [ставка]
   🎲 Кубик [число] [ставка]
   🏀 Баскетбол [ставка]
   🎯 Дартс [ставка]
   ⚽️ Футбол [ставка]
   🎳️ Боулинг [ставка]
   📉 Трейд [вверх/вниз] [ставка]
   🎰 Казино [ставка]''', reply_markup=kb.help_back())


@antispam_help
async def help_rz(call):
    name = await getinlinename(call)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''
{name}, развлекательные команды:
   🔮 Шар [фраза]
   💬 Выбери [фраза] или [фраза2]
   📊 Инфа [фраза]

💒 Браки:
   💖 Свадьба [ID пользователя]
   💖 Развод
   💌 Мой брак

📦 Кейсы:
   🛒 Купить кейс [номер] [количество]
   🔐 Открыть кейс [номер] [количество]

🗄 Бизнес:
   💰 Мой бизнес/бизнес
   💸 Продать бизнес (временно недоступно)

🏭Генератор
   🏭 Мой генератор/генератор
   💷 Продать генератор (временно недоступно)

🧰 Майнинг ферма:
   🔋 Моя ферма/ферма
   💰 Продать ферму (временно недоступно)

⚠️ Карьер:
   🏗 Мой карьер/карьер
   💰 Продать карьер (временно недоступно)

🌳 Сады:
   🪧 Мой сад/сад
   💰 Продать сад (временно недоступно)
   💦 Сад полить
   🍸 Зелья
   🔮 Создать зелье [номер]''', reply_markup=kb.help_back())





@dp.callback_query_handler(lambda c: c.data == 'help_back')
async def help_back_s(callback_query: types.CallbackQuery):
    await help_back(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'help_osn')
async def help_osn_s(callback_query: types.CallbackQuery):
    await help_osn(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'help_game')
async def help_game_s(callback_query: types.CallbackQuery):
    await help_game(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'help_rz')
async def help_rz_s(callback_query: types.CallbackQuery):
    await help_rz(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'help_clans')
async def help_clans_s(callback_query: types.CallbackQuery):
    await help_clans(callback_query)

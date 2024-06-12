import sys
from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from commands.db import url_name, getstatus, get_name
from commands.admin.admin_db import *
from commands.main import geturl
from commands.main import win_luser
import config as cfg
from commands.admin.loger import new_log
from bot import bot

from assets.antispam import earning_msg
from assets.gettime import bonus_time, kazna_time
from commands.help import help_msg


class new_ads_state(StatesGroup):
    txt = State()


async def give_money(message):
    user_id = message.from_user.id
    status = await getstatus(user_id)
    if user_id not in [6888643375, 1688468160] and status == 0:
        return await message.answer('👮‍♂️ Вы не являетесь администратором бота чтобы использовать данную команду.\nДля покупки введи команду "Донат"')

    user_name = await get_name(user_id)
    rwin, rloser = await win_luser()
    url = await geturl(user_id, user_name)

    try:
        r_user_id = message.reply_to_message.from_user.id
        r_user_name = await get_name(r_user_id)
        r_url = await geturl(r_user_id, r_user_name)
    except:
        return await message.answer(f'{url}, чтобы выдать деньги нужно ответить на сообщение пользователя {rloser}')

    try:
        su = message.text.split()[1]
        su = (su).replace('к', '000').replace('м', '000000').replace('.', '')
        summ = int(su)
        summ2 = '{:,}'.format(summ).replace(',', '.')
    except:
        return await message.answer(f'{url}, вы не ввели сумму которую хотите выдать {rloser}')

    if user_id in [6888643375, 1688468160]:
        await give_money_db(user_id, r_user_id, summ, 'rab')
        await message.answer(f'{url}, вы выдали {summ2}$ пользователю {r_url}  {rwin}')
    else:
        res = await give_money_db(user_id, r_user_id, summ, 'adm')
        if res == 'limit':
            return await message.answer(f'{url}, вы достигли лимита на выдачу денег  {rloser}')

        await message.answer(f'{url}, вы выдали {summ2}$ пользователю {r_url}  {rwin}')
    await new_log(f'#выдача\nПользователь {user_name} ({user_id})\nСумма: {summ2}$\nПользователю {r_user_name} ({r_user_id})', 'issuance_money')


async def give_bcoins(message):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    user_name = await get_name(user_id)
    rwin, rloser = await win_luser()
    url = await geturl(user_id, user_name)

    try:
        r_user_id = message.reply_to_message.from_user.id
        r_user_name = await get_name(r_user_id)
        r_url = await geturl(r_user_id, r_user_name)
    except:
        return await message.answer(f'{url}, чтобы выдать деньги нужно ответить на сообщение пользователя {rloser}')

    try:
        su = message.text.split()[1]
        su = (su).replace('к', '000').replace('м', '000000').replace('.', '')
        summ = int(su)
        summ2 = '{:,}'.format(summ).replace(',', '.')
    except:
        return await message.answer(f'{url}, вы не ввели сумму которую хотите выдать {rloser}')

    await give_bcoins_db(r_user_id, summ)
    await message.answer(f'{url}, вы выдали {summ2}💳 пользователю {r_url}  {rwin}')
    await new_log(f'#бкоин-выдача\nАдмин {user_name} ({user_id})\nСумма: {summ2}$\nПользователю {r_user_name} ({r_user_id})', 'issuance_bcoins')


async def obnyl_cmd(message: types.Message):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        await message.answer("У вас нет доступа к данной команде")
        return
    
    user_name = await get_name(user_id)
    r_user_id = message.reply_to_message.from_user.id
    r_user_name = await get_name(r_user_id)
    r_url = await geturl(r_user_id, r_user_name)
    rwin, rloser = await win_luser()
    url = await geturl(user_id, user_name)


    
    await message.answer(f'{url}, вы обнулили пользователя {r_user_name} {rwin}')
    await new_log(f'#обнуление\nАдмин {user_name} ({user_id})\nОбнулил баланс пользователю {r_user_name} ({r_user_id})', 'issuance_obnyl')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET btc = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET timedepozit = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET exp = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET case1 = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET case2 = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET case3 = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET case4 = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET games = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET status = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET yen = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET perlimit = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    cursor.execute(f'UPDATE users SET ecoins = {0} WHERE user_id = "{r_user_id}"')
    conn.commit()




async def new_ads(message, state: FSMContext, type=0):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    if type == 0:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("Отмена"))
        await message.answer("⚙️ Введите новый текст рекламы ('-' чтобы удалить)\n\n<i>Вы можете использовать HTML-теги для форматирования текста.</i>", reply_markup=keyboard)
        await new_ads_state.txt.set()
        return

    txt = message.text
    if txt == 'Отмена':
        await state.finish()
        await admin_menu(message)
        return

    txt = '' if txt == '-' else txt
    try:
        ads = txt.replace(r'\n', '\n')
        msg = '⚙️ Реклама в сообщениях удалена' if txt == '' else '⚙️ Установлен новый текст рекламы:\n\n' + ads
        await message.answer(msg, disable_web_page_preview=True)
        await upd_ads(txt)
    except:
        await message.answer('❌ Ошибка в разметке HTML')

    await state.finish()
    await admin_menu(message)


async def unloading(message):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    if message.chat.type != 'private':
        return

    time = datetime.now().strftime("%Y-%m-%d в %H:%M:%S")
    with open('users.db', 'rb') as file:
        await bot.send_document(message.chat.id, file, caption=f'🛡 Копия бд создана <blockquote>{time}</blockquote>')


async def admin_menu(message: types.Message):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='📍 Рассылка'), types.KeyboardButton(text='🕹 Управление')],
            [types.KeyboardButton(text='✨ Промокоды'), types.KeyboardButton(text='📥 Выгрузка')],
            [types.KeyboardButton(text='🎪 Мероприятия'), types.KeyboardButton(text='⚙️ Изменить текст рекламы')]
        ],
        resize_keyboard=True
    )

    await message.answer('<b>👮‍♂️ Админ меню:</b>', reply_markup=keyboard)


async def control(message: types.Message):
    print(546546)
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🛡 Пользователи"), types.KeyboardButton("💽 ОЗУ"))
    keyboard.add(types.KeyboardButton("👮 Вернуться в админ меню"))

    await message.answer('<b>🕹️ Меню управления:</b>', reply_markup=keyboard)


def sizeof_fmt(num):
    for unit in ['Б', 'КБ', 'МБ']:
        if abs(num) < 1024.0:
            return "%3.1f %s" % (num, unit)
        num /= 1024.0
    return "%.1f %s" % (num, 'ТБ')


async def RAM_control(message: types.Message):
    user_id = message.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🗑 Очистить все", callback_data="ram-clear"))

    earning = sizeof_fmt(sys.getsizeof(earning_msg))
    help_menu = sizeof_fmt(sys.getsizeof(help_msg))
    bonus = sizeof_fmt(sys.getsizeof(bonus_time))
    kazna = sizeof_fmt(sys.getsizeof(kazna_time))

    await message.answer(f'''💽 Информация о использовании ОЗУ:
💸 Заработок: {earning}
🆘 Помощь: {help_menu}
🎁 Бонусы: {bonus}
💰 Казна: {kazna}''', reply_markup=keyboard)


async def RAM_clear(call: types.CallbackQuery):
    user_id = call.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return

    global earning_msg, help_msg, bonus_time, kazna_time
    earning_msg.clear()
    help_msg.clear()
    bonus_time.clear()
    kazna_time.clear()

    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='🗑 Очищено!')

async def mpadmin(call: types.CallbackQuery):
    user_id = call.from_iser.id
    if user_id not in [6888643375, 1688468160]:
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Правила проведения мероприятий"), types.KeyboardButton("Информация о проведении"))

    await message.answer('<b>Меню мероприятий для игроков:</b>', reply_markup=keyboard)

async def mppravila(call: types.CallbackQuery):
    user_id = call.from_user.id
    if user_id not in [6888643375, 1688468160]:
        return
        
        await message.answer('Правила мероприятий')


def reg(dp: Dispatcher):
    dp.register_message_handler(admin_menu, commands='adm')
    dp.register_message_handler(give_money, lambda message: message.text.lower().startswith('выдать'))
    dp.register_message_handler(obnyl_cmd, lambda message: message.text.lower().startswith('обнулить'))
    dp.register_message_handler(give_bcoins, lambda message: message.text.lower().startswith('бдать'))
    dp.register_message_handler(unloading, lambda message: message.text.lower().startswith('📥 Выгрузка'))
    dp.register_message_handler(mpadmin, lambda message: message.text.lower().startswith('🎪 Мероприятия'))
    dp.register_message_handler(control, lambda message: message.text == '🕹 Управление')
    dp.register_message_handler(RAM_control, lambda message: message.text == '💽 ОЗУ')
    dp.register_message_handler(mppravila, lambda message: message.text == 'Правила проведения мероприятий')
    dp.register_callback_query_handler(RAM_clear, text='ram-clear')
    dp.register_message_handler(new_ads, lambda message: message.text == '⚙️ Изменить текст рекламы')
    dp.register_message_handler(lambda message, state: new_ads(message, state, type=1), state=new_ads_state.txt)

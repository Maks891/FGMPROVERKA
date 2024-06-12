import sqlite3
from aiogram import types
from aiogram.dispatcher import Dispatcher
from commands.db import conn, cursor  # Импорт основной бд

print('!!! СОЗДАН ПРОМОКОД "непромо start". Для удаление промокода удалите файл ptomo.py из папки modules.')

conn2 = sqlite3.connect('promo.db')
cursor2 = conn2.cursor()

cursor2.execute('''
CREATE TABLE IF NOT EXISTS promo (
    id INTEGER
);
''')
conn2.commit()


async def getname(user_id):
    cursor.execute("SELECT name FROM users WHERE user_id=?", (int(user_id),))
    name = cursor.fetchone()[0]
    return name


async def promo_start(message: types.Message):
    user_id = message.from_user.id
    username = await getname(user_id)

    cursor2.execute('SELECT id FROM promo WHERE id = ?', (user_id,))
    result = cursor2.fetchone()

    if result:
        await message.reply(f'😞 <b>{username}</b>, вы уже активировали промокод.', parse_mode='html')
    else:
        cursor.execute("UPDATE users SET ecoins = ecoins + 250 WHERE user_id = ?", (user_id,))
        conn.commit()

        cursor2.execute('INSERT INTO promo (id) VALUES (?)', (user_id,))
        conn2.commit()

        await message.reply(f'🎁 <b>{username}</b>, вы получили:\n250 B-coins', parse_mode='html')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(promo_start, lambda message: message.text.lower().startswith('непромо start'))

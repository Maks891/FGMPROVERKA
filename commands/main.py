from commands.db import register_users, getname
from commands.assets.kb import startKB
import random

async def on_start(message):
    await register_users(message)
    sticker_id = 'CAACAgQAAxkBAAEKs6JlSQUtGTtSzXGVcJGBe0PwnWkI9QACRwkAAm0NeFIe5FE9nk15XTME'
    await message.answer_sticker(sticker=sticker_id)

    await message.answer('''🤖 Добро пожаловать на борт, Кто-то! Меня зовут BFG, твой верный игровой бот.

🎮 У меня есть множество интересных команд и игр, чтобы скрасить твоё время, будь ты один или в компании друзей! (Кстати, вместе всегда веселее) 💙
🔍 Познакомиться со всеми моими возможностями ты можешь, введя команду «помощь».

<a href="https://t.me/+_TipRhtinIcyZDg6">🔈 Наш канал</a>
<a href="https://t.me/+BpEAdjRMNQIzODYy">💬 Наш чат</a>''', parse_mode='html', disable_web_page_preview=True, reply_markup=startKB)

    await message.answer('''🚀 Не уверен, с чего начать своё приключение?
Присоединяйся к нашему официальному чату BFG: <a href="https://t.me/+BpEAdjRMNQIzODYy">t.me/bforgame_chat</a>''', parse_mode='html', disable_web_page_preview=True)

async def chat_list(message):
    await register_users(message)
    await message.answer('''💭 Официальная первая беседа бота:
@bforgame_chat
💭 Официальная вторая беседа бота:
@bforgame_chat_two
💭 Официальный канал разработки:
@bforgame_dev
🏆 Официальный чат с розыгрышами:
@bforgame_events''', parse_mode='html', disable_web_page_preview=True)

async def myname_cmd(message):
    await register_users(message)
    name = await getname(message)
    await message.answer(f'🗂 Ваш ник - «{name}»')

async def win_luser():
    win = ['🙂', '😋', '😄', '🤑', '😃']
    rwin = random.choice(win)
    loser = ['😔', '😕', '😣', '😞', '😢']
    rloser = random.choice(loser)
    return rwin, rloser

async def geturl(id, txt):
    url = f'<a href="tg://user?id={id}">{txt}</a>'
    return url

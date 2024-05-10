from commands.db import register_users, getname
from commands.assets.kb import startKB
import random

async def on_start(message):
    await register_users(message)

    await message.answer('''🤖 Добро пожаловать на борт, Кто-то! Меня зовут FGM.

🎮 У меня есть множество интересных команд и игр, чтобы скрасить твоё время, будь ты один или в компании друзей! (Кстати, вместе всегда веселее) 💙
🔍 Познакомиться со всеми моими возможностями ты можешь, введя команду «помощь».

''', parse_mode='html', disable_web_page_preview=True, reply_markup=startKB)

    await message.answer('''🚀 Не уверен, с чего начать своё приключение?
Присоединяйся к нашему официальному чату FGM''', parse_mode='html', disable_web_page_preview=True)

async def chat_list(message):
    await register_users(message)
    await message.answer('''💭 Официальная первая беседа бота:
@FGMoficial
💭 Официальная вторая беседа бота:
@
💭 Официальный канал разработки:
@
🏆 Официальный чат с розыгрышами:
@''', parse_mode='html', disable_web_page_preview=True)

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

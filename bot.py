from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot("7092521991:AAG18Ty2cie-czUSvfhQmyWo9sZmIpHtYos", parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

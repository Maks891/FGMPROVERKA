from aiogram import Bot, Dispatcher
from datetime import datetime, timedelta
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as cfg


bot = Bot(cfg.API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

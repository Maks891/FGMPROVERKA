from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

# Количество кликов для улучшения уровня
LEVEL_UP_CLICKS = 10

# Счетчик кликов и уровень игрока
player_data = {}

async def click_cmd(message: types.Message):
    # Инициализация данных игрока, если они еще не существуют
    if message.from_user.id not in player_data:
        player_data[message.from_user.id] = {'clicks': 0, 'level': 1}

    # Переход в состояние ожидания клика
    await ClickerGame.waiting_for_click.set()
    await message.answer("Начни игру! Нажми на кнопку, чтобы кликнуть.")

async def on_click(update: types.Update, context: FSMContext):
    # Получение текущего количества кликов и уровня
    user_id = update.effective_user.id
    clicks, level = player_data[user_id]['clicks'], player_data[user_id]['level']

    # Увеличение количества кликов
    player_data[user_id]['clicks'] += 1

    # Проверка, достаточно ли кликов для улучшения уровня
    if clicks % LEVEL_UP_CLICKS == 0:
        player_data[user_id]['level'] += 1
        await update.message.answer(f"Уровень улучшен! Теперь ты на уровне {level}.")

    # Отправка сообщения с текущим количеством кликов
    await update.message.answer(f"Клики: {clicks}")

async def reset_game(message: types.Message):
    # Сброс данных игрока
    player_data[message.from_user.id] = {'clicks': 0, 'level': 1}
    await message.answer("Игра сброшена. Начни заново!")

# Определение клавиатуры с кнопкой для клика
click_button = InlineKeyboardButton("Кликнуть", callback_data="click")
click_button2 = InlineKeyboardButton("Мой уровень", callback_data="level")
start_keyboard = InlineKeyboardMarkup().add(click_button, click_button2)

# Обработчики команд
dp.register_message_handler(start_game, commands=['start'])
dp.register_message_handler(reset_game, commands=['reset'])

# Обработчик нажатия на кнопку
dp.register_callback_query_handler(on_click, text="click")

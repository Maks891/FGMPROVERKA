# YT: userbotik
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from commands.main import *
from commands.help import *
from commands.balance import *
from commands.status.main import *
from commands.rz import *
from commands.peredat import *
from commands.games.games import *
from commands.assets.auto import automatisation
from commands.ore.btcs import *
from commands.earnings.business.main import *
from commands.ore.dig import *
from commands.ore.sell import *
from commands.ore.rating import *
from commands.case.main import *
from commands.case.buy import *
from commands.bank.main import *
from commands.earnings.garden.main import *
from commands.earnings.garden.potions import *
from commands.earnings.farm.main import *
from commands.earnings.generator.main import *


bot = Bot(token="6542734064:AAGYEBv8My1nSOiJK3CY85J3U3qjP3gDIag")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def on_start_s(message: types.Message):
    await on_start(message)


@dp.message_handler(lambda message: message.text in ['помощь', 'Помощь', '/help'])
async def help_cmd_s(message: types.Message):
    await help_cmd(message)


@dp.message_handler(lambda message: message.text in ['топ', 'Топ'])
async def top_command_s(message: types.Message):
    await top_command(message)


@dp.message_handler(lambda message: message.text in ['казна', 'Казна'])
async def kazna_cmd_s(message: types.Message):
    await kazna_cmd(message)


@dp.message_handler(lambda message: message.text in ['статистика бота', 'Статистика бота'])
async def stats_cmd_s(message: types.Message):
    await stats_cmd(message)


@dp.message_handler(lambda message: message.text in ['б', 'Б', 'Баланс', 'баланс'])
async def balance_cmd_s(message: types.Message):
    await balance_cmd(message)


@dp.message_handler(lambda message: message.text in ['биткоины', 'Биткоины'])
async def btc_cmd_s(message: types.Message):
    await btc_cmd(message)


@dp.message_handler(lambda message: message.text in ['энергия', 'Энергия'])
async def energy_cmd_s(message: types.Message):
    await energy_cmd(message)


@dp.message_handler(lambda message: message.text in ['рейтинг', 'Рейтинг'])
async def rrating_cmd_s(message: types.Message):
    await rrating_cmd(message)


@dp.message_handler(lambda message: message.text in ['!Беседа', '!беседа'])
async def chat_list_s(message: types.Message):
    await chat_list(message)


@dp.message_handler(lambda message: message.text in ['донат', 'Донат'])
async def donat_list_s(message: types.Message):
    await donat_list(message)


@dp.message_handler(lambda message: message.text in ['статусы', 'Статусы'])
async def status_list_s(message: types.Message):
    await status_list(message)

@dp.message_handler(lambda message: message.text in ['Выдать', 'выдать'])
async def vidat_cmd_s(message: types.Message):
    await vidat_cmd(message)


@dp.message_handler(lambda message: message.text in ['мой статус', 'Мой статус'])
async def my_status_s(message: types.Message):
    await my_status(message)


@dp.message_handler(lambda message: message.text in ['банк', 'Банк'])
async def bank_cmd_s(message: types.Message):
    await bank_cmd(message)


@dp.message_handler(lambda message: message.text in ['мой лимит', 'Мой лимит'])
async def limit_cmd_s(message: types.Message):
    await limit_cmd(message)


@dp.message_handler(lambda message: message.text in ['профиль', 'Профиль'])
async def profil_cmd_s(message: types.Message):
    await profil_cmd(message)


@dp.message_handler(lambda message: message.text in ['мой ник', 'Мой ник'])
async def myname_cmd_s(message: types.Message):
    await myname_cmd(message)


@dp.message_handler(lambda message: message.text in ['Моя ферма', 'моя ферма'])
async def my_ferma_s(message: types.Message):
    await my_ferma(message)


@dp.message_handler(lambda message: message.text in ['фермы', 'Фермы', 'ферма', 'Ферма'])
async def ferma_list_s(message: types.Message):
    await ferma_list(message)


@dp.message_handler(lambda message: message.text in ['генератор', 'Генератор', 'Генераторы', 'генераторы'])
async def generator_list_s(message: types.Message):
    await generator_list(message)


@dp.message_handler(lambda message: message.text in ['мой генератор', 'Мой генератор'])
async def my_generator_s(message: types.Message):
    await my_generator(message)


@dp.message_handler(lambda message: message.text in ['построить генератор', 'Построить генератор'])
async def buy_turbine_s(message: types.Message):
    await buy_turbine(message)


@dp.message_handler(lambda message: message.text in ['зелья', 'Зелья'])
async def potions_list_s(message: types.Message):
    await potions_list(message)


@dp.message_handler(lambda message: message.text in ['сад', 'Сад'])
async def harden_list_s(message: types.Message):
    await harden_list(message)


@dp.message_handler(lambda message: message.text in ['Мой сад', 'мой сад'])
async def my_garden_s(message: types.Message):
    await my_garden(message)


@dp.message_handler(lambda message: message.text in ['Сад полить', 'сад полить'])
async def garden_polit_s(message: types.Message):
    await polit_dereva_garden_2(message)


@dp.message_handler(lambda message: message.text in ['Построить сад', 'построить сад'])
async def buy_garden_s(message: types.Message):
    await buy_garden(message)


@dp.message_handler(lambda message: message.text in ['бизнес', 'Бизнес', 'бизнесы', 'Бизнесы'])
async def business_list_s(message: types.Message):
    await business_list(message)


@dp.message_handler(lambda message: message.text in ['Мой бизнес', 'мой бизнес'])
async def my_business_s(message: types.Message):
    await my_business(message)


@dp.message_handler(lambda message: message.text in ['Построить ферму', 'построить ферму'])
async def buy_ferma_s(message: types.Message):
    await buy_ferma(message)


@dp.message_handler(lambda message: message.text in ['Построить бизнес', 'построить бизнес'])
async def buy_business_s(message: types.Message):
    await buy_business(message)


@dp.message_handler(lambda message: message.text.lower().startswith('банк положить'))
async def putbank_s(message: types.Message):
    await putbank(message)


@dp.message_handler(lambda message: message.text.lower().startswith('банк снять'))
async def takeoffbank_s(message: types.Message):
    await takeoffbank(message)


@dp.message_handler(lambda message: message.text.lower().startswith('депозит положить'))
async def pudepozit_s(message: types.Message):
    await pudepozit(message)


@dp.message_handler(lambda message: message.text.lower().startswith('депозит снять'))
async def takeoffdepozit_s(message: types.Message):
    await takeoffdepozit(message)


@dp.message_handler(lambda message: message.text.lower().startswith('ограбить мэрию') or message.text.lower().startswith('ограбить казну'))
async def ogr_kazna_s(message: types.Message):
    await ogr_kazna(message)


@dp.message_handler(lambda message: message.text.lower().startswith('продать рейтинг'))
async def sellrating_s(message: types.Message):
    await sellrating(message)


@dp.message_handler(lambda message: message.text.lower().startswith('продать биткоин') or message.text.lower().startswith('биткоин продать'))
async def sellbtc_s(message: types.Message):
    await sellbtc(message)


@dp.message_handler(lambda message: message.text.lower().startswith('купить биткоин') or message.text.lower().startswith('биткоин купить'))
async def buybtc_s(message: types.Message):
    await buybtc(message)


@dp.message_handler(lambda message: message.text.lower().startswith('курс биткоин') or message.text.lower().startswith('биткоин курс'))
async def btc_kurs_s(message: types.Message):
    await btc_kurs(message)


@dp.message_handler(lambda message: message.text in ['курс руды', 'Курс руды'])
async def kursrud_cmd_s(message: types.Message):
    await kursrud_cmd(message)


@dp.message_handler(lambda message: message.text in ['кейсы', 'Кейсы'])
async def getcase_cmd_s(message: types.Message):
    await getcase_cmd(message)


@dp.message_handler(lambda message: message.text.lower().startswith('открыть кейс'))
async def open_case_s(message: types.Message):
    await open_case(message)


@dp.message_handler(lambda message: message.text.lower().startswith('купить кейс'))
async def buy_case_s(message: types.Message):
    await buy_case(message)


@dp.message_handler(lambda message: message.text in ['Ежедневный бонус', 'ежедневный бонус'])
async def bonus_cmd_s(message: types.Message):
    await bonus_cmd(message)


@dp.message_handler(lambda message: message.text in ['Моя шахта', 'моя шахта'])
async def mymine_cmd_s(message: types.Message):
    await mymine_cmd(message)


@dp.message_handler(lambda message: message.text in ['шахта', 'Шахта'])
async def mine_cmd_s(message: types.Message):
    await mine_cmd(message)


@dp.message_handler(lambda message: message.text.lower().startswith('копать'))
async def digmine_s(message: types.Message):
    await digmine(message)


@dp.message_handler(lambda message: message.text.lower().startswith('продать'))
async def sellruda_cmd_s(message: types.Message):
    await sellruda_cmd(message)


@dp.message_handler(lambda message: message.text in ['инвентарь', 'Инвентарь'])
async def inventary_cmd_s(message: types.Message):
    await inventary_cmd(message)


@dp.message_handler(lambda message: message.text in ['курс руды', 'Курс руды'])
async def kursrud_cmd_s(message: types.Message):
    await kursrud_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("шар ") or message.text.startswith("Шар "))
async def shar_cmd_s(message: types.Message):
    await shar_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("сменить ник") or message.text.startswith("Сменить ник"))
async def setname_cmd_s(message: types.Message):
    await setname_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("дать") or message.text.startswith("Дать"))
async def dat_cmd_s(message: types.Message):
    await dat_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("дартс") or message.text.startswith("Дартс"))
async def darts_cmd_s(message: types.Message):
    await darts_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("кубик") or message.text.startswith("Кубик"))
async def kybik_game_cmd_s(message: types.Message):
    await kybik_game_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("баскетбол") or message.text.startswith("Баскетбол"))
async def basketbol_cmd_s(message: types.Message):
    await basketbol_cmd(message)


@dp.message_handler(lambda message: message.text.startswith("боулинг") or message.text.startswith("Боулинг"))
async def bowling_cmd_s(message: types.Message):
    await bowling_cmd(message)


@dp.callback_query_handler(lambda c: c.data == 'garden_sobrat')
async def snyt_pribl_garden_s(callback_query: types.CallbackQuery):
    await snyt_pribl_garden(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'garden_nalog')
async def oplata_nalogov_garden_s(callback_query: types.CallbackQuery):
    await oplata_nalogov_garden(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'garden_baytree')
async def buy_tree_s(callback_query: types.CallbackQuery):
    await buy_tree(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'garden_polit')
async def polit_dereva_garden_s(callback_query: types.CallbackQuery):
    await polit_dereva_garden(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'business_sobrat')
async def snyt_pribl_business_s(callback_query: types.CallbackQuery):
    await snyt_pribl_business(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'business_nalog')
async def business_nalog_s(callback_query: types.CallbackQuery):
    await oplata_nalogov_business(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'business_ter')
async def buy_territory_s(callback_query: types.CallbackQuery):
    await buy_territory(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'business_bis')
async def buy_bsterritory_s(callback_query: types.CallbackQuery):
    await buy_bsterritory(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'ferma_bycards')
async def buy_cards_s(callback_query: types.CallbackQuery):
    await buy_cards(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'ferma_sobrat')
async def snyt_pribl_ferma_s(callback_query: types.CallbackQuery):
    await snyt_pribl_ferma(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'ferma_nalog')
async def oplata_nalogov_ferma_S(callback_query: types.CallbackQuery):
    await oplata_nalogov_ferma(callback_query)


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


async def main(dp):
    await automatisation()


handlers_folder = 'modules'
for filename in os.listdir(handlers_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = __import__(f"{handlers_folder}.{module_name}", fromlist=["register_handlers"])
        module.register_handlers(dp)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=main, skip_updates=True)

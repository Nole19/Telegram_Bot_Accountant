from aiogram import executor
from db import BotDB
from dispatcher import dp

BotDB = BotDB('accountant.db')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

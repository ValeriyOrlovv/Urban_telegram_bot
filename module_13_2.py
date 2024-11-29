from aiogram import Bot, Dispatcher, executor, types
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
api = os.getenv('BOT_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

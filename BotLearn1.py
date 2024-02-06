from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message 

BOT_TOKEN = '6358456657:AAGeGX8wUfEcgE5kOXK9rWBVr-3OnjK_0To'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
        )

async def send_echo(message: Message):
    await message.reply(text=message.text)
    
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)
    
if __name__ == '__main__':
    dp.run_polling(bot)
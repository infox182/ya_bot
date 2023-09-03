import kb
from config import dp, bot
from aiogram import types
import os 

CURRENT_PATH = os.getcwd()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Привет! Это Бот для Знакомста с Ильей С.!",
        reply_markup = kb.menu
    )
    
@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        "Тыкай кнопочки или используй комманды:\n"
        "/current_selfie - мое настоящее селфи\n"
        "/school_photo - фото со старшей школы\n"
        "/my_hobby - пост о моем хобби\n",
        reply_markup = kb.menu
    )
    

@dp.message_handler(commands=["current_selfie"])
async def current_selfie(message: types.Message):
    file_path = f'{CURRENT_PATH}/data_files/selfie.jpg'
    await bot.send_photo(
        message.chat.id,
        photo = open(file_path,'rb'),
        caption="Test caption!",
    )


@dp.message_handler(commands=["school_photo"])
async def school_photo(message: types.Message):
    file_path = f'{CURRENT_PATH}/data_files/school.jpg'
    await bot.send_photo(
        message.chat.id,
        photo = open(file_path,'rb'),
        caption="Test caption!",
    )

@dp.message_handler(commands=["my_hobby"])
async def my_hobby(message: types.Message):
    await message.answer(
        "Играю в баскетбол"
    )
    
@dp.callback_query_handler()
async def gpt_say(callback: types.CallbackQuery):
    if callback.data == 'gpt_say':
        await callback.answer(
            "GPT"
        )
    
    
@dp.callback_query_handler()
async def sql_say(callback: types.CallbackQuery):
    if callback.data == 'sql_say':
        await callback.answer(
            "SQL"
        )
    
@dp.callback_query_handler()
async def love_say(callback: types.CallbackQuery):
    if callback.data == 'love_say':
        await callback.answer(
            "LOVE"
        )

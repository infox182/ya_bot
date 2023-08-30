import kb
from config import dp, bot
from aiogram import types
from aiogram import F
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
        photo = file_path,
        reply_markup = kb.menu,
        caption="Test caption!",
    )


@dp.message_handler(commands=["school_photo"])
async def school_photo(message: types.Message):
    file_path = f'{CURRENT_PATH}/data_files/school.jpg'
    await bot.send_photo(
        message.chat.id,
        photo = file_path,
        reply_markup = kb.menu,
        caption="Test caption!",
    )

@dp.message_handler(commands=["my_hobby"])
async def my_hobby(message: types.Message):
    await message.answer(
        "Играю в баскетбол",
        reply_markup = kb.menu
    )
    
@dp.callback_query(F.data.in_(['gpt_say']))
async def gpt_say(callback: types.CallbackQuery):
    await callback.answer(
        "GPT",
        reply_markup = kb.menu
    )
    
    
@dp.callback_query(F.data.in_(['sql_say']))
async def sql_say(callback: types.CallbackQuery):
    await callback.answer(
        "SQL",
        reply_markup = kb.menu
    )
    
@dp.callback_query(F.data.in_(['love_say']))
async def love_say(callback: types.CallbackQuery):
    await callback.answer(
        "LOVE",
        reply_markup = kb.menu
    )

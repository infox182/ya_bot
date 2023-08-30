from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [InlineKeyboardButton(text = "🧑‍🏫 Объясняю своей бабушке, что такое GPT", callback_data = "gpt_say"),
    InlineKeyboardButton(text = "💻 Объясняю разницу между SQL и NoSQL", callback_data = "sql_say"),
    InlineKeyboardButton(text = "❤️ Моя история первой любви", callback_data = "love_say")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

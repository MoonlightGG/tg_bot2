from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


select_task = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Process status',
            callback_data= 'zxc'
        )
    ]
])
import logging
from local import running_processes
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, types, Dispatcher, F
from aiogram.types import BotCommand, BotCommandScopeDefault, CallbackQuery
import asyncio
from config import Token_api
from aiogram.filters import Filter
import config
from inline import select_task
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=Token_api)
dp = Dispatcher()



reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Process status'
        )
    ]
])

@dp.message(F.text == '/start')
async def get_inline(message: types.Message):
    await message.answer(f'Greetings!, {message.from_user.first_name}. Choose wisely',
                         reply_markup=reply_keyboard)




@dp.callback_query()
async def process_callback_button1(callback_query: types.CallbackQuery):
    if callback_query.data == 'zxc':
        await bot.send_message(text='/Process_status', chat_id=callback_query.from_user.id)


@dp.message(F.text == 'Process status')
async def event_log(message: types.Message):
    a = running_processes()
    if len(a) > 4095:
        for x in range(0, len(a), 4095):
            z = a.rfind('\n')
            await bot.send_message(text=a[0:z], chat_id=message.from_user.id)
            await bot.send_message(text=a[z:len(a)], chat_id=message.from_user.id)


    else:
        await bot.send_message(text=a, chat_id=message.from_user.id)






async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())

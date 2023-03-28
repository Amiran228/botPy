import logging
import time

from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ''  # никуда не скидывать

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# button_start = KeyboardButton()

start_button = [
    [
        types.KeyboardButton(text='/start'),
        types.KeyboardButton(text='/menu'),
        types.KeyboardButton(text='/techsupport'),
        types.KeyboardButton(text='/howtouse')
    ],
]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard_start = types.ReplyKeyboardMarkup(keyboard=start_button)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}", reply_markup=keyboard_start)


menuKB = InlineKeyboardMarkup(row_width=1)
menuButton = InlineKeyboardButton(text='Человек и общество', callback_data="menu_1")
menuButton2 = InlineKeyboardButton(text='Социальные отношения', callback_data="menu_2")
menuButton3 = InlineKeyboardButton(text='чет 1', callback_data="menu_3")
menuButton4 = InlineKeyboardButton(text='чет 2 ', callback_data="menu_4")
menuButton5 = InlineKeyboardButton(text='чет 3', callback_data="menu_5")
menuKB.add(menuButton, menuButton2, menuButton3, menuButton4, menuButton5)


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await message.answer('тут меню', reply_markup=menuKB)
    #await message.reply()
    #await callback.answer();


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('menu_'))
async def process_callback_menubutton(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    logging.info({code})
    if code.isdigit(): # Исправь нахуй даун безмамный, нахуй  нт
        code = int(code)
        
    if code == 1:
        await bot.answer_callback_query(callback_query.id, text='Нажата первая кнопка')
    elif code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code} ')


@dp.message_handler(commands=['techsupport'])
async def techSupport(message: types.Message):
    await message.answer("Он во всем виноват - @lkklkk")


@dp.message_handler(commands=['howtouse'])
async def howToUse(message: types.Message):
    await message.answer("тут должно быть про использование")


@dp.message_handler()
async def echo(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    message_name = message.text
    logging.info(f'{user_id} {user_full_name} {time.asctime()} {message_name}')
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

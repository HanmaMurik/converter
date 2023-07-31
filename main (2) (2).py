import telebot
from currency_converter import CurrencyConverter
from telebot import types

tg_bot = telebot.TeleBot('6394463227:AAHrD2wwD1oB_UF0CVpF8LkIzs_FmCfdPOY')
module = CurrencyConverter()
something = 0

@tg_bot.message_handler(commands=['start'])
def start(message):
    tg_bot.send_message(message.chat.id, 'Hello!!! add sum')
    tg_bot.register_next_step_handler(message, count)

def count(message):
    global something
    try:
        something = int(message.text.strip())
    except ValueError:
        tg_bot.send_message(message.chat.id, 'ERROR_MACROS!. Please, stick to the rules and write the amount')
        tg_bot.register_next_step_handler(message, count)
        return
    if something > 0:
        button = types.InlineKeyboardMarkup(row_width=1)
        popit1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
        popit2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
        popit3 = types.InlineKeyboardButton('EUR/RUB', callback_data='EUR/RUB')
        popit4 = types.InlineKeyboardButton('RUB/EUR', callback_data='RUB/EUR')
        popit5 = types.InlineKeyboardButton('USD/RUB', callback_data='USD/RUB')
        popit6 = types.InlineKeyboardButton('RUB/USD', callback_data='RUB/USD')
        button.add(popit1, popit2, popit3, popit4, popit5, popit6)
        tg_bot.send_message(message.chat.id, 'add count of valut', reply_markup=button)
    else:
        tg_bot.send_message(message.chat.id, 'ERROR_MACROS!. your number is less or equals to 0')
        tg_bot.register_next_step_handler(message, count)


@tg_bot.callback_query_handler(func=lambda call: True)
def cash(call):
    meanings = call.data.split('/')
    answer = module.convert(something, meanings[0], meanings[1])
    tg_bot.send_message(call.message.chat.id, f'Result: {round(answer, 5)}')
    tg_bot.register_next_step_handler(call.message, count)


tg_bot.polling(none_stop=True)



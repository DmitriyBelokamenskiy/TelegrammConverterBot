import telebot
from Config import TOKEN, keys, text
from extensions import GetPrice, Input, ConversionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text1 = 'Доступные валюты:'
    for key in keys:
        text1 = '\n'.join((text1, key,))
    bot.reply_to(message, text1)


@bot.message_handler(content_types=['text', ])
def input_message(message: telebot.types.Message):
    try:
        correct_input = Input.check_input(message.text)

    except ConversionException as e:
        bot.send_message(message.chat.id, f'{e}')

    else:
        correct_input = Input.check_input(message.text)
        result = GetPrice.get_price(correct_input)
        bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)

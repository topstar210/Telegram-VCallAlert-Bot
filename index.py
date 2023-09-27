import config

import telebot
from telebot import types

bot = telebot.TeleBot(config.botkey)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("hello bot👋")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Hello! I'm your alert assistant bot!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'hello bot👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #creating new buttons
        btn1 = types.KeyboardButton('Bot test')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ask a question you are interested in ❓', reply_markup=markup) #bot response

    elif message.text == 'Bot test':
        bot.send_message(message.from_user.id, 'This is a bot test', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) #required part for the bot to work
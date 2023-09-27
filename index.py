import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Say hello")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Hello! I'm your assistant bot!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Say hello':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #creating new buttons
        btn1 = types.KeyboardButton('How to become an author on Habré??')
        btn2 = types.KeyboardButton('Site Rules')
        btn3 = types.KeyboardButton('Tips for designing a publication')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Ask a question you are interested in', reply_markup=markup) #bot response


    elif message.text == 'How to become an author on Habré??':
        bot.send_message(message.from_user.id, 'You write the first post, it is checked by moderators, and, if all is well, it is sent to the main Habr feed, where it gains views, comments and ratings. ' + '[link](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == 'Site Rules':
        bot.send_message(message.from_user.id, 'You can read the site rules at' + '[link](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == 'test':
        print(message.from_user.id)
        # bot.send_message('serhiiofii', 'Successsfully !!!!!', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #required part for the bot to work
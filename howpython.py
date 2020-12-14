import telebot
import random

bot = telebot.TeleBot('1316436768:AAF3R_D1uXKUJYPi5SWmh-vJDbyMHvjRfVo')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/py')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши мне /help', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def send_text(message):
    bot.send_message(message.chat.id, 'Привет, вот мои команды: ')
    bot.send_message(message.chat.id, 'команда /py определяет насколько вы питонист')

@bot.message_handler(commands=['py'])
def send_text(message):
    raand = random.randint(0, 100)
    f = 'Вы питонист на ' + str(raand) + '%'
    bot.send_message(message.chat.id, f)

bot.polling()

import telebot
import random

bot = telebot.TeleBot('1486328249:AAHm2E9-dWN_6edvb21jkxOM90Dcz8B4eII')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/random')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, напиши мне /help', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def send_text(message):
    bot.send_message(message.chat.id, 'Привет, вот мои команды: /random')

@bot.message_handler(commands=['random'])
def send_text(message):
    raand = random.randint(0, 100)
    f = 'Ваше число: ' + str(raand)
    bot.send_message(message.chat.id, f)

bot.polling()

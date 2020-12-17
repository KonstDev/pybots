import telebot
import random
from telebot import types
import datetime

bot = telebot.TeleBot('')


@bot.message_handler(commands=['uid'])
def send_text(message):
    bot.send_message(message.chat.id, message.from_user.id)

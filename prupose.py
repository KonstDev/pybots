# -*- coding: utf-8 -*-

import telebot
import random
from telebot import types
import datetime

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def send_text(message):
    bot.send_message(message.chat.id, 'Hey, here You can write your feedback!')



# Инлайн-режим с
@bot.message_handler(content_types=['text'])
def send_text(message):
        #raand = random.seed(message.user.id)
        #f = 'Вы питонист на ' + str(raand) + '%'
        bot.send_message(447648578, str(message.from_user.id) + ' : ' + message.text)
        print(message.from_user.id)
        bot.send_message(message.chat.id, 'Thanks, your proposal has been sent.')

bot.polling() 

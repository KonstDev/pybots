import telebot
import random
from telebot import types
import time

bot = telebot.TeleBot('')


#made by KonstDev

print('HowJewBot v.1.0 is running.')

# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: True)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="", callback_data="test"))
    results = []
    cache_time = 0
    rrr = random.randrange(0, 100, 1)
    rrrstr = '🇮🇱 I am ' + str(rrr) + '% jew 🇮🇱!'
    single_msg = types.InlineQueryResultArticle(
        id="1", title="How jew are You?",
        input_message_content=types.InputTextMessageContent(message_text = rrrstr),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results, cache_time=0)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if (message.text == "/py"):
        raand = random.seed(message.user.id)
        f = 'Вы питонист на ' + str(raand) + '%'
        bot.send_message(message.chat.id, f)

bot.polling()

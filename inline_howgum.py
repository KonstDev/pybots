import telebot
import random
from telebot import types
import datetime

bot = telebot.TeleBot('1457557479:AAELLNrkOVaurYh5rQh9bnPN95-UTvnMe70')


@bot.message_handler(commands=['uid'])
def send_text(message):
    bot.send_message(message.chat.id, message.from_user.id)



# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: True)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="", callback_data="test"))
    results = []
    random.seed(query.from_user.id + int(datetime.datetime.today().isoweekday()))
    cache_time = 0
    guum = random.randint(0,6)
    rrr = random.randrange(1, 101, 1)
    if (guum == 0 or guum == 1 or guum == 2):
        rrrstr = 'Я технарь на ' + str(rrr) + '%!'
    elif (guum == 4 or guum == 3 or guum == 5):
        rrrstr = 'Я гуманитарий на ' + str(rrr) + '%!'
    else:
        rrrstr = 'Tyanochku by'
    #rrrstr = 'I am ' + str(rrr) + '% python!'
    tyan = 'Tyanochku by'
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Насколько Вы технарь или гуманитарий?",
        input_message_content=types.InputTextMessageContent(message_text = rrrstr),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results, cache_time=0)


#@bot.message_handler(content_types=['text'])
#def send_text(message):
 #   if (message.text == "/py"):
    #    raand = random.seed(message.user.id)
   #     f = 'Вы питонист на ' + str(raand) + '%'
     #   bot.send_message(message.chat.id, f)

bot.polling()

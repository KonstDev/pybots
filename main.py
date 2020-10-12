import HLTV
import vk_api
import telebot
from vk import utils

bot = telebot.TeleBot('1319312903:AAH4x6ERJFenG1itR5UexZfB8tBUHuccuvw')
#print(HLTV.get_upcoming_matches())
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANfX3y1pDJrr3kE7WrpnNXAWRnljtwAAuQDAAKJ6uUH96krUY45jZ8bBA')

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(utils.getShortLink(str(message.text), "fe4e5280fe4e5280fe4e528084fe3a0871ffe4efe4e5280a1cd4c4f33114dce4b289b95"))
#   if message.text.lower() == 'live':
 #      bot.send_message(message.chat.id, HLTV.get_live_matches())
  # elif message.text.lower() == 'upcoming':
   #    bot.send_message(message.chat.id, HLTV.get_upcoming_matches())
   #elif message.text.lower() == 'ты лох':
    #   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMQX3tVfMBvgokE-8TJzjwY8rMVSbUAAlQAAy7yXCUakl03HYs5qhsE')
   #elif message.text.lower() == 'mylogin':
    #   bot.send_message(message.chat.id, message.chat.username)
  # elif message.text == 'ямыбатька':
   #    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMmX3tdiPad77cbjiAPKbst_dVqnncAAu0AA6tXxAsI817NM7dIhBsE')
    #   #CAACAgIAAxkBAAMQX3tVfMBvgokE-8TJzjwY8rMVSbUAAlQAAy7yXCUakl03HYs5qhsE
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message.sticker.file_id)
#.file_id
#GRAY
#GUKAY
#VYASNY ZYALYLAY TEPLAY CHARY

bot.polling()
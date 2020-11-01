import telebot
import pyshorteners as pysh
import requests







#text1 = "hello"
# print(HLTV.get_upcoming_matches())

bot = telebot.TeleBot('1396209391:AAFJE_mGt8VmtBu0npi__qAn-66DsGcHguA')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANfX3y1pDJrr3kE7WrpnNXAWRnljtwAAuQDAAKJ6uUH96krUY45jZ8bBA')


@bot.message_handler(content_types=['text'])
def send_text(message):
    #Authorization =
    #url = "https://api-ssl.bitly.com/v4/shorten"
    #values = {'url': message}
    #r = requests.post(url, params=values)
   # resp = r.text
    url = message.text
    resp = pysh.Shortener().tinyurl.short(url)
    print(message.text, " : ", resp)
    bot.send_message(message.chat.id,resp)


#   if message.text.lower() == 'live':
#      bot.send_message(message.chat.id, HLTV.get_live_matches())
# elif message.text.lower() == 'upcoming':
#    bot.send_message(message.chat.id, HLTV.get_upcoming_matches())

# elif message.text.lower() == 'ты лох':

#   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMQX3tVfMBvgokE-8TJzjwY8rMVSbUAAlQAAy7yXCUakl03HYs5qhsE')
# elif message.text.lower() == 'mylogin':
#   bot.send_message(message.chat.id, message.chat.username)
# elif message.text == 'ямыбатька':
#    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMmX3tdiPad77cbjiAPKbst_dVqnncAAu0AA6tXxAsI817NM7dIhBsE')
#   #CAACAgIAAxkBAAMQX3tVfMBvgokE-8TJzjwY8rMVSbUAAlQAAy7yXCUakl03HYs5qhsE
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message.sticker.file_id)


# .file_id
# GRAY
# GUKAY
# VYASNY ZYALYLAY TEPLAY CHARY

bot.polling()

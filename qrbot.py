import telebot
import qrcode
import os

bot = telebot.TeleBot('1914244980:AAE50Mk9TGKETTLcvVTl5XADtlwBqQkbviA')

global n
n = 0
os.system('mkdir pics')
@bot.message_handler(content_types=['text'])
def send_and_generateqr(message):
    global n
    s = str(message.text)
    img = qrcode.make(s)
    type(img)
    #path = "/pics/
    path = "code" + str(n) + ".png"
    img.save(path)
    bot.send_photo(message.chat.id, open(path, 'rb'))

while (True):
    try:
        bot.polling()
    except Exception as ex:
        print(ex)

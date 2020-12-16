import telebot

bot = telebot.TeleBot('')
#print(HLTV.get_upcoming_matches())
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANkX3y4lgttowG4mbZYU7jA2m9yVw4AAocCAAJWnb0KQu10K0BX0JAbBA')
  bot.send_message(message.chat.id, 'Привет, отправь мне стикер для того чтобы получить его file_id')
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)
#.file_id
#GRAY
#GUKAY
#VYASNY ZYALYONAY TEPLAY CHARY

bot.polling()

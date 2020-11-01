import telebot

bot = telebot.TeleBot('yr_token')
@bot.message_handler(commands=['start'])

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_message(message.chat.id, "file_ id is --> ")
    bot.send_message(message.chat.id,message.sticker.file_id)

bot.polling()

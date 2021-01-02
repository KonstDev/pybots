import telebot

bot = telebot.TeleBot('yr_token')
@bot.message_handler(commands=['start'])
def send_message(message):
   	bot.send_message(message.chat.id, "Pong!")
    		
bot.polling()

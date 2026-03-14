import telebot

TOKEN = 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Напишите\photo")
    
    @bot.message_handler(commands['photo])
    def photo(message):
    
        photo_url = 

        bot.send_photo(message.chat.id,
                       photo_url)

                       bot.infinty_polling()
                       
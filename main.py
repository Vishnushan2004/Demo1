import telebot

# Replace with your actual bot token from BotFather
TOKEN = "8757623892:AAFqUdsFlVAkK6A8GNdXCixj9SLZwbPEBbw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi")

# Keep the bot running
bot.polling()

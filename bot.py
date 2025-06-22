import telebot
import json

with open('config.json', 'r') as f:
    config = json.load(f)

bot = telebot.TeleBot(config['BOT_TOKEN'])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مرحبًا بك في FayNo 🎉")

bot.polling()
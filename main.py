import telebot
from config import settings
from model.model import Model
from count.count import Count

token = settings['main']
bot = telebot.TeleBot(token)

model = Model()
count = Count(bot)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,settings['start_message'])

@bot.message_handler(content_types='text')
def start_message(message):
    if message.text == '/start':
        return

    bot.send_message(message.chat.id, "Proccessing...")

    output = model.generate(message.text)
    bot.send_message(message.chat.id,output)
    count()

bot.polling()
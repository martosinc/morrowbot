import telebot
from config import settings

class Count():
    def __init__(self,bot):
        self.count = 0
        self.cap = settings['cap']
        self.channel = settings['channel']
        self.bot = bot

    def __call__(self):
        self.count += 1
        if self.count == self.cap:
            self.count = 0

            self.bot.send_message(self.channel,f'+{self.cap} Requests')
import telebot
from telebot import types
from secret_vars import *
import os

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['tts'])
def handle_tts(message):
    try:
        text = [x for x in message.text.split() if '/tts@' not in x]

        #this will make sure that the string doesn't have any " in it where
        #there shouldn't be, i.e. can't use this bot to execute commands
        text = ' '.join(text) + "\""
        text = "\"" + text[:text.index("\"")] + "\""  

        os.system("espeak -w speech.wav " + text)

        audio = open('speech.wav','rb')
        bot.send_audio(
                message.chat.id, 
                audio)
        audio.close
    except:
        print("too bad")

while True:
    try:
        bot.polling()
    except:
        pass

import telebot
from telebot import types
from secret_vars import *
import os

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['tts'])
def handle_tts(message):
    try:
        text = message.text[5:]
        print(text)
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

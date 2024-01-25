import telebot
import time

bot = telebot.TeleBot('6958783112:AAEvgeKxpnClQFT1sT-kL7M-4R8-j0Z-1zI')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message == '\start':
        bot.send_message(message.from_user.id, 'Привет', reply_markup=webAppKeyboard())
    else:
        bot.send_message(message.from_user.id, 'Воспользуйтесь меню', reply_markup=webAppKeyboard())


def webAppKeyboard(): 
   keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
   webAppTest = telebot.types.WebAppInfo("https://bug-games.ru") 
   one_butt = telebot.types.KeyboardButton(text="Games", web_app=webAppTest)
   keyboard.add(one_butt)

   return keyboard

bot.polling(none_stop=True, interval=0)

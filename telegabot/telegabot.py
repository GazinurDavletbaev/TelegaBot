import telebot

bot = telebot.TeleBot('7084082443:AAGrqnOeAa7ub1vW1LRytZdN0pzLIZhHYT4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')


@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')

bot.polling(none_stop=True)

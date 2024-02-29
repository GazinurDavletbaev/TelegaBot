import telebot
from func import plus

bot = telebot.TeleBot('7084082443:AAGrqnOeAa7ub1vW1LRytZdN0pzLIZhHYT4')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')


print(plus(3, 4))
print(plus(4, 4))
print(plus(5, 4))
print(plus(5, 5))

@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')


@bot.message_handler(commands=['branch dev'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')


@bot.message_handler(commands=['merge master'])
def main(message):
    bot.send_message(message.chat.id, 'Privet Danja')


bot.polling(none_stop=True)

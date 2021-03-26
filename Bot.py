import telebot

try:
    from Token import token
except ImportError:
    token = ''


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот напоминатель')

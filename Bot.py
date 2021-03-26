import telebot
import NoBotFunctions

try:
    from Token import token
except ImportError:
    token = ''


bot = telebot.TeleBot(token)
date_rem = []

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    edit_button = telebot.types.KeyboardButton('Редактировать напоминание')
    create_button = telebot.types.KeyboardButton('Создать напоминание')
    all_list_button = telebot.types.KeyboardButton('Список всех напоминаний')
    markup.add(edit_button, create_button, all_list_button)
    bot.send_message(chat_id=message.chat.id, text="Выберете действие:", reply_markup=markup)


@bot.message_handler(regexp='Редактировать напоминание')
def handle_message(message):
    bot.send_message(message.chat.id, 'Редактируем')


@bot.message_handler(regexp='Создать напоминание')
def handle_message(message):
    bot.send_message(message.chat.id, 'Когда выхотите получить напоминание?')
    bot.send_message(message.chat.id, 'Введите дату в формате дд.мм чч:мм')
    
    
@bot.message_handler(regexp='Список всех напоминаний')
def handle_message(message):
    bot.send_message(message.chat.id, 'Список')
    

@bot.message_handler(regexp='^[0-3][0-9]\.[0-1][0-9] [0-2][0-9]:[0-5][0-9]$')
def handle_message(message):
    date_rem.append(message.text)
    bot.send_message(message.chat.id, 'Введите напоминание, начав его с $')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text[0] == '$':
        date_rem.append(message.text[1:])
        NoBotFunctions.add_remind(date_rem)
    

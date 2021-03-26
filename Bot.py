import telebot

try:
    from Token import token
except ImportError:
    token = ''


bot = telebot.TeleBot(token)


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
    bot.send_message(message.chat.id, 'Введите дату в формате дд.мм.гг чч:мм')
    
    
@bot.message_handler(regexp='Список всех напоминаний')
def handle_message(message):
    bot.send_message(message.chat.id, 'Список')
    

import telebot
import NoBotFunctions

try:
    from Token import token
except ImportError:
    token = ''


bot = telebot.TeleBot(token)
date_rem_id = [None, None, None]


@bot.message_handler(commands=['start'])
def start_message(message):
    """Обработчик команды /start: выводит на экран 3 кнопки."""
    
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    edit_button = telebot.types.KeyboardButton('Редактировать напоминание')
    create_button = telebot.types.KeyboardButton('Создать напоминание')
    all_list_button = telebot.types.KeyboardButton('Список всех напоминаний')
    markup.add(edit_button, create_button, all_list_button)
    bot.send_message(chat_id=message.chat.id, text="Выберете действие:", reply_markup=markup)


@bot.message_handler(regexp='Редактировать напоминание')
def handle_message(message):
    """Обработчик кнопки 'Редактируем'."""
    
    bot.send_message(message.chat.id, 'Редактируем')


@bot.message_handler(regexp='Создать напоминание')
def handle_message(message):
    """Обработчик кнопки 'Создать напоминание'."""
    
    bot.send_message(message.chat.id, 'Когда вы хотите получить напоминание?')
    bot.send_message(message.chat.id, 'Введите дату в формате дд.мм чч:мм')
    
    
@bot.message_handler(regexp='Список всех напоминаний')
def handle_message(message):
    """Обработчик кнопки 'Список всех напоминаний'."""
 
    bot.send_message(message.chat.id, 'Список')
    

@bot.message_handler(regexp='^[0-3][0-9]\.[0-1][0-9] [0-2][0-9]:[0-5][0-9]$')
def handle_message(message):
    """Функция записи даты напоминания."""
 
    date_rem_id[0] = message.text
    bot.send_message(message.chat.id, 'Введите напоминание, начав его с $')


@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Функция записи текста напоминания (также вызывает функцию добавления напоминания)."""
 
    if message.text[0] == '$':
        date_rem_id[1] = message.text[1:]
        date_rem_id[2] = message.chat.id
        NoBotFunctions.add_remind(date_rem_id)

import telebot
import NoBotFunctions

try:
    from Token import token
except ImportError:
    token = ''


bot = telebot.TeleBot(token)
time_rem_id = [None, None, None]
num_text = [None, None]


states = {}


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

    bot.send_message(message.chat.id, 'Введите номер напоминания')

    states[message.chat.id] = {'create_date': False, 'create_text': False, 'edit_number': True, 'edit_text': False}


@bot.message_handler(regexp='Создать напоминание')
def handle_message(message):
    """Обработчик кнопки 'Создать напоминание'."""
    
    bot.send_message(message.chat.id, 'Когда вы хотите получить напоминание?')
    bot.send_message(message.chat.id, 'Введите время в формате чч:мм')
    states[message.chat.id] = {'create_date': True, 'create_text': False, 'edit_number': False, 'edit_text': False}


@bot.message_handler(regexp='Список всех напоминаний')
def handle_message(message):
    """Обработчик кнопки 'Список всех напоминаний'."""
 
    NoBotFunctions.print_reminds_list(message.chat.id)
    

@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Функция обработки текста"""
 
    if states[message.chat.id]['create_date']:
        time_rem_id[0] = message.text
        bot.send_message(message.chat.id, 'Введите напоминание')
        states[message.chat.id] = {'create_date': False, 'create_text': True, 'edit_number': False, 'edit_text': False}
        
    elif states[message.chat.id]['create_text']:
        time_rem_id[1] = message.text
        time_rem_id[2] = message.chat.id
        NoBotFunctions.add_remind(time_rem_id)
        bot.send_message(message.chat.id, 'Напоминание создано')
        states[message.chat.id] = {'create_date': False, 'create_text': False, 'edit_number': False, 'edit_text': False}
    
    elif states[message.chat.id]['edit_number']:
        num_text[0] = int(message.text)
        bot.send_message(message.chat.id, 'Введите новое сообщение')
        states[message.chat.id] = {'create_date': False, 'create_text': False, 'edit_number': False, 'edit_text': True}
    
    elif states[message.chat.id]['edit_text']:
        num_text[1] = message.text
        NoBotFunctions.edit_remind(message.chat.id, num_text)
        bot.send_message(message.chat.id, 'Напоминание изменено')
        states[message.chat.id] = {'create_date': False, 'create_text': False, 'edit_number': False, 'edit_text': False}

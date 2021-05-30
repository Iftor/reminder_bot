from datetime import datetime
from Bot import bot
from time import sleep
import schedule


def send_message_func(remind):
    """Функция выдачи напоминания"""
    
    bot.send_message(remind['id'], remind['text'])
    return schedule.CancelJob


def add_remind(time_rem_id):
    """Функция добавления напоминания в расписание"""
    
    time = datetime.strptime(time_rem_id[0], '%H:%M')
    remind = {'text': time_rem_id[1], 'id': time_rem_id[2]}
    schedule.every().day.at(f'{time.hour}:{time.minute}').do(send_message_func, remind=remind)
    time_rem_id[0], time_rem_id[1], time_rem_id[2] = None, None, None


def issue_remind():
    """Функция выдачи напоминаний по расписанию"""

    while True:
        schedule.run_pending()
        sleep(1)


def bot_polling():
    """Работа бота"""
    
    bot.polling()

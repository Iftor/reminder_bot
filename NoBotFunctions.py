from Bot import bot
from time import sleep
import schedule

reminds = dict()


def send_message_func(remind):
    """Функция выдачи напоминания"""
    
    bot.send_message(remind['id'], remind['text'])
    reminds[remind['id']].remove(remind)
    return schedule.CancelJob


def add_remind(time_rem_id):
    """Функция добавления напоминания в расписание"""
    
    time = time_rem_id[0].split(':')

    remind = {'time': time_rem_id[0], 'text': time_rem_id[1], 'id': time_rem_id[2]}
    schedule.every().day.at(f'{time[0]}:{time[1]}').do(send_message_func, remind=remind)
    if remind['id'] in reminds:
        reminds[remind['id']].append(remind)
    else:
        reminds[remind['id']] = [remind]

    time_rem_id[0], time_rem_id[1], time_rem_id[2] = None, None, None


def print_reminds_list(id):
    message = ''
    if id in reminds:
        for remind in reminds[id]:
            message += f'{remind["time"]}: {remind["text"]}\n'
    else:
        message = 'Список пуст'
    bot.send_message(id, message)


def issue_remind():
    """Функция выдачи напоминаний по расписанию"""

    while True:
        schedule.run_pending()
        sleep(1)


def bot_polling():
    """Работа бота"""
    
    bot.polling()

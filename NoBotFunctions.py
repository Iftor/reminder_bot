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
    job = schedule.every().day.at(f'{time[0]}:{time[1]}').do(send_message_func, remind=remind)
    remind['job'] = job
    if remind['id'] in reminds:
        reminds[remind['id']].append(remind)
    else:
        reminds[remind['id']] = [remind]
    time_rem_id[0], time_rem_id[1], time_rem_id[2] = None, None, None


def print_reminds_list(id):
    """Функция просмотра списка напоминаний"""
    
    message = ''
    if id in reminds:
        for i, remind in enumerate(reminds[id]):
            message += f'№{i + 1} ({remind["time"]}) {remind["text"]}\n'
    else:
        message = 'Список пуст'
    bot.send_message(id, message)


def edit_remind(id, number, text):
    """Функция редактирования напоминания"""
    
    remind = reminds[id][number - 1]
    reminds[id].remove(remind)
    schedule.cancel_job(remind['job'])
    add_remind([remind['time'], text, id])


def issue_remind():
    """Функция выдачи напоминаний по расписанию"""

    while True:
        schedule.run_pending()
        sleep(1)


def bot_polling():
    """Работа бота"""
    
    bot.polling()

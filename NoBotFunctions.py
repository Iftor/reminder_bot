from datetime import datetime
from Bot import bot
from time import sleep


reminds = []


def add_remind(date_rem_id):
    date = datetime.strptime(date_rem_id[0], '%d.%m %H:%M')
    remind = {'date': date, 'text': date_rem_id[1], 'id': date_rem_id[2]}
    reminds.append(remind)
    date_rem_id[0], date_rem_id[1], date_rem_id[2] = None, None, None


def issue_remind():
    while True:
        current_datetime = datetime.now()
        for i, remind in enumerate(reminds):
            if (remind['date'].day == current_datetime.day
                    and remind['date'].month == current_datetime.month
                    and remind['date'].hour == current_datetime.hour
                    and remind['date'].minute == current_datetime.minute):
                bot.send_message(remind['id'], remind['text'])
                reminds.pop(i)
            else:
                sleep(30)


def bot_polling():
    bot.polling()

from datetime import datetime
from Bot import bot
from time import sleep


reminds = []


def add_remind(date_rem_id):
    date = datetime.strptime(date_rem_id[0], '%d.%m %H:%M')
    remind = {'date': date, 'text': date_rem_id[1], 'id': date_rem_id[2]}
    reminds.append(remind)
    date_rem_id[0], date_rem_id[1], date_rem_id[2] = None, None, None

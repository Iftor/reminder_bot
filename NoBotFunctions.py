reminds = []


def add_remind(date_rem: list[str]):
    date = date_rem[0]
    remind = date_rem[1]
    date, time = date.split(' ')
    day, month = date.split('.')
    hour, minute = time.split(':')
    reminds.append({'day': day, 'month': month, 'hour': hour, 'minute': minute})
    
    
    
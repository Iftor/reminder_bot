from threading import Thread
from NoBotFunctions import issue_remind, bot_polling


if __name__ == '__main__':
    p1 = Thread(target=bot_polling)
    p2 = Thread(target=issue_remind)
    p1.start()
    p2.start()

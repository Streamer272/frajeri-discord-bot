from datetime import datetime, date
from time import sleep
from threading import Thread
from os import system, chdir

last_send_date = ""


def send():
    chdir("\\".join(__file__.split("\\")[0:-1]))
    send_thread = Thread(target=system, args=["python send.py"])
    send_thread.daemon = True
    send_thread.start()


if __name__ == "__main__":
    print("Bot running...")

    while True:
        time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

        if time_ > 135500 and last_send_date != str(date.today()):
            last_send_date = str(date.today())
            send()

        sleep(60)

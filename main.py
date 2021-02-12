import datetime
import time
import send

last_send_date = "wda"


if __name__ == "__main__":
    print("Bot running...")
    while True:
        while True:
            time_ = int(str(datetime.datetime.now().strftime("%H:%M:%S")).replace(":", ""))
            if time_ > 140000 and last_send_date != str(datetime.date.today()):
                last_send_date = str(datetime.date.today())
                break
            time.sleep(1)
        send.send()

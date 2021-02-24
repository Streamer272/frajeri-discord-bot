from datetime import datetime, date
from time import sleep
from threading import Thread
from os import system, write
from sys import argv

argv.pop(0)  # we dont want the "main.py" arg here
last_send_date = str(date.today())
pray_time = 135500

for i in range(len(argv)):
    if "--set-starttoday" in argv[i]:
        last_send_date = "" if argv[i].replace("--set-starttoday=", "").lower() in ("true", "t", "yes", "y", "1") else str(date.today())
    
    elif "--set-praytime" in argv[i]:
        try:
            pray_time = int(argv[i].replace("--set-praytime=", ""))
        except:
            raise TypeError


def write_log(message: str) -> None:
    file = open("log-" + str(date.today()) + ".txt", "a")
    file.write(str(datetime.now().strftime("%H:%M:%S")) + ": " + str(message) + "\n")


def send() -> None:
    write_log("Sending pray message...")
    send_thread = Thread(target=system, args=["python3 send.py"])
    send_thread.daemon = True
    send_thread.start()


if __name__ == "__main__":
    print("Bot running...")

    while True:
        try:
            time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

            if time_ > pray_time and last_send_date != str(date.today()):
                print("Sending message...")
                last_send_date = str(date.today())
                send()

            sleep(60)

        except Exception as err:
            print("Error occoured")
            write_log("Error occoured: " + str(err))
            sleep(5)

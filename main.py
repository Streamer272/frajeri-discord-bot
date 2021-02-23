from datetime import datetime, date
from time import sleep
from sys import argv
from asyncio import run
from threading import Thread
import discord

today = str(date.today())
warn_time = 135500
pray_time = 140000
channel_id = 809822474668736583
bot_token = "ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA"

for i in range(len(argv)):
    if "--set-starttoday=" in argv[i]:
        today = "" if argv[i].split("--set-starttoday=")[1] in ("true", "True", "t") else today

    elif "--set-warntime=" in argv[i]:
        warn_time = int(argv[i].split("--set-warntime=")[1])

    elif "--set-praytime=" in argv[i]:
        pray_time = int(argv[i].split("--set-praytime=")[1])
    
    elif "--set-channelid=" in argv[i]:
        channel_id = int(argv[i].split("--set-channelid=")[1])
    
    elif "--set-bottoken=" in argv[i]:
        bot_token = argv[i].split("--set-bottoken=")[1]

last_send_date = today


class CustomClient(discord.Client):
    async def on_ready(self):
        print("Bot running...")
    
    async def send_message(self, message: str) -> None:
        channel = self.get_channel(channel_id)
        await channel.send(message)

def send(message: str):
    global client
    run(client.send_message(message))
    print("Pray message (" + message + ") send...")


def main():
    global last_send_date, client

    while True:
        # try:
            time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

            if time_ > warn_time and last_send_date != str(date.today()) + "w":
                last_send_date = str(date.today()) + "w"
                send("Hey @everyone, you should go and pray in 5 minues...")

            elif time_ > pray_time and last_send_date != str(date.today()) + "p":
                last_send_date = str(date.today()) + "p"
                send("Hey @everyone, you should go pray...")

            print("Time: " + str(time_))
            print("Pray: " + str(pray_time) + ", Warn: " + str(warn_time))
            sleep(60)

        # except Exception as err:
        #     print("Exception occoured")
        #     with open("log.txt", "a") as file:
        #         file.write(str(err) + "\n")
        #         file.close()

        #    sleep(5)


if __name__ == "__main__":
    global client

    client = CustomClient()
    Thread(target=main).start()
    client.run(bot_token)

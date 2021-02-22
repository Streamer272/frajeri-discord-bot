from datetime import datetime, date
from time import sleep
from sys import argv
import discord

warn_time = 135500
pray_time = 140000
channel_id = 809822474668736583
bot_token = "ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA"

for i in range(len(argv)):
    if "--start-today=" in argv[i]:
        today = "" if argv[i].split("--start-today=")[1] in ("true", "True", "t") else str(date.today())

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
        channel = self.get_channel(channel_id)
        await channel.send(self.message)
        await self.close()

def send(message: str):
    client = CustomClient()
    client.message = message
    client.run(bot_token)
    print("Pray message (" + message + ") send...")


def main():
    global last_send_date
    
    time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

    if time_ > warn_time and last_send_date != str(date.today()):
        send("Hey @everyone, you should go and pray in 5 minues...")

    elif time_ > pray_time and last_send_date != str(date.today()):
        last_send_date = str(date.today())
        send("Hey @everyone, you should go pray...")

    sleep(60)


if __name__ == "__main__":
    print("Bot running...")
    
    while True:
        try:
            main()
        except Exception as err:
            with open("log.txt", "a") as file:
                file.write(str(err) + "\n")
                file.close()

from datetime import datetime, date
from time import sleep
from sys import argv
import discord

today = str(date.today())

try:
    if argv[1].split("--start-today=")[1] in ("true", "True", "t"):
       today = ""
except:
    pass

last_send_date = today

class CustomClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(809822474668736583)
        await channel.send("Hey @everyone, you should go and pray in 5 minues...")
        await self.close()

def send():
    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")
    print("Pray message send...")


if __name__ == "__main__":
    print("Bot running...")
    while True:
        time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

        if time_ > 135500 and last_send_date != str(date.today()):
            last_send_date = str(date.today())
            send()

        del time_
        sleep(60)

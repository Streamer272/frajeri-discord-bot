import discord
import datetime
import time

last_send_date = str(datetime.date.today())


class CustomClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(809822474668736583)
        await channel.send("Hey @everyone its time to pray")
        exit()


if __name__ == "__main__":
    print("Bot running...")
    while True:
        while True:
            time_ = int(str(datetime.datetime.now().strftime("%H:%M:%S")).replace(":", ""))
            if time_ > 140000 and last_send_date != str(datetime.date.today()):
                last_send_date = str(datetime.date.today())
                break
            time.sleep(1)

        client = CustomClient()
        client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")

import discord
import datetime
import time


class CustomClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(806802497226145802)
        await channel.send("Hey @everyone its time to pray")


if __name__ == "__main__":
    while True:
        time_ = int(str(datetime.datetime.now().strftime("%H:%M:%S")).replace(":", ""))
        if time_ > 140000:
            break
        time.sleep(1)

    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")

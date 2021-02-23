from time import sleep
import os
import discord


class CustomClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()

        channel = self.get_channel(809822474668736583)
        sleep(1)

        await channel.send("Hey @everyone, you should go and pray in 5 minues...")

        os._exit(1)


if __name__ == "__main__":
    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")
    print("Pray message send...")

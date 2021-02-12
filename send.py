import discord


class CustomClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(809822474668736583)
        await channel.send("Hey @everyone its time to pray")
        await self.close()


def send():
    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")
    print("Pray message send...")


if __name__ == "__main__":
    pass

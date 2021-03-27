"""
used as reminder (sends message every day)
"""

from sys import argv
from datetime import datetime, date
from asyncio import sleep
import discord

argv.pop(0)  # we dont want the "main.py" arg here
last_send_date = str(date.today())
pray_time = 135500

for i in range(len(argv)):
    if "--set-starttoday" in argv[i]:
        last_send_date = "" if argv[i].replace("--set-starttoday=", "").lower() in (
            "true", "t", "yes", "y", "1") else str(date.today())

    elif "--set-praytime" in argv[i]:
        try:
            pray_time = int(argv[i].replace("--set-praytime=", ""))
        except:
            raise TypeError


def write_log(message: str) -> None:
    """
    writes message in to log.txt
    :param message: message you want to write
    """

    file = open("log-" + str(date.today()) + ".txt", "a")
    file.write(str(datetime.now().strftime("%H:%M:%S")) + ": " + str(message) + "\n")


class CustomClient(discord.Client):
    """
    custom client for discord bot
    """

    async def on_ready(self):
        """
        runs when bot is ready
        """

        global last_send_date, pray_time

        await self.wait_until_ready()

        channel = self.get_channel(809822474668736583)

        await sleep(1)

        while True:
            try:
                time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

                if time_ > pray_time and last_send_date != str(date.today()):
                    print("Sending message...")
                    last_send_date = str(date.today())

                    await channel.send("Hey @everyone, you should go pray in 5 minutes...")
                    write_log("Pray message sent...")

            except Exception as err:
                print("Error occurred...")
                write_log("Error: " + str(err))

            await sleep(60)


if __name__ == "__main__":
    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")

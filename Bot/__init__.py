"""
discord bot
"""

from datetime import datetime, date
from asyncio import sleep
from typing import List

from Console import Console
from RunController import RunController

import discord


class BotNotRunningException(Exception):
    """
    error that occurs when bot is not running
    """

    def __init__(self):
        super().__init__("Bot is not running...")


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

        Console.print_message("Bot running...")

        while True:
            try:
                if open("run", "r").read() != "true":
                    raise BotNotRunningException

                time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

                if time_ > pray_time and last_send_date != str(date.today()):
                    Console.print_message("Sending message...")
                    last_send_date = str(date.today())

                    await channel.send(RunController.get_config_setting("pray_message"))
                    Console.write_log("Pray message sent...")

            except BotNotRunningException:
                pass

            except Exception as err:
                Console.print_error("Error occurred...")
                Console.write_log("Error: " + str(err))

            await sleep(60)


def run(argv: List[str]):
    """
    runs discord bot
    :param argv: args inserted in console
    """

    global last_send_date, pray_time

    last_send_date = str(date.today())
    pray_time = RunController.get_config_setting("pray_time")

    run_file = open("run", "w")
    run_file.write("true")
    run_file.close()

    for i in range(len(argv)):
        if "--set-starttoday" in argv[i]:
            last_send_date = "" if argv[i].replace("--set-starttoday=", "").lower() in (
                "true", "t", "yes", "y", "1") else str(date.today())

        elif "--set-praytime" in argv[i]:
            try:
                pray_time = int(argv[i].replace("--set-praytime=", ""))
            except:
                raise TypeError

    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")


if __name__ == "__main__":
    run([])

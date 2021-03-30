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

        await self.wait_until_ready()

        channel = self.get_channel(809822474668736583)

        await sleep(1)

        Console.print_message("Bot running...")

        while True:
            try:
                if open("run", "r").read() != "true":
                    raise BotNotRunningException

                time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

                # noinspection PyTypeChecker
                if time_ > RunController.get_run_setting("pray_time") and RunController.get_run_setting("last_send_date") != str(date.today()):
                    Console.print_message("Sending message...")
                    RunController.set_run_setting("last_send_date", str(date.today()))

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

    start_today = False

    for i in range(len(argv)):
        if "--Sst" in argv[i]:
            start_today = argv[i + 1] in ("true", "t", "yes", "y", "1")

    RunController.init_run_file(start_today)

    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")


if __name__ == "__main__":
    run([])

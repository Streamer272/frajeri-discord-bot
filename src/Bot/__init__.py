"""
discord bot
"""

from datetime import datetime, date
from asyncio import sleep
from typing import List, Optional

from src.Bot.Console import Console
from src.Bot.RunController import RunController

import discord


class BotNotRunningError(Exception):
    """
    error that occurs when bot is not running
    """

    def __init__(self):
        super().__init__("Bot is not running...")


class ConfigError(Exception):
    """
    error that occurs when there is missing configuration
    """

    def __init__(self, config_error: Exception = Exception("unknown")):
        super().__init__("Configuration error: " + str(config_error) + "...")


class CustomClient(discord.Client):
    """
    custom client for discord bot
    """

    async def on_ready(self):
        """
        runs when bot is ready
        """

        await self.wait_until_ready()

        Console.print_message("Bot running...")

        while True:
            try:
                if not RunController.get_run_setting("active"):
                    raise BotNotRunningError

                try:
                    server: Optional[dict]
                    for server in RunController.get_configuration("servers"):
                        channel = self.get_channel(server["id"])

                        time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))

                        if time_ > server["pray_time"] and RunController.get_run_setting("last_send_date") != str(
                                date.today()):
                            Console.print_message("Sending message...")
                            RunController.set_run_setting("last_send_date", str(date.today()))

                            await channel.send(server["pray_message"])
                            RunController.add_log("Pray message sent...")

                except Exception as err:
                    raise ConfigError(err)

            except BotNotRunningError:
                pass

            except Exception as err:
                Console.print_error("Error occurred...")
                RunController.add_log("Error: " + str(err))

            await sleep(60)


def to_bool(string: str) -> bool:
    """
    returns bool out of string
    :param string: string you want to get bool from
    :return: bool type of string
    """

    return string.lower() in ("true", "t", "yes", "y", "1", "")


def run(argv: List[str]) -> None:
    """
    runs discord bot
    :param argv: args inserted in console
    """

    start_today = False

    for i in range(len(argv)):
        if "--Sst" == argv[i]:
            start_today = to_bool(argv[i + 1])

    RunController.init_run_file(start_today)

    client = CustomClient()
    client.run("ODA5ODE2OTcxNTMyODI4Nzgy.YCam0w.cYBBRIwM2ZWnuEOoJrCfLj6nWaA")


if __name__ == "__main__":
    run([])

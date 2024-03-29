"""
discord bot
"""

from datetime import datetime, date
from asyncio import sleep
from colorama import Fore, Style
from typing import List, Optional

from Bot.Console import Console
from Bot.RunController import RunController

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

    # TODO: add temp measuring

    async def on_ready(self):
        """
        runs when bot is ready
        """

        await self.wait_until_ready()

        Console.print_message("Bot running...")

        # TODO: rework this loop cuz its thrash:

        while True:
            try:
                if not RunController.get_run_setting("active"):
                    raise BotNotRunningError

                temp_config = RunController.get_configuration("run").get("temp_config")
                if temp_config:
                    if RunController.get_temp() > temp_config.get("temp_level"):
                        channel = self.get_channel(temp_config.get("channel"))

                        await channel.send(temp_config.get("message").replace("<temp>", RunController.get_temp()))

                try:
                    server: Optional[dict]
                    for server in RunController.get_configuration("servers"):
                        channel = self.get_channel(server["id"])

                        time_ = int(str(datetime.now().strftime("%H:%M:%S")).replace(":", ""))
                        last_send_date = RunController.get_run_setting("last_send_date")

                        if time_ > server["pray_time"] and (last_send_date.get(server["name"])) != str(
                                date.today()):
                            Console.print_message("Sending message to server " + server["name"] + "...")
                            last_send_date[server["name"]] = str(date.today())
                            RunController.set_run_setting("last_send_date", last_send_date)

                            await channel.send(server["pray_message"])
                            RunController.add_log("Pray message sent to server " + server["name"] + "...")

                except Exception as err:
                    raise ConfigError(err)

            except BotNotRunningError:
                pass

            except Exception as err:
                Console.print_error("Error occurred...")
                RunController.add_log("Error: " + str(err))

            await sleep(60)


def run(argv: List[str]) -> None:
    """
    runs discord bot
    :param argv: args inserted in console
    """

    Console.print_message("Running configuration safe check...")
    RunController.run_configuration_safe_check()
    Console.print_message(f"Configuration safe check: {Fore.RED}OK{Style.RESET_ALL}")

    start_today = False

    for i in range(len(argv)):
        if "--Sst" == argv[i]:
            start_today = argv[i + 1].lower() in ("true", "t", "yes", "y", "1", "")

    RunController.init_run_file(start_today)

    client = CustomClient()
    client.run(RunController.get_configuration("token"))


if __name__ == "__main__":
    run([])

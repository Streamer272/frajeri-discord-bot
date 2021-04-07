"""
controls run file and run setting
"""

from os import mkdir, path
from json import loads, dumps, decoder
from datetime import datetime, date
from time import sleep


class ConfigurationException(Exception):
    """
    :exception: for wrong configuration or errors
    """

    def __init__(self, problem: str) -> None:
        super().__init__("Configuration not valid: " + problem + "...")


class RunController:
    """
    controls run file and settings
    """

    @staticmethod
    def get_configuration(setting: str) -> any:
        """
        returns configuration for requested setting
        :param setting: setting you want configuration for
        :return: configuration for setting
        """

        config = loads(open("config.json", "r").read())
        return config.get(setting)

    @staticmethod
    def run_configuration_safe_check() -> None:
        """
        runs configuration check
        """

        sleep(1)

        try:
            config = loads(open("config.json", "r").read())

        except decoder.JSONDecodeError:
            raise ConfigurationException("JSON can't decode config.json")

        if "token" not in config:
            raise ConfigurationException("Missing bot token")

        for server in (config.get("servers") if config.get("servers") else []):
            needed = ["name", "id", "pray_time", "pray_message"]
            needed_type = [str, int, int, str]

            for need in needed:
                need_type = needed_type[needed.index(need)]

                if need not in server:
                    raise ConfigurationException(f"Missing server configuration \"{need}\" in \"{str(server)}\"")

                if type(server[need]) != need_type:
                    raise ConfigurationException(f"Wrong server configuration in \"{str(server)}\", type of \"{need}\" "
                                                 f"should be \"{str(need_type)}\"")

    @staticmethod
    def init_run_file(start_today: bool = False) -> None:
        """
        creates run file
        """

        with open("run.json", "w") as file:
            run_data = {
                "active": True
            }

            for server in RunController.get_configuration("servers"):
                run_data[server["name"]] = "" if start_today else str(date.today())

            file.write(dumps(run_data))

    @staticmethod
    def get_run_setting(setting: str) -> any:
        """
        returns value for requested setting
        :param setting: setting you want value for
        :return: value for setting
        """

        config = loads(open("run.json", "r").read())
        return config.get(setting)

    @staticmethod
    def set_run_setting(setting: str, value: str) -> None:
        """
        sets setting to value
        :param value: value you want to set setting
        :param setting: setting you want value to set on
        """

        config = loads(open("run.json", "r").read())
        config[setting] = value

        with open("run.json", "w") as file:
            file.write(dumps(config))

    @staticmethod
    def add_log(message: str) -> None:
        """
        writes message in to log.txt
        :param message: message you want to write
        """

        if not path.exists("log"):
            mkdir("log")

        with open("log/log-" + str(date.today()) + ".txt", "a") as file:
            file.write(str(datetime.now().strftime("%H:%M:%S")) + ": " + str(message) + "\n")

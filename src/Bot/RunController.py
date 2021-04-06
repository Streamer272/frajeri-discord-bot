"""
controls run file and run setting
"""

from typing import Optional
from os import mkdir, path
from json import loads, dumps
from datetime import datetime, date


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
    def init_run_file(start_today: bool = False) -> None:
        """
        creates run file
        """

        with open("run.json", "w") as file:
            file.write(dumps({
                "active": True,
                "last_send_date": "" if start_today else str(date.today())
            }))

    @staticmethod
    def get_run_setting(setting: str) -> Optional[str]:
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

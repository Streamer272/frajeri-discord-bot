"""
controls run file and run setting
"""

from typing import Optional
from os import remove
from json import loads, dumps


class RunController:
    """
    controls run file and settings
    """

    @staticmethod
    def get_config_setting(setting: str) -> Optional[str]:
        """
        returns configuration for requested setting
        :param setting: setting you want configuration for
        :return: configuration for setting
        """

        config = loads(open("config.json", "r").read())
        return config.get(setting)

    # @staticmethod
    # def set_config_setting(setting: str, value: str) -> None:
    #     """
    #     sets setting to value
    #     :param value: value you want to set setting
    #     :param setting: setting you want value to set on
    #     """
    #
    #     config = loads(open("config.json", "r").read())
    #     config[setting] = value
    #
    #     with open("config.json", "w") as file:
    #         file.write(config)

    @staticmethod
    def init_run_file() -> None:
        """
        creates run file
        """

        with open("run.json", "w") as file:
            file.write(dumps({
                "active": True
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
            file.write(config)

    @staticmethod
    def delete_run_file() -> None:
        """
        deletes run file
        """

        remove("run.json")

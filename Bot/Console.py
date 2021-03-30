"""
console controller
"""

from datetime import datetime, date
from colorama import Fore, Style


class Console:
    """
    console controller
    """

    @staticmethod
    def print_message(message: str) -> None:
        """
        prints string in console
        :param message: message you want to print
        """

        print(f"{Fore.CYAN}[BOT]{Style.RESET_ALL} {message}")

    @staticmethod
    def print_error(error: str):
        """
        prints error in console
        :param error: error you want to print
        """

        print(f"{Fore.YELLOW}[BOT]{Style.RESET_ALL} {error}")

    @staticmethod
    def write_log(message: str) -> None:
        """
        writes message in to log.txt
        :param message: message you want to write
        """

        file = open("log-" + str(date.today()) + ".txt", "a")
        file.write(str(datetime.now().strftime("%H:%M:%S")) + ": " + str(message) + "\n")

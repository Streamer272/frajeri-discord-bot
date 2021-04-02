"""
console controller
"""

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
    def print_error(error: any):
        """
        prints error in console
        :param error: error you want to print
        """

        print(f"{Fore.YELLOW}[BOT]{Style.RESET_ALL} {str(error)}")

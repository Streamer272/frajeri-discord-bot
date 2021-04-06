"""
used as reminder (sends message every day)
"""

from sys import argv
from threading import Thread

from Bot import run as run_bot
from src.Bot import RunController
from Server import run as run_server


argv.pop(0)  # we dont want the "main.py" argument here

if __name__ == '__main__':
    if RunController.get_configuration("run").get("server"):
        Thread(target=run_server).start()

    if RunController.get_configuration("run").get("bot"):
        run_bot(argv)

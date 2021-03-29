"""
used as reminder (sends message every day)
"""

from sys import argv
from threading import Thread

from discord_bot import run as run_bot
from flask_server import run as run_server


argv.pop(0)  # we dont want the "main.py" arg here

if __name__ == '__main__':
    Thread(target=run_server).start()
    run_bot(argv)

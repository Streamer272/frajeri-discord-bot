"""
flask server for discord bot
"""

from flask import Flask, render_template, make_response, request
from json import loads, dumps


def run():
    """
    starts flask server
    """
    app = Flask(__name__)

    @app.route("/")
    def mapping_():
        """
        mapping for main page
        """
        return render_template("index.html")

    app.run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    run()

"""
flask server for discord bot
"""

from flask import Flask, render_template, make_response  # , request
from json import loads
# from json import loads, dumps


def run():
    """
    starts flask server
    """

    app = Flask(__name__, template_folder="static/public")

    @app.route("/", methods=["GET"])
    def mapping_():
        """
        mapping for main page
        """

        return render_template("src/Server/static/public/index.html")

    @app.route("/is_bot_running", methods=["GET"])
    def mapping_is_bot_running():
        """
        mapping for bot running
        """

        try:
            return make_response(
                str(loads(open("run.json", "r").read())["active"]).lower(),
                200
            )

        except FileNotFoundError:
            return make_response(
                "false",
                200
            )

    app.run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    run()

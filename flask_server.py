"""
flask server for discord bot
"""

from flask import Flask, render_template, make_response  # , request
# from json import loads, dumps


def run():
    """
    starts flask server
    """
    app = Flask(__name__, template_folder="static")

    @app.route("/", methods=["GET"])
    def mapping_():
        """
        mapping for main page
        """

        return render_template(["index.html"])

    @app.route("/is_bot_running", methods=["GET"])
    def mapping_is_bot_running():
        """
        mapping for bot running
        """

        try:
            return make_response(
                open("run", "r").read(),
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

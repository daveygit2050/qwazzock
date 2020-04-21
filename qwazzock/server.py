from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from qwazzock import Game


def get_socketio_and_app():
    app = Flask(__name__)
    socketio = SocketIO(app)

    game = Game()

    @app.route("/")
    def player_client():
        return render_template("player_client.html")

    @app.route("/admin")
    def admin():
        return render_template("admin.html")

    @app.route("/buzz", methods=["POST"])
    def buzz():
        app.logger.info(f"Recevied buzz from {request.form['name']}")
        game.buzz(player=request.form["name"])
        socketio.emit(
            "buzz_data",
            {"player_in_hotseat": game.player_in_hotseat},
            namespace="/buzz_data_socket",
        )
        return "Buzzed!"

    @socketio.on("connect", namespace="/buzz_data_socket")
    def connect_buzz_data_socket():
        socketio.emit(
            "buzz_data",
            {"player_in_hotseat": game.player_in_hotseat},
            namespace="/buzz_data_socket",
        )

    @socketio.on("pass", namespace="/pass_socket")
    def question_passed_socket():
        game.clear_hotseat()
        socketio.emit(
            "buzz_data",
            {"player_in_hotseat": game.player_in_hotseat},
            namespace="/buzz_data_socket",
        )

    return socketio, app

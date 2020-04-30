from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import emit
from flask_socketio import SocketIO

from qwazzock import logger


def get_socketio_and_app(game):
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins="*")

    # Routes

    @app.route("/")
    def player_client():
        return render_template("player_client.html", page_name="player_client")

    @app.route("/host")
    def host():
        return render_template("host_client.html", page_name="host_client")

    # Sockets

    @socketio.on("connect", namespace="/host_client_socket")
    def host_client_socket_connect():
        update_clients()

    @socketio.on("pass", namespace="/host_client_socket")
    def host_client_socket_pass_event():
        game.clear_hotseat()
        game.locked_out_teams = []
        update_clients()

    @socketio.on("reset", namespace="/host_client_socket")
    def host_client_socket_reset_event():
        game.reset()
        update_clients()

    @socketio.on("right", namespace="/host_client_socket")
    def host_client_socket_right_event():
        game.right_answer()
        update_clients()

    @socketio.on("wrong", namespace="/host_client_socket")
    def host_client_socket_wrong_event():
        game.wrong_answer()
        update_clients()

    @socketio.on("connect", namespace="/player_client_socket")
    def player_client_socket_connect():
        update_clients()

    @socketio.on("buzz", namespace="/player_client_socket")
    def player_client_socket_buzz_event(json):
        logger.info(f"Received buzz from {json['player_name']} of {json['team_name']}.")
        game.update_hotseat(
            player_name=json["player_name"], team_name=json["team_name"]
        )
        update_clients()

    # Helpers

    def update_clients():
        socketio.emit(
            "host_client_data", game.__dict__, namespace="/host_client_socket"
        )
        socketio.emit(
            "player_client_data", game.__dict__, namespace="/player_client_socket"
        )

    return socketio, app

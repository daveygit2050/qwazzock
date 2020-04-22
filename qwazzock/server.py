from flask import Flask
from flask import render_template
from flask import request
from flask_socketio import emit
from flask_socketio import SocketIO


def get_socketio_and_app(game):
    app = Flask(__name__)
    socketio = SocketIO(app)

    # Routes

    @app.route("/")
    def player_client():
        return render_template("player_client.html")

    @app.route("/host")
    def host():
        return render_template("host_client.html")

    # Sockets

    @socketio.on("buzz", namespace="/player_client_socket")
    def player_client_socket_buzz_event(json):
        app.logger.info(
            f"Recevied buzz from {json['player_name']} of {json['team_name']}."
        )
        game.update_hotseat(
            player_name=json["player_name"], team_name=json["team_name"]
        )
        update_host_client()

    @socketio.on("connect", namespace="/host_client_socket")
    def host_client_socket_connect():
        update_host_client()

    @socketio.on("pass", namespace="/host_client_socket")
    def host_client_socket_pass_event():
        game.clear_hotseat()
        update_host_client()

    # Helpers

    def update_host_client():
        socketio.emit(
            "host_client_data", game.__dict__, namespace="/host_client_socket"
        )

    return socketio, app

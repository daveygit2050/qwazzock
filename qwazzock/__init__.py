from qwazzock.game import Game
from qwazzock.server import get_socketio_and_app


if __name__ == "__main__":
    socketio, app = get_socketio_and_app()
    socketio.run(app, host="0.0.0.0", ssl_context=("cert.pem", "key.pem"))

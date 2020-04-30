import os

from qwazzock.game import Game
from qwazzock.logs import logger
from qwazzock.server import get_socketio_and_app


def run():
    socketio, app = get_socketio_and_app(game=Game())
    debug_mode = True if os.getenv("QWAZZOCK_SOCKETIO_DEBUG_MODE") else False
    socketio.run(app, debug=debug_mode, host="0.0.0.0")


if __name__ == "__main__":
    run()

import os

from qwazzock.logs import logger  # noreorder
from qwazzock.game import Game
from qwazzock.server import get_socketio_and_app


def run():
    game = Game(content_path=os.getenv("QWAZZOCK_CONTENT_PATH"))
    logger.info(f"Content path set to {game.content_path}.")
    socketio, app = get_socketio_and_app(game=game)
    debug_mode = True if os.getenv("QWAZZOCK_SOCKETIO_DEBUG_MODE") else False
    socketio.run(app, debug=debug_mode, host="0.0.0.0")


if __name__ == "__main__":
    run()

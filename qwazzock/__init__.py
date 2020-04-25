import logging

from qwazzock.game import Game
from qwazzock.server import get_socketio_and_app


def configure_logging(log_level="info"):
    # fmt: off
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    # fmt: on
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    lib_logger = logging.getLogger("qwazzock")
    lib_logger.setLevel(log_level.upper())
    lib_logger.addHandler(handler)
    lib_logger.debug("Logging configured")


def run():
    configure_logging()
    socketio, app = get_socketio_and_app(game=Game())
    socketio.run(app, host="0.0.0.0", ssl_context=("cert.pem", "key.pem"))


if __name__ == "__main__":
    run()

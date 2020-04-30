import logging
import os

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger("qwazzock")
logger.setLevel(os.getenv("QWAZZOCK_LOG_LEVEL", "INFO").upper())
logger.addHandler(handler)
logger.debug("Logging configured")

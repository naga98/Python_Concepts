import logging
from pathlib import Path


def get_logger(log_file="library_management.log"):
    logger = logging.getLogger("library_management")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(Path(log_file), encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    return logger
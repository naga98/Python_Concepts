import logging
from datetime import datetime
from pathlib import Path


def get_logger(log_file="banking.log"):
    logger = logging.getLogger("mini_banking")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(Path(log_file), encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    return logger


def timestamp():
    return datetime.now().isoformat(timespec="seconds")
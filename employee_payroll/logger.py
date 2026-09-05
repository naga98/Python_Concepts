import logging
from pathlib import Path


def _get_logger(name, log_file, level):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        handler = logging.FileHandler(Path(log_file), encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
    return logger


def get_payroll_logger(log_file="payroll.log"):
    return _get_logger("employee_payroll.payroll", log_file, logging.INFO)


def get_error_logger(log_file="error.log"):
    return _get_logger("employee_payroll.errors", log_file, logging.ERROR)
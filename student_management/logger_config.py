"""Centralized logging configuration (module 2 of the student_management package)."""

import logging
import os

LOG_FILE = os.path.join(os.getcwd(), "student.log")


def setup_logger():
    """Configure and return the application-wide logger that writes to student.log."""
    logger = logging.getLogger("student_management")
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers if setup_logger() is called more than once.
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

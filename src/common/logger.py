"""
Centralized logging configuration for the Data Warehouse Project.

Responsibilities:
- Configure console logging
- Configure file logging
- Automatically create log directory
- Return reusable logger instance
"""

from pathlib import Path
import sys

from loguru import logger

# -----------------------------------------------------------------------------
# Create logs directory if it doesn't exist
# -----------------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# -----------------------------------------------------------------------------
# Remove default logger
# -----------------------------------------------------------------------------

logger.remove()

# -----------------------------------------------------------------------------
# Console Logger
# -----------------------------------------------------------------------------

logger.add(
    sys.stdout,
    level="INFO",
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
)

# -----------------------------------------------------------------------------
# File Logger
# -----------------------------------------------------------------------------

logger.add(
    LOG_DIR / "application.log",
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)

# -----------------------------------------------------------------------------
# Export Logger
# -----------------------------------------------------------------------------

__all__ = ["logger"]
"""
Time utility functions.
"""

from datetime import UTC, datetime


def utc_now() -> str:
    """
    Return current UTC time as ISO-8601 string.
    """
    return datetime.now(UTC).isoformat()
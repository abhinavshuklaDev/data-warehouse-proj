"""
Base Service

Reusable functionality for all master-data services.
"""

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from src.common.logger import logger
from src.master_data.services.csv_writer import CSVWriter


class BaseService:
    """
    Base class for all master-data services.
    """

    OUTPUT_DIR: str = ""
    FILE_NAME: str = ""

    @classmethod
    def to_dataframe(cls, objects: list) -> pd.DataFrame:
        """
        Convert dataclass objects into a pandas DataFrame.
        """

        logger.info(f"Creating DataFrame for {cls.__name__}")

        return pd.DataFrame(
            [asdict(obj) for obj in objects]
        )

    @classmethod
    def save(cls, dataframe: pd.DataFrame) -> Path:
        """
        Save dataframe to CSV.
        """

        logger.info(
            f"Writing {cls.FILE_NAME}"
        )

        return CSVWriter.write(
            dataframe=dataframe,
            output_dir=cls.OUTPUT_DIR,
            filename=cls.FILE_NAME,
        )
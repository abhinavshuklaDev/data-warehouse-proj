"""
CSV Writer Service

Responsibilities:
- Create output directories if they don't exist
- Write pandas DataFrame to CSV
- Support overwrite and append modes
- Log all operations
"""

from pathlib import Path

import pandas as pd

from src.common.logger import logger


class CSVWriter:
    """
    Utility class for writing DataFrames to CSV files.
    """

    @staticmethod
    def write(
        dataframe: pd.DataFrame,
        output_dir: str,
        filename: str,
        overwrite: bool = True,
    ) -> Path:
        """
        Write a DataFrame to a CSV file.

        Args:
            dataframe: Pandas DataFrame to save.
            output_dir: Directory where the CSV will be stored.
            filename: CSV file name.
            overwrite: If False, append to an existing file.

        Returns:
            Path to the written CSV file.
        """

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / filename

        mode = "w" if overwrite else "a"
        header = overwrite or not file_path.exists()

        try:
            dataframe.to_csv(
                file_path,
                mode=mode,
                header=header,
                index=False,
            )

            logger.success(f"CSV written successfully: {file_path}")

            return file_path

        except Exception as error:
            logger.exception(f"Failed to write CSV: {file_path}")
            raise error
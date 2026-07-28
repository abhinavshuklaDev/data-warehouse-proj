from pathlib import Path

import pandas as pd

from src.master_data.services.csv_writer import CSVWriter


def test_write_csv():

    dataframe = pd.DataFrame(
        {
            "id": [1, 2],
            "name": ["Alice", "Bob"],
        }
    )

    output_file = CSVWriter.write(
        dataframe=dataframe,
        output_dir="data/output/test",
        filename="sample.csv",
    )

    assert isinstance(output_file, Path)

    assert output_file.exists()
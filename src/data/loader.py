"""load and preprocess the data"""

from pathlib import Path

import pandas as pd

from .schema import Schema


def load_data(path: Path) -> pd.DataFrame:
    """loads data from the given path"""

    data = pd.read_csv(path, sep=";", decimal=",")
    data[Schema.INTERNAL_ID] = range(len(data))

    data = column_to_date(data, Schema.EXECUTION_TIMESTAMP)
    data = column_to_date(data, Schema.LAUNCH_TIMESTAMP)

    return data


def column_to_date(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """converts a given column into the datetime format"""

    data_column = data[column].str.slice(stop=-4)
    data_column = pd.to_datetime(data_column, format='%a, %d %b %Y %H:%M:%S', utc=False)\
        .dt.strftime('%a, %d %b %Y %H:%M:%S')
    data_column = pd.to_datetime(data_column)
    data[column] = data_column.dt.to_pydatetime()
    return data

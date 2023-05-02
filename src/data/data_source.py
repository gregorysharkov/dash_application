from dataclasses import dataclass
from datetime import datetime

import pandas as pd


@dataclass
class Source():
    _data: pd.DataFrame

    def sort_by(self, column: str) -> pd.DataFrame:
        """sorts data by a column and adds a sort index column"""

        sorted_data = self._data.sort_values(column, ascending=True)
        sorted_data[f"{column}_sort_index"] = range(len(sorted_data))  #noqa

        return sorted_data

    def get_col(self, column) -> pd.Series:
        """gets a given column of the data"""
        return self._data[column]

    def get_min_max_date(self, column: str) -> tuple[datetime, datetime]:
        """returns min and max datatime for the slider"""

        min_date = self._data[column].min(axis=0)
        max_date = self._data[column].max(axis=0)
        return min_date, max_date

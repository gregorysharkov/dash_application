"""data handling layer"""

from dataclasses import dataclass, field
from datetime import datetime

import pandas as pd

from .schema import Schema

DEFAULT_LABELS = [
    Schema.ID, Schema.ANALYTICS_URL, Schema.BENCHMARK, Schema.DIRECTION,
    Schema.EVENT_ID, Schema.IDENTIFIER, Schema.PURCHASE_AT, Schema.SELL_AT,
    Schema.SYMBOL,
]

@dataclass
class Source():
    """the class is responsible for handling the data source"""
    _data: pd.DataFrame
    text_label_attributes: list[str] = field(default_factory=lambda: DEFAULT_LABELS)  #type: ignore

    def sort_by(self, column: str) -> pd.DataFrame:
        """sorts data by a column and adds a sort index column"""

        sorted_data = self._data.sort_values(column, ascending=True).copy()
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
    
    @property
    def label_attributes(self) -> pd.Series:
        """generates a series that contains text labels to be added to the text"""

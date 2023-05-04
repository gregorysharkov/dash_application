"""data handling layer"""

from __future__ import annotations

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

    def filter_dates(self, min_date: datetime, max_date: datetime) -> Source:
        """filters data by datetime range"""
        data_col = self._data[Schema.EXECUTION_TIMESTAMP].apply(lambda x: pd.Timestamp(x).timestamp())
        condition = (data_col >= min_date.timestamp()) & (data_col <= max_date.timestamp())
        filtered_data = self._data[condition]
        return Source(filtered_data)

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
    
    # @property
    # def label_attributes(self) -> pd.Series:
    #     """generates a series that contains text labels to be added to the text"""

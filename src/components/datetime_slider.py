"""datetime slider used to filter out rows of data"""

from datetime import datetime

import pandas as pd
from dash import Dash, Input, Output, dcc, html

from ..data.data_source import Source
from . import ids


def render_slider(app: Dash, source: Source, column: str) -> html.Div:
    """generates code for the slider"""

    date_column = source.get_col(column)
    min_val = date_column.min().timestamp()
    max_val = date_column.max().timestamp()
    date_range = pd.date_range(min_val, max_val, freq="3T")
    date_strings = date_range.strftime("%Y-%m-%d\n%H:%M").tolist()
    marks = {i: date_strings[i] for i in range(len(date_strings))}
    return html.Div(
        id="date_slider",
        children=[
            html.H6("Select date range:"),
            dcc.RangeSlider(
                id=ids.DATETIME_SLIDER,
                min=min_val,
                max=max_val, #len(date_strings) - 1,
                value=[min_val, max_val],
                marks=marks,
                # value=[0, len(date_strings) - 1],
            ),
        ],
    )

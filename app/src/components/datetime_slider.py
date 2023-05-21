"""datetime slider used to filter out rows of data"""

# from datetime import datetime

import datetime

import pandas as pd
from dash import Dash, dcc, html

from ..data.data_source import Source
from . import ids


def render_slider(_app: Dash, source: Source, column: str) -> html.Div:
    """generates code for the slider"""

    date_column = source.get_col(column)
    min_val = date_column.min().timestamp()
    max_val = date_column.max().timestamp()
    date_range = pd.date_range(date_column.min(), date_column.max(), freq="3T")
    date_strings = date_range.strftime("%Y-%m-%d %H:%M").tolist()
    marks = {}
    for time_string in date_strings:
        parsed_time = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M").timestamp()
        marks[float(parsed_time)] = {"label": time_string}

    return html.Div(
        id="date_slider",
        children=[
            html.H6("Select date range:"),
            dcc.RangeSlider(
                id=ids.DATETIME_SLIDER,
                min=min_val,
                max=max_val,
                value=[min_val, max_val],
                marks=marks,
            ),
        ],
    )
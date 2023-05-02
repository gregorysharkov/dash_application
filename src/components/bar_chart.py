import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.data_source import Source
from ..data.schema import Schema
from . import ids

MEDAL_DATA = px.data.medals_long()


def render_bar_chart(_app: Dash, source: Source, column: str, log_y: bool = False) -> html.Div:
    """
    renders a barchart

    Args:
        app: dash application
        source: data source used to build
        column: name of the column to be ploted

    Returns:
        html div with the object
    """
    data = source.sort_by(column=column)
    print(data.info())
    fig = px.bar(data, x=range(len(data[column])), y=column, hover_data=[Schema.ANALYTICS_URL], log_y=log_y)
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

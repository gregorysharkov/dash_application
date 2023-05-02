import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.data_source import Source
from ..data.schema import Schema
from . import ids

MEDAL_DATA = px.data.medals_long()


def render_bar_chart(app: Dash, source: Source) -> html.Div:
    """renders a barchart"""

    fig = px.bar(source.sort_by(column=Schema.HOLDING_DAYS), x=f"{Schema.HOLDING_DAYS}_sort_index", y=Schema.HOLDING_DAYS, text=Schema.INTERNAL_ID)
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    # return html.Div(id=ids.BAR_CHART)
    
"""barchart containing sorted values"""

from datetime import datetime

import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.data_source import Source
from ..data.schema import Schema
from . import ids

# import pandas as pd
# import plotly.graph_objs as go
MEDAL_DATA = px.data.medals_long()


def render_bar_chart(app: Dash, source: Source, column: str, log_y: bool = False) -> html.Div:
    """
    renders a barchart

    Args:
        app: dash application
        source: data source used to build
        column: name of the column to be ploted

    Returns:
        html div with the object
    """

    @app.callback(
        Output(f"{ids.BAR_CHART}_{column}", "children"),
        [Input(ids.DATETIME_SLIDER, "value")],
)
    def update_barchart(date_range: list[datetime]) -> html.Div:
        """updates barchart by leaving only filtered_values"""
        print(date_range)
        min_date = datetime.fromtimestamp(date_range[0]) # type: ignore
        max_date = datetime.fromtimestamp(date_range[1]) # type: ignore
        data = source.filter_dates(min_date, max_date).sort_by(column=column)
        fig = px.bar(
            data_frame=data,
            x=range(len(data[column])),
            y=column,
            hover_data=[Schema.ANALYTICS_URL], log_y=log_y
        )
        return html.Div(dcc.Graph(figure=fig), id=f"{ids.BAR_CHART}_{column}")

    return html.Div(id=f"{ids.BAR_CHART}_{column}")

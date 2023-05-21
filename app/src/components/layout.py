"""main application layout"""

from dash import Dash, html

from ..data.data_source import Source
from ..data.schema import Schema
from .bar_chart import render_bar_chart
from .datetime_slider import render_slider


def create_main_layout(app: Dash, source: Source) -> html.Div:
    """creates main application layout"""
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            render_slider(app, source, Schema.EXECUTION_TIMESTAMP),
            html.Hr(),
            render_bar_chart(app, source, Schema.HOLDING_DAYS),
            render_bar_chart(app, source, Schema.LOWER),
            render_bar_chart(app, source, Schema.AVERAGE, True),
            render_bar_chart(app, source, Schema.HIGHER),
        ]
    )

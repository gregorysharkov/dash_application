from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render_nation_dropdown(app: Dash) -> html.Div:
    """generates a list of countrues"""
    all_nations = ["China", "South Korea", "Canada"]

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_NATIONS_BUTTON, "n_clicks")
    )
    def select_all_nations(_: int) -> list[str]:
        """selects all nations"""

        return all_nations

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                options=[{"label": nation, "value": nation} for nation in all_nations],
                value=all_nations,
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_NATIONS_BUTTON,
                className="dropdown-button",
                children=["Select all"]
            )
        ]
    )

"""
main entry point
"""
from pathlib import Path

from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP  # noqa

from src.components.layout import create_main_layout
from src.data.data_source import Source
from src.data.loader import load_data

DATA_PATH = Path() / "data" / "test_data.csv"


def main() -> None:
    """application entry point"""

    data = load_data(DATA_PATH)
    source = Source(data)

    app = Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    app.title = "Dash visualization"
    app.layout = create_main_layout(app, source)
    app.run()


if __name__ == '__main__':
    main()

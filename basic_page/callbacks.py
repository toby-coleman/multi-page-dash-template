from random import random

import dash

from app import app


# Any callbacks for the page should go here
@app.callback(
    dash.dependencies.Output(__package__ + "-chart", "figure"),
    [dash.dependencies.Input(__package__ + "-button", "n_clicks")],
)
def button_click(n_update):
    # Plot some random numbers on a chart
    return {
        "data": [
            {
                "x": [2 * random() - 1 for x in range(10)],
                "y": [2 * random() - 1 for y in range(10)],
                "mode": "markers",
                "name": "Demo",
            },
        ],
        "layout": {
            "margin": {"l": 0, "r": 0, "t": 0, "b": 0, "pad": 0},
            "xaxis": {"range": [-1, +1]},
            "yaxis": {"range": [-1, +1]},
        },
    }

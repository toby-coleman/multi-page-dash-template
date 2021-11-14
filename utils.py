def empty_figure(text="No data"):
    return {
        "layout": {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "showlegend": False,
            "xaxis": {
                "range": [0, 1],
                "showgrid": False,
                "zeroline": False,
                "showline": False,
                "ticks": "",
                "showticklabels": False,
            },
            "yaxis": {
                "range": [0, 1],
                "showgrid": False,
                "zeroline": False,
                "showline": False,
                "ticks": "",
                "showticklabels": False,
            },
            "annotations": [
                {
                    "x": 0.5,
                    "y": 0.5,
                    "xref": "x",
                    "yref": "y",
                    "text": text,
                    "showarrow": False,
                }
            ],
        },
    }

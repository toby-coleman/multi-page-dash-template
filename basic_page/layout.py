import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import utils


def layout(params):
    # This function must return a layout for the page
    # Use __package__ as a prefix to each id to make sure they are unique between pages

    # Do something basic as a demo
    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader("Chart demo"),
                            dbc.CardBody(
                                [
                                    dbc.Button(
                                        "Click here to update chart...",
                                        id=__package__ + "-button",
                                        color="primary",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Br(),
                    dbc.Card(
                        [
                            dbc.CardHeader("URL parameters table"),
                            dbc.CardBody(
                                [
                                    html.A(
                                        "Click here for an example",
                                        href="?param1=42&param2=test",
                                    ),
                                    dbc.Table(
                                        html.Tbody(
                                            [html.Tr([html.Td(key), html.Td(value)]) for key, value in params.items()],
                                            id=__package__ + "-table",
                                        ),
                                        bordered=True,
                                        striped=True,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                width=6,
                className="pd-2",
            ),
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader("Some points on a chart"),
                            dbc.CardBody(
                                [
                                    dcc.Graph(
                                        figure=utils.empty_figure(),
                                        id=__package__ + "-chart",
                                        config={"displayModeBar": False},
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
                width=6,
                className="pd-2",
            ),
        ],
        className="mx-5 mt-5",
    )

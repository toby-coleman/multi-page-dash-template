import math

import dash_bootstrap_components as dbc
from dash import dcc, html

from app import config

CARDS_PER_ROW = config.get("cards_per_row", 2)


def layout(params):
    # This function must return a layout for the homepage

    return dbc.Container(
        [
            html.Div(
                [
                    html.H5("Choose a page to view"),
                ],
                className="px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center",
            ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Card(
                                        [
                                            dbc.CardHeader(page.get("name", "")),
                                            dbc.CardBody(
                                                [
                                                    html.P(page.get("description", "")),
                                                    html.A(
                                                        "View",
                                                        href=page.get("path", "/"),
                                                        className="btn btn-block btn-outline-primary",
                                                    ),
                                                ],
                                                className="d-flex flex-column",
                                            ),
                                        ],
                                        className="mb-3 mx-auto",
                                    )
                                ],
                            )
                            for page_id, page in enumerate(config.get("pages", []))
                            if page_id // CARDS_PER_ROW == row_id
                        ],
                        className=f"row-cols-{CARDS_PER_ROW}",
                    )
                    for row_id in range(math.ceil(len(config.get("pages", [])) / CARDS_PER_ROW))
                ]
            ),
        ],
    )


def header(auth=None):
    return [
        dbc.NavbarSimple(
            [
                # Add other menu items here...
                # Logout button (only show if a user is logged in)
                dcc.LogoutButton(
                    logout_url="/custom-auth/logout",
                    className="btn btn-outline-danger",
                    style={"display": "none"} if not auth else {},
                ),
            ],
            brand=config.get("title", ""),
            brand_href="/",
            fluid=True,
            color="dark",
            dark=True,
        ),
    ]


def login():
    return dbc.Col(
        html.Form(
            [
                dbc.Row(
                    [
                        dbc.Label("Username", html_for=__package__ + "username", width="auto"),
                        dbc.Col(
                            dbc.Input(
                                id=__package__ + "-username",
                                placeholder="Enter username",
                                name="username",
                            ),
                            class_name="me-3",
                        ),
                        dbc.Label("Password", html_for=__package__ + "password", width="auto"),
                        dbc.Col(
                            dbc.Input(
                                id=__package__ + "-password",
                                placeholder="Enter password",
                                name="password",
                                type="password",
                            ),
                            class_name="me-3",
                        ),
                        dbc.Col(
                            [
                                dbc.Button(
                                    "Submit",
                                    id=__package__ + "-submit",
                                    className="button btn-primary",
                                    type="submit",
                                ),
                            ]
                        ),
                    ],
                    class_name="g-2",
                ),
            ],
            action="/custom-auth/login",
            method="post",
        ),
        width={"size": 5},
        className="mt-4 mx-auto",
    )

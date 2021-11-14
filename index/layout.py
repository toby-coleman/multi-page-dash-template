import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import config


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
            dbc.CardDeck(
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
                    for page in config.get("pages", [])
                ],
                className="homepage mb-3",
            ),
        ],
    )


def header(auth=None):
    return [
        dbc.NavbarSimple(
            [
                # Add other menu items here...
                # Logout button (only show if a user is logged in)
                dbc.NavItem(
                    dcc.LogoutButton(
                        logout_url="/custom-auth/logout",
                        className="btn btn-outline-danger",
                    ),
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
                dbc.FormGroup(
                    [
                        dbc.Label("Username", html_for=__package__ + "username", width=2),
                        dbc.Col(
                            dbc.Input(
                                id=__package__ + "-username",
                                placeholder="Enter username",
                                name="username",
                            ),
                            width=10,
                        ),
                    ],
                    row=True,
                ),
                dbc.FormGroup(
                    [
                        dbc.Label("Password", html_for=__package__ + "password", width=2),
                        dbc.Col(
                            dbc.Input(
                                id=__package__ + "-password",
                                placeholder="Enter password",
                                name="password",
                                type="password",
                            ),
                            width=10,
                        ),
                    ],
                    row=True,
                ),
                html.Button(
                    "Submit",
                    id=__package__ + "-submit",
                    className="button btn-primary",
                    type="submit",
                ),
            ],
            action="/custom-auth/login",
            method="post",
        ),
        width={"size": 4, "offset": 4},
        className="mt-4 mx-auto",
    )

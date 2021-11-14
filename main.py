from importlib import import_module
from urllib import parse

import dash
import flask_jwt_extended
from dash import dcc, html

import authentication

# Import homepage and authentication package
import index
from app import app, config

# Import packages for each page in the configuration
pages = {page["path"]: import_module(page["package"]) for page in config.get("pages", [])}

# Main layout
app.layout = html.Div(
    [
        # URL bar
        dcc.Location(id="url", refresh=False),
        # Header bar
        html.Div(id="page-header"),
        # Page content
        html.Div(id="page-content"),
    ]
)


# Use the URL to serve specific pages, and pass query parameters
@app.callback(
    [
        dash.dependencies.Output("page-header", "children"),
        dash.dependencies.Output("page-content", "children"),
    ],
    [dash.dependencies.Input("url", "pathname")],
    [dash.dependencies.State("url", "search")],
)
def display_page(url_path, search):
    # Parse key/value parameters contained in the URL path after '?'
    if search:
        params = parse.parse_qs(search[1:])
    else:
        params = {}
    # Load session cookie to see if user is logged in
    if config.get("authenticate"):
        try:
            # Verify JWT token
            flask_jwt_extended.verify_jwt_in_request(optional=True)
        except flask_jwt_extended.exceptions.JWTExtendedException:
            # Failure, so go to login screen
            return [index.header(), index.login()]
        if not authentication.check_cookie():
            # User is not logged in, so go to login screen
            return [index.header(), index.login()]
    # Load the page from the appropriate package
    if url_path and url_path.rstrip("/") in pages.keys():
        return [
            index.header(auth=authentication.check_cookie() if config.get("authenticate") else None),
            pages[url_path.rstrip("/")].layout(params),
        ]
    else:
        # Default to homepage
        return [
            index.header(auth=authentication.check_cookie() if config.get("authenticate") else None),
            index.layout(params),
        ]


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", threaded=True, debug=True, port=8081)

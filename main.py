import json
from importlib import import_module
from urllib import parse

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

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
    session_cookie = flask.request.cookies.get("auth-session")
    if config.get("authenticate"):
        if not session_cookie or not authentication.check_cookie(session_cookie):
            # User is not logged in, so go to login screen
            return [index.header(), index.login()]
    # Load the page from the appropriate package
    if url_path and url_path.rstrip("/") in pages.keys():
        return [
            index.header(auth=session_cookie),
            pages[url_path.rstrip("/")].layout(params),
        ]
    else:
        # Default to homepage
        return [index.header(auth=session_cookie), index.layout(params)]


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", threaded=True, debug=True, port=8080)

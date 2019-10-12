import dash
import dash_core_components as dcc
import dash_html_components as html
from urllib import parse
import json
from importlib import import_module

from app import app, config
# Import homepage and header
import index
import header


# Import packages for each page in the configuration
pages = {
    page['path']: import_module(page['package']) for page in config.get('pages', [])
}

# Main layout
app.layout = html.Div(
    [
        # URL bar
        dcc.Location(id='url', refresh=False),
        # Put any common components here, e.g. navbar
        header.layout(),
        # Page content
        html.Div(id='page-content'),
    ]
)


# Use the URL to serve specific pages, and pass query parameters
@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')],
    [dash.dependencies.State('url', 'search')]
)
def display_page(url_path, search):
    # Parse key/value parameters contained in the URL path after '?'
    if search:
        params = parse.parse_qs(search[1:])
    else:
        params = {}
    # Load the page from the appropriate package
    if url_path and url_path.rstrip('/') in pages.keys():
        return pages[url_path.rstrip('/')].layout(params)
    else:
        # Default to homepage
        return index.layout(params)


if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', threaded=True, debug=True, port=8080)

import json

import dash
import dash_bootstrap_components as dbc

with open("config.json") as f:
    config = json.loads(f.read())


theme = config.get("theme")
css = config.get("external_css", [])
css = [getattr(dbc.themes, theme.upper()), *css] if theme else css


app = dash.Dash(__name__, external_stylesheets=css)
# Set the page title
app.title = config.get("title", "Dash")
# This setting is required for multi-page views
app.config["suppress_callback_exceptions"] = True

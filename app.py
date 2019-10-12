import dash
import json


with open('config.json') as f:
    config = json.loads(f.read())


app = dash.Dash(
    __name__,
    external_stylesheets=config.get('external_css', [])
)
# Set the page title
app.title = config.get('title', 'Dash')
# This setting is required for multi-page views
app.config['suppress_callback_exceptions'] = True

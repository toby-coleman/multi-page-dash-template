import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import config


def layout():
    # Return a navbar to show across the top of every page
    return dbc.Navbar(
        [
            html.A(
                config.get('title', ''),
                href='/',
                className='navbar-brand'
            ),
            # Add other menu items here...
        ],
        color='dark', dark=True
    )

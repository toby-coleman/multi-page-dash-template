import dash_core_components as dcc
import dash_html_components as html


def layout():
    # Return a navbar to show across the top of every page
    return html.Nav(
        [
            html.A(
                'Dash Template Application',
                href='#',
                className='navbar-brand'
            ),
            # Add other menu items here...
        ], className='navbar navbar-dark bg-dark',
    )

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import config


def layout(params):
    # This function must return a layout for the homepage

    return dbc.Container(
        [
            html.Div(
                [
                    html.H5('Choose a page to view'),
                ],
                className='px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center'
            ),
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(page.get('name', '')),
                            dbc.CardBody(
                                [
                                    html.P(page.get('description', '')),
                                    html.A('View', href=page.get('path', '/'), className='btn btn-block btn-outline-primary')
                                ],
                                className='d-flex flex-column'
                            )
                        ],
                        className='mb-3 mx-auto'
                    )
                    for page in config.get('pages', [])
                ],
                className='homepage mb-3'
            )
        ],
    )

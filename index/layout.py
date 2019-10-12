import dash_core_components as dcc
import dash_html_components as html

from app import config


def layout(params):
    # This function must return a layout for the homepage

    return html.Div(
        [
            html.Div(
                [
                    html.H5('Choose a page to view'),
                ],
                className='px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(page.get('name', ''), className='card-header'),
                            html.Div(
                                [
                                    html.P(page.get('description', '')),
                                    html.A('View', href=page.get('path', '/'), className='btn btn-block btn-outline-primary')
                                ],
                                className='card-body d-flex flex-column'
                            )
                        ],
                        className='card mb-3 mx-auto'
                    )
                    for page in config.get('pages', [])
                ],
                className='card-deck homepage mb-3'
            )
        ],
        className='container'
    )

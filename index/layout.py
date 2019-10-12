import dash_core_components as dcc
import dash_html_components as html


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
                            html.Div(html.H5('Test page 1'), className='card-header'),
                            html.Div(
                                [
                                    html.P('Info on page 1'),
                                    html.A('View', href='/page1', className='btn btn-lg btn-block btn-outline-dark mt-auto')
                                ],
                                className='card-body d-flex flex-column'
                            )
                        ],
                        className='card ', style={'min-width': '220px'}
                    ),
                    html.Div(
                        [
                            html.Div(html.H5('Test page 2'), className='card-header'),
                            html.Div(
                                [
                                    html.P('Page 2 doesn\'t exist yet...'),
                                ],
                                className='card-body d-flex flex-column'
                            )
                        ],
                        className='card ', style={'min-width': '220px'}
                    )
                ],
                className='card-deck mb-3 text-center'
            )
        ],
        className='container'
    )

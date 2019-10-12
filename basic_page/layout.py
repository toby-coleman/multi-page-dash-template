import dash_core_components as dcc
import dash_html_components as html

import utils


def layout(params):
    # This function must return a layout for the page
    # Use __package__ as a prefix to each id to make sure they are unique between pages

    # Do something basic as a demo
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div('Chart demo', className='card-header'),
                            html.Div(
                                [
                                    html.Button(
                                        'Click here to update chart...',
                                        id=__package__ + '-button',
                                        className='btn btn-primary'
                                    ),
                                ],
                                className='card-body mx-auto'
                            ),
                        ],
                        className='card'
                    ),
                    html.Br(),
                    html.Div(
                        [
                            html.Div('URL parameters table', className='card-header'),
                            html.Div(
                                [
                                    html.A('Click here for an example', href='?param1=42&param2=test'),
                                    html.Table(
                                        html.Tbody(
                                            [
                                                html.Tr([html.Td(key), html.Td(value)])
                                                for key, value in params.items()
                                            ],
                                            id=__package__ + '-table'
                                        ),
                                        className='table table-striped table-sm'
                                    ),
                                ],
                                className='card-body'
                            ),
                        ],
                        className='card'
                    ),
                ],
                className='col-6 pd-2'
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div('Some points on a chart', className='card-header'),
                            html.Div(
                                [
                                    dcc.Graph(
                                        figure=utils.empty_figure(),
                                        id=__package__ + '-chart',
                                        config={'displayModeBar': False},
                                    )
                                ],
                                className='card-body'
                            ),
                        ],
                        className='card mx-auto'
                    ),                    
                ],
                className='col-6 pd-2'
            ),
        ],
        className='row mx-5 mt-5'
    )

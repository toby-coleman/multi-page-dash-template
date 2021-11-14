# Multi-page Dash Template

This repo contains a basic template for a multi-page [Dash](https://dash.plot.ly/) application. Each page is contained in a separate Python package to allow for easy extension.

It demonstrates:

1.  A Dash application for building interactive chart-based pages;
2.  Integration with [Bootstrap](https://getbootstrap.com/) to improve the page style; and
3.  Use of Dash's [location](https://dash.plot.ly/dash-core-components/location) component to work with the URL path and parameters.

## Installation

To set up and activate a conda environment containing Dash, use:

    conda env create -f environment.yml
    conda activate dash-template

## Run the application locally

Run `python main.py` to launch the application, then navigate to http://0.0.0.0:8080 to view.

## Usage

To use this template as part of a new application you need to:

1.  Edit [header.py](header.py) and the [index](index) package to customise the homepage;
2.  Rename/edit the [basic_page](basic_page) package to add layout and callbacks for your own page;
3.  Create new packages for each additional page that you need;
4.  Edit the `pages` list in [config.json](config.json) to provide configuration for each page, i.e.
    *   The URL path, e.g. `page1`;
    *   The package that contains its layout/callbacks, e.g. [basic_page](basic_page);
    *   The name and description to be displayed on the homepage menu;
5.  If authentication is required, enable it in [config.json](config.json) and then either:
    *   Set an environment variable called `VALID_USERS` with a JSON dictionary of username/password combinations to be accepted, e.g. `{"demo_user": "demo_pass"}` or;
    *   Implement your own authentication logic in [authentication methods](authentication/logic.py): `check_cookie` should check the session cookie for a logged-in user and return `True` only if it is valid;
6.  Customise [style.css](assets/style.css) with any changes to the page style.

## Useful references

1.  [Plotly Dash Documentation](https://dash.plot.ly/).
2.  [Bootstrap CSS Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/).
3.  [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/).
4.  Information on authentication in [Flask](https://medium.com/analytics-vidhya/integrating-cognito-with-flask-e00010866054).

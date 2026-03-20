"""Smoke tests to verify the app initialises correctly."""

import os
import sys

# Ensure the project root is on the path so local packages are importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_app_initialises():
    """The Dash app object should be created without errors."""
    from app import app

    assert app is not None
    assert app.title == "Basic Dash Template"


def test_utils_empty_figure():
    """utils.empty_figure should return a valid figure dict."""
    import utils

    fig = utils.empty_figure()
    assert isinstance(fig, dict)
    assert "layout" in fig


def test_utils_empty_figure_custom_text():
    """utils.empty_figure should accept custom annotation text."""
    import utils

    fig = utils.empty_figure(text="Loading…")
    annotations = fig["layout"]["annotations"]
    assert annotations[0]["text"] == "Loading…"


def test_index_layout_returns_component():
    """index.layout should return a Dash component."""
    import index

    layout = index.layout({})
    assert layout is not None


def test_index_header_returns_list():
    """index.header should return a list containing a navbar."""
    import index

    header = index.header()
    assert isinstance(header, list)
    assert len(header) == 1


def test_basic_page_layout_returns_component():
    """basic_page.layout should return a Dash component."""
    import basic_page

    layout = basic_page.layout({})
    assert layout is not None

import json
import os
import secrets

import flask
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    set_access_cookies,
    unset_access_cookies,
)

from app import app

# A dictionary of valid username: password combinations
VALID_USERS = json.loads(os.environ.get("VALID_USERS", "{}"))
# Secret key for signing JWT tokens
SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_urlsafe(16))

jwt = JWTManager(app.server)
# Only send cookies over HTTPS: set to True for production
app.server.config["JWT_COOKIE_SECURE"] = False
app.server.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.server.config["JWT_COOKIE_CSRF_PROTECT"] = True
# If JWT_COOKIE_CSRF_PROTECT = True the next two settings are required to play nicely with Dash
app.server.config["JWT_ACCESS_CSRF_COOKIE_NAME"] = "_csrf_token"
app.server.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "X-CSRFToken"
app.server.config["JWT_SECRET_KEY"] = SECRET_KEY


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    # Invalid token in auth header
    response = flask.Response(
        response=json.dumps({"message": "Invalid token"}), status=401, mimetype="application/json"
    )
    unset_access_cookies(response)
    return response


# Login route
@app.server.route("/custom-auth/login", methods=["POST"])
def route_login():
    data = flask.request.form
    username = data.get("username")
    password = data.get("password")

    if username not in VALID_USERS or VALID_USERS[username] != password:
        # Invalid username or password, redirect to the homepage
        return flask.redirect("/")

    # Set a cookie with a JWT access token
    access_token = create_access_token(identity=username)

    # Return a redirect with
    response = flask.redirect(flask.request.referrer)
    # Set cookie lifetime to 1 day
    set_access_cookies(response, access_token, max_age=1 * 24 * 3600)

    return response


# Logout route
@app.server.route("/custom-auth/logout", methods=["POST"])
def route_logout():
    # Redirect back to the index and remove the session cookie.
    response = flask.redirect("/")
    unset_access_cookies(response)
    return response


def check_cookie():
    # Return JWT identity
    return get_jwt_identity()

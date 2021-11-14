import dash
import flask

from app import app

# For example code, see https://dash.plot.ly/dash-core-components/logout_button

# Login route
@app.server.route("/custom-auth/login", methods=["POST"])
def route_login():
    data = flask.request.form
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        # Redirect to the homepage
        rep = flask.redirect("/")

    # actual implementation should verify the password.
    # Recommended to only keep a hash in database and use something like
    # bcrypt to encrypt the password and check the hashed results.

    # Return a redirect with
    rep = flask.redirect(flask.request.referrer)

    # Here we just store the given username in a cookie.
    # Actual session cookies should be signed or use a JWT token.
    payload = username
    rep.set_cookie("auth-session", payload, httponly=True)
    return rep


# Logout route
@app.server.route("/custom-auth/logout", methods=["POST"])
def route_logout():
    # Redirect back to the index and remove the session cookie.
    rep = flask.redirect("/")
    rep.set_cookie("auth-session", "", httponly=True, expires=0)
    return rep


# Use this method to check that a cookie is for a valid, logged-in user
def check_cookie(cookie):
    # Need to implement proper checks here, e.g. of JWT token
    return True if cookie else False

import os
import sys
import logging

# https://docs.python.org/3/library/urllib.parse.html
from urllib.parse import urlparse

# Flask
from flask import (
    Flask, request, redirect, url_for, render_template_string,
    make_response
)
# https://flask-login.readthedocs.io/en/latest/
from flask_login import LoginManager, current_user

# https://flask-ldap3-login.readthedocs.io/en/latest/quick_start.html
from flask_ldap3_login.forms import LDAPLoginForm


app = Flask(__name__)

def url_path(url):
    # extract path and query parameters from URL
    o = urlparse(url)
    parts = list(filter(None, [o.path, o.query]))
    return '?'.join(parts)

@app.route('/')
def home():
    # Redirecting users who are not logged in
    if not current_user or current_user.is_anonymous:
        return redirect(url_for('login'))
    
    # if logged
    template = """
    <h1>Welcome: {{ current_user.username }}</h1>
    <h2>{{ current_user.dn }}</h2>
    """
    return render_template_string(template)

@app.route('/login', methods=['GET', 'POST'])
def login():
    target_url = url_path(request.args.get('url', '/'))
    if current_user.is_authenticated:
        return redirect(target_url)
    form = LDAPLoginForm()
    if form.validate_on_submit():
        user = form.user
        # flask_login stores user in session
        login_user(user)
        app.logger.info("Logging in as user '%s'" % user.username)
        app.logger.info("Groups: %s" % user.groups)
        if user.groups:
            identify = {'uisername': user.username, 'groups': user.groups}
        else:
            identify = user.username

        response = make_response(redirect(target_url))
        return response


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(host='localhost', port=5000, debug=True)
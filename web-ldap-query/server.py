import os
import sys

# https://docs.python.org/3/library/urllib.parse.html
from urllib.parse import urlparse

# Flask
from flask import Flask, request, redirect, url_for, render_template_string
# https://flask-login.readthedocs.io/en/latest/
from flask_login import LoginManager, current_user


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    target_url = url_path(request.args.get('url', '/'))
    if current_user.is_authenticated:
        return redirect(target_url)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
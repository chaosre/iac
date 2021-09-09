import os
import sys
import i18n

from urllib.parse import urlparse

from flask import (
    Flask, jsonify, request, flash, render_template, redirect, make_response,
    url_for, render_template_string, get_flashed_messages
)
from flask_login import LoginManager, current_user, login_user, logout_user, UserMixin
from flask_jwt_extended import (
    jwt_optional, create_access_token,
    jwt_refresh_token_required, create_refresh_token, get_csrf_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from flask_ldap3_login import LDAP3LoginManager
from flask_ldap3_login.forms import LDAPLoginForm


app = Flask(__name__)

# https://flask-ldap3-login.readthedocs.io/en/latest/quick_start.html

# Hostname of your LDAP Server
app.config['LDAP_HOST'] = os.environ.get('LDAP_HOST', 'localhost')

# The port number of your LDAP server.
app.config['LDAP_PORT'] = int(os.environ.get('LDAP_PORT', 389))

# Set to True if your server uses SSL
app.config['LDAP_USE_SSL'] = os.environ.get('LDAP_USE_SSL', False)

# Base DN of your directory
app.config['LDAP_BASE_DN'] = os.environ.get(
    'LDAP_BASE_DN', 'dc=example,dc=org')

# Users DN to be prepended to the Base DN
app.config['LDAP_USER_DN'] = os.environ.get('LDAP_USER_DN', 'ou=users')

# Groups DN to be prepended to the Base DN
app.config['LDAP_GROUP_DN'] = os.environ.get('LDAP_GROUP_DN', 'ou=groups')

# Search for groups
app.config['LDAP_SEARCH_FOR_GROUPS'] = os.environ.get(
    'LDAP_SEARCH_FOR_GROUPS', False)
# Specifies what scope to search in when searching for a specific group
app.config['LDAP_GROUP_SEARCH_SCOPE'] = os.environ.get(
     'LDAP_GROUP_SEARCH_SCOPE', 'LEVEL')

# Specifies what object filter to apply when searching for groups.
app.config['LDAP_GROUP_OBJECT_FILTER'] = os.environ.get(
    'LDAP_GROUP_OBJECT_FILTER', '(objectclass=group)')
# Specifies the LDAP attribute where group members are declared.
app.config['LDAP_GROUP_MEMBERS_ATTR'] = os.environ.get(
    'LDAP_GROUP_MEMBERS_ATTR', 'uniqueMember')

# Specifies what scope to search in when searching for a specific user
app.config['LDAP_USER_SEARCH_SCOPE'] = os.environ.get(
    'LDAP_USER_SEARCH_SCOPE', 'LEVEL')

# The RDN attribute for your user schema on LDAP
app.config['LDAP_USER_RDN_ATTR'] = os.environ.get('LDAP_USER_RDN_ATTR', 'cn')

# The Attribute you want users to authenticate to LDAP with.
LDAP_USER_LOGIN_ATTR = os.environ.get('LDAP_USER_LOGIN_ATTR', 'cn')
app.config['LDAP_USER_LOGIN_ATTR'] = LDAP_USER_LOGIN_ATTR

# Default is ldap3.ALL_ATTRIBUTES (*)
app.config['LDAP_GET_USER_ATTRIBUTES'] = os.environ.get(
    'LDAP_GET_USER_ATTRIBUTES', '*')  # app.config['LDAP_USER_LOGIN_ATTR']

# The Username to bind to LDAP with
app.config['LDAP_BIND_USER_DN'] = os.environ.get('LDAP_BIND_USER_DN', None)

# The Password to bind to LDAP with
app.config['LDAP_BIND_USER_PASSWORD'] = os.environ.get(
    'LDAP_BIND_USER_PASSWORD', None)

# Group name attribute in LDAP group response
LDAP_GROUP_NAME_ATTRIBUTE = os.environ.get('LDAP_GROUP_NAME_ATTRIBUTE', 'cn')

# Default is ldap3.ALL_ATTRIBUTES (*)
app.config['LDAP_GET_GROUP_ATTRIBUTES'] = os.environ.get(
    'LDAP_GET_GROUP_ATTRIBUTES', '*')  # LDAP_GROUP_NAME_ATTRIBUTE

# Setup a Flask-Login Manager
login_manager = LoginManager(app)    
# Setup a LDAP3 Login Manager.          
ldap_manager = LDAP3LoginManager(app)

# Create a dictionary to store the users in when they authenticate.
users = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    target_url = url_path(request.args.get('url', '/'))

@app.route('/logout', methods=['GET', 'POST'])
@jwt_optional
def logout():
    target_url = url_path(request.args.get('url', '/'))

# liveness probe endpoint
@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
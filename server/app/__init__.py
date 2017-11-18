""" Startup Flask """
from flask import Flask
from flask_restful import Api
from app.db import DB
from app.model import *
from app.api.user_api import UserApi

# Create Flask Application
APP = Flask(__name__)
API = Api(APP)

TABLES = [User, Friend, Image]
DB.create_tables(TABLES, safe=True)

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@APP.before_request
def _db_connect():
    DB.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@APP.teardown_request
def _db_close(exc):
    if not DB.is_closed():
        DB.close()

API.add_resource(UserApi, "/api/user/")

@APP.route("/isadnanlate")
def is_adnan_late():
    return "yes"

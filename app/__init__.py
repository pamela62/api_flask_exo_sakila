# Importer flask
from flask import Flask, jsonify, abort, request
from flask.helpers import make_response, url_for
#import pour mysql
from flask_mysqldb import MySQL

app = Flask(__name__)

from app import routes

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

app.run(debug=app.config["DEBUG"])
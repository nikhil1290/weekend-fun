from flask import Flask, redirect, request, url_for
from logging.handlers import RotatingFileHandler

import database
import logging
import resource


app = Flask(__name__)


@app.route("/",methods= ["GET"])
def index():
    return "Welcome,"


@app.route("/api/v1/profile/", methods=["GET", "POST"])
@app.route("/api/v1/profile/<int:profile_id>", methods= ["DELETE", "GET"])
def profile(profile_id=None):
    return redirect(url_for("index"))


@app.route("/api/v1/participants/", methods= ["GET","POST", "DELETE"])
@app.route("/api/v1/participants/<int:participant_id>", methods= ["DELETE"])
def participants(participant_id=None):
    return redirect(url_for("index"))


@app.route("/api/v1/expenses/", methods = ["GET", "POST", ])
@app.route("/api/v1/expenses/<int:expense_id>", methods = ["GET", "DELETE"])
def expenses(expense_id=None):
    return redirect(url_for("index"))


@app.route("/api/v1/weekend/", methods=["GET", "POST"])
@app.route("/api/v1/weekend/<int:weekend_id>", methods=["GET", "DELETE"])
def weekend(weekend_id=None):
    return redirect(url_for("index"))



@app.teardown_request
def teardown_request(exception):
    database.remove_session()


def get_application(arguments):
    global app
    for arg in vars(arguments):
        app.config[arg] = getattr(arguments, arg)

    handler = RotatingFileHandler('log', maxBytes=12000, backupCount=0)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.debug = True

    database.configure(app.config["database"])
    return app

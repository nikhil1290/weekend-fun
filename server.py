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
    uri = request.url_root + "api/v1/"

    if request.method == "POST":
        name = request.form["name"]
        number = request.form["number"]
        company= request.form["company"]
        title = request.form["title"]
        address = request.form["address"]
        ok, profile = database.post_profile(name=name, number= number,
                                            company = company, title=title,
                                                address=address)
        if ok:
            database.commit()
            return resource.profile(uri, profile), 201
        return "Resource already exists", 409

    if request.method == "GET" and profile_id:
        ok , profile = database.get_profile(profile_id)
        if ok:
            return resource.profile(uri, profile), 200
        return "No Resource Found", 404

    if request.method == "GET":
        ok , profile = database.get_profile()
        if ok:
            return resource.profile(uri, profile), 200
        return "No Resource Found", 404

    if request.method == "DELETE" and profile_id:
        ok = database.del_profile(profile_id)
        if ok:
            database.commit()
            return "", 200
        return "No Resource Found", 404

    return "Resource Not Found", 404

@app.route("/api/v1/participants/", methods= ["GET","POST", "DELETE"])
@app.route("/api/v1/participants/<int:participant_id>", methods= ["GET","DELETE"])
def participants(participant_id=None):
    uri = request.url_root + "api/v1/"
    if request.method == "POST":
        weekend_id = request.form["weekend_id"]
        profile_id = request.form["profile_id"]
        ok, participants = database.post_participants(weekend_id=weekend_id,
                                                    profile_id=profile_id)
        if ok:
            database.commit()
            return resource.participant(uri, participants), 201
        return "Resource already exists", 409

    if request.args.get('weekend_id'):
        weekend_id = request.args.get('weekend_id')
    else:
        weekend_id = None

    if request.method == "GET" and weekend_id:
        ok , participants = database.get_participants(weekend_id=weekend_id)
        if ok:
            return resource.participant(uri, participants), 200
        return "Resource Not Found", 404

    if request.method == "GET" and participant_id:
        ok , participants = database.get_participants(participant_id=participant_id)
        if ok:
            return resource.participant(uri, participants), 200
        return "Resource Not Found", 404

    if request.method == "GET":
        ok , participants = database.get_participants()
        if ok:
            database.commit()
            return resource.participant(uri, participants), 200
        return "Resource Not Found", 404


    if request.method == "DELETE" and participant_id:
        ok = database.del_participant(participant_id)
        if ok:
            database.commit()
            return "", 200
        return "No resource found", 404

    return "Resource Not Found", 404

@app.route("/api/v1/expenses/", methods = ["GET", "POST", ])
@app.route("/api/v1/expenses/<int:expense_id>", methods = ["GET", "DELETE"])
def expenses(expense_id=None):
    return redirect(url_for("index"))


@app.route("/api/v1/weekend/", methods=["GET", "POST"])
@app.route("/api/v1/weekend/<int:weekend_id>", methods=["GET", "DELETE"])
def weekend(weekend_id=None):
    uri = request.url_root + "api/v1/"

    if request.method == "POST":
        week_of = str(request.form["week_of"])
        place = request.form["place"]
        ok, weekend = database.post_weekend(week_of=week_of, place=place)
        if ok:
            database.commit()
            return resource.weekend(uri, weekend), 201
        return "Resource Already exists", 409

    if request.method == "GET" and weekend_id:
        ok, weekend = database.get_weekend(weekend_id)
        if ok:
            return resource.weekend(uri, weekend), 200
        return "Resource not found", 404

    if request.method == "GET":
        ok , weekend = database.get_weekend()
        if ok:
            return resource.weekend(uri, weekend), 200
        return "Resource not found", 404

    if request.method == "DELETE" and weekend_id:
        ok = database.del_weekend(weekend_id)
        if ok:
            database.commit()
            return "", 200
        return "Resource Not Found", 404

    return "Resource Not Found", 404


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

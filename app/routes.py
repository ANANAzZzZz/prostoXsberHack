from app import app, db
from flask import jsonify, request, session


@app.route("/")
def index():
    return "index page"

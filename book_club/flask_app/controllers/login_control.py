from flask_app import app
# from flask_app.config.myConnection import connect_to_mysql
from flask_app.models.login_model import logins
from flask_bcrypt import Bcrypt
from flask import flash,render_template,redirect,flash,request

@app.route("/login", methods=["POST"])
def login():
    data = {
        "email":request.form["email"]
    }
    return render_template("dashboard.html")
from flask_app import app
# from flask_app.config.myConnection import connect_to_mysql
from flask_app.models.login_models import logins
from flask_bcrypt import Bcrypt


@app.route("/login", methods=["POST"])
def login():
    data = {
        "email":request.form["email"]
    }
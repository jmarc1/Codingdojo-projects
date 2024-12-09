from flask_app import app
from flask_app.models.register_model import register
from flask import render_template,redirect,session,request,flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "passwd":None
    }
    if register.isValid(data,request.form["passwd"]) == True:
        if request.form["passwd"] != request.form["confirm-passwd"]:
            return redirect("/")
        data["passwd"] = bcrypt.generate_password_hash(request.form["passwd"])
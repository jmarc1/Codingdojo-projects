from flask_app import app
from flask_app.controllers import register_control
from flask_app.controllers import login_control
# from flask_app.controllers import dashboard

if __name__ == "__main__":
    app.run(debug=True)
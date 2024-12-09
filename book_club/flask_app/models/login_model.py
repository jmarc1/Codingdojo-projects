#from flask_app.config.myConnection import connect_to_mysql
from flask_app.models.register_model import register
import re

class logins(register):
    def __init__(self,data):
        super().__init__(data)

    def user_by_email(self,data):
        category="login"
        super().isValid(data,category)
            
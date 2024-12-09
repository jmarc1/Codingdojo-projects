# from flask_app.config.myconnection import connect_to_mysql
import re
from flask import flash
REGRED_EMAIL=re."'compile"
class register:
    def __init__(self,data):
        self.first_name= data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.passwd = data["passwd"]
        self.created = data["created_at"]
        self.updated = data["updated_at"]
        
    @classmethod
    def get_users(cls):
        query = """SELECT * FROM users;"""
        data = connect_to_mysql(cls.db).query_db(query)
        return data
    
    @staticmethod
    def isValid(data,passwd):
        valid_Data = True
        if data["first_name"] < 3 or data["last_name"] < 3:
            flash("Your name can not be less than 3 character","register")
            valid_Data =False
            
        if data["first_name"] < 3 or data["last_name"] < 3:
            flash("Your name can not be less than 3 character","register")
            valid_Data =False
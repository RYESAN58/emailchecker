from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Emails:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.email = db_data['Email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.emails = []
    @classmethod
    def save(cls,data):
        query = "INSERT INTO `random_emails`.`emails` (`Email`) VALUES (%(theemail)s);"
        return connectToMySQL('random_emails').query_db( query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Emails"
        results = connectToMySQL('random_emails').query_db(query)
        x = []
        for i in results:
            x.append( cls(i) )
        return x 
    @staticmethod
    def validate_emails(emails):
        is_valid = True
        y = Emails.get_all()
        x = []
        for i in y:
            x.append(i.email)
        if not EMAIL_REGEX.match(emails['theemail']):
            flash('Invalid Email address')
            is_valid = False
        elif emails['theemail'] in x:
            flash('Already Taken!')
            is_valid = False
        else:
            flash("SUCCESSFUL EMAIL!!!")
        return is_valid
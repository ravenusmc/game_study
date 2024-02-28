# This file will handle the connection to the database

# Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
from datetime import datetime

class Connection():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                            password='pass',
                                            host='localhost',
                                            port=3306,
                                            database='game_study')
        self.cursor = self.conn.cursor()
    
    def encrypt_pass(self, post_data):
        password = post_data['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed
    
    # This method will insert a new user into the database.
    def insert(self, post_data, hashed):
        self._SQL = """insert into users
        (firstName, lastName, email, password)
        values
        (%s, %s, %s, %s)"""
        self.cursor.execute(self._SQL, (post_data['firstName'], post_data['lastName'], 
                            post_data['email'], hashed))
        self.conn.commit()
        user_created = True
        return user_created

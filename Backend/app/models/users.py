from .. import db
from flask import current_app
from datetime import datetime
import hashlib

class User(db.Model):

    __tablename__ = 'users'
    
    username = db.Column(db.String(50), nullable = False)
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    email = db.Column(db.String(120), nullable = False)
    phone_number = db.Column(db.String(10), nullable = False)
    Roll_no1 = db.Column(db.String(9), nullable = False)
    Roll_no2 = db.Column(db.String(9), nullable = True)
    event = db.Column(db.String(9), nullable = False)




    

        
    

from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
from flask_bcrypt import Bcrypt
 

bcrypt = Bcrypt()



class User(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    

    def __init__(self, first_name, last_name, email, age, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.set_password(password)

 
   
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def to_dict(self):
        return {
            'db_id': self.db_id,
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'password_hash': self.password_hash
        }
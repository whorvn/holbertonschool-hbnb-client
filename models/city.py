from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
 

class City(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    country_code = db.Column(db.String(20), unique=False, nullable=False)
     


    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code


 
 
    def to_dict(self):
        return {
            'db_id': self.db_id,
            'name': self.name,
            'country_code': self.country_code,
            'id' : self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
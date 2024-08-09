from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
 

class Amenity(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
     


    def __init__(self, name):
        super().__init__()
        self.name = name


 
 
    def to_dict(self):
        return {
            'db_id': self.db_id,
            'name': self.name,
            'id' : self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
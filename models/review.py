from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
 

class Review(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.String(20), unique=False, nullable=False)
    user_id  = db.Column(db.String(20), unique=False, nullable=False)
    rating = db.Column(db.String(20), unique=False, nullable=False)
    comment = db.Column(db.String(20), unique=False, nullable=False)


    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

 
 
    def to_dict(self):
        return {
            'db_id': self.db_id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'id' : self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
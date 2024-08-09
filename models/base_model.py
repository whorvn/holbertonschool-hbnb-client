from datetime import datetime
from .db import db
import uuid
import json

class BaseModel:

    id = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.String(20), default=datetime.now, nullable=False)
    updated_at = db.Column(db.String(20), default=datetime.now, onupdate=datetime.now, nullable=False)


    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())
        
    def save(self):
        self.updated_at = str(datetime.now())

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
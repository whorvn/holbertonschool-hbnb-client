from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
 

class Place(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    description  = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(20), unique=False, nullable=False)
    city_id = db.Column(db.String(20), unique=False, nullable=False)
    latitude = db.Column(db.String(20), unique=False, nullable=False)
    longitude = db.Column(db.String(20), unique=False, nullable=False)
    host_id  = db.Column(db.String(20), unique=False, nullable=False)
    number_of_rooms = db.Column(db.String(20), unique=False, nullable=False)
    number_of_bathrooms = db.Column(db.String(20), unique=False, nullable=False)
    price_per_night = db.Column(db.String(20), unique=False, nullable=False)
    max_guests = db.Column(db.String(20), unique=False, nullable=False)
    amenity_ids  = db.Column(db.String(20), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    country  = db.Column(db.String(20), unique=False, nullable=False)

 
    def __init__(self, name, description, address, city_id, latitude, longitude,  host_id,  number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids, city, country):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.city = city
        self.country = country
        

    def to_dict(self):
        return {
            'db_id': self.db_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenity_ids': self.amenity_ids,
            'city': self.city,
            'country': self.country,
            'id' : self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
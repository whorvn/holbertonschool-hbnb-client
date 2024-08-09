from flask import Blueprint, request, jsonify, render_template, redirect, url_for
 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.place import Place
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS


bcrypt = Bcrypt()



place_controller = Blueprint('place_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()




@place_controller.route("/places" , methods=['POST'])
def place_post():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    city = data.get('city')
    country = data.get('country')
    place = Place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids, city, country)
    dmanager.save(place)
    return "saved"


@place_controller.route("/places", methods=['GET'])
# @jwt_required()
def user_get():
    return dmanager.get_all(Place)



@place_controller.route("/places/<place_id>", methods=['GET'])
def place_getid(place_id):
    return dmanager.get(place_id, Place)
    

@place_controller.route("/places/<place_id>", methods=['DELETE'])
def place_delete(place_id):
    return dmanager.delete(place_id, Place)
    


@place_controller.route("/places/<place_id>", methods=['PUT'])
def place_update(place_id):
    entity = db.session.query(Place).filter_by(id=place_id).first()
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    city = data.get('city')
    country = data.get('country')
    return dmanager.update(entity)
    




@place_controller.route("/place", methods=['GET'])
def place_get():
    return render_template("place.html") 






 

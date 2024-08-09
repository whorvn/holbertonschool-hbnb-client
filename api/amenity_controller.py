from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.amenity import Amenity
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS



amenity_controller = Blueprint('amenity_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()

""""""
#post

@amenity_controller.route("/amenities" , methods=['POST'])
def amenity_post():
    data = request.get_json()
    name = data.get('name')
    amenity = Amenity(name)  
    dmanager.save(amenity)
    return "saved"



@amenity_controller.route("/amenities" , methods=['GET'])
def amenity_get():
    return dmanager.get_all(Amenity)



@amenity_controller.route("/amenities/<amenity_id>", methods=['GET'])
def get_amenity(amenity_id):
    return dmanager.get(amenity_id, Amenity)



@amenity_controller.route("/amenities/<amenity_id>", methods=['DELETE'])
def delete_amenity(amenity_id):
    return dmanager.delete(amenity_id, Amenity)




@amenity_controller.route("/amenities/<amenity_id>", methods=['PUT'])
def update_amenity(amenity_id):
    entity = db.session.query(Amenity).filter_by(id=amenity_id).first()
    data = request.get_json()
    entity.name = data.get('name') 
    return dmanager.update(entity)



















from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.city import City
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS



city_controller = Blueprint('city_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()


@city_controller.route("/countries/<country_code>/cities", methods=['GET'])
def get_cities_by_country(country_code):
    cities = db.session.query(City).filter_by(country_code=country_code).all()
    return jsonify([entity.to_dict() for entity in cities]), 200


@city_controller.route("/cities" , methods=['POST'])
def city_post():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')
    city = City(name, country_code)  
    dmanager.save(city)
    return "saved"

@city_controller.route("/cities" , methods=['GET'])
def city_get():
    return dmanager.get_all(City)


@city_controller.route("/cities/<city_id>", methods=['GET'])
def get_city(city_id):
    return dmanager.get(city_id, City)



@city_controller.route("/cities/<city_id>", methods=['DELETE'])
def delete_city(city_id):
    return dmanager.delete(city_id, City)

@city_controller.route("/cities/<city_id>", methods=['PUT'])
def update_city(city_id):
    entity = db.session.query(City).filter_by(id=city_id).first()
    data = request.get_json()
    entity.country_code = data.get('country_code') 
    entity.name = data.get('name')
    return dmanager.update(entity)



















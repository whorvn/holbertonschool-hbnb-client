from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from models.country import Country
import json

country_controller = Blueprint('country_controller', __name__)
dmanager = DataManager()

@country_controller.route("/countries", methods=['GET'])
def countries():
    with open('country_code.json', 'r') as data:
        dataStore = json.load(data)
    return jsonify(dataStore)


@country_controller.route("/countries/<country_code>", methods=['GET'])
def countries_code(country_code):
    with open('country_code.json', 'r') as data:
        dataStore = json.load(data)
        for country in dataStore:
            if country["alpha-2"].upper() == country_code.upper():
                return jsonify(country)
    return jsonify(country)
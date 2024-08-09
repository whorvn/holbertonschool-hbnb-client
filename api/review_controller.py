from flask import Blueprint, request, jsonify, render_template, redirect, url_for
 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.review import Review
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS


bcrypt = Bcrypt()



review_controller = Blueprint('review_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()

""""""
#post

@review_controller.route("/places/<place_id>/reviews" , methods=['POST'])
#@jwt_required()
def review_post(place_id):
    data = request.get_json()
    comment = data.get('comment')
    rating = data.get('rating')
    rew = Review(place_id, "user_id", rating, comment)  
    dmanager.save(rew)
    return "saved"






@review_controller.route("/places/<place_id>/reviews" , methods=['GET'])
def review_get(place_id):
    return dmanager.get_all(Review)


"""
@review_controller.route("/users/<user_id>/reviews", methods=['GET'])
"""

@review_controller.route("/reviews/<review_id>", methods=['GET'])
def get_review(review_id):
    return dmanager.get(review_id, Review)


@review_controller.route("/reviews/<review_id>", methods=['DELETE'])
def delete_review(review_id):
    return dmanager.delete(review_id, Review)




@review_controller.route("/reviews/<review_id>", methods=['PUT'])
def update_review(review_id):
    entity = db.session.query(Review).filter_by(id=review_id).first()
    data = request.get_json()
    entity.user_id = data.get('user_id') 
    entity.place_id = data.get('place_id') 
    entity.rating = data.get('rating') 
    entity.comment = data.get('comment') 
    return dmanager.update(entity)



















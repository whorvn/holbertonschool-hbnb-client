from flask import Blueprint, request, jsonify, render_template, redirect, url_for
 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.user import User
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS


bcrypt = Bcrypt()



user_controller = Blueprint('user_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()

""""""
#post

@user_controller.route("/users" , methods=['POST'])
def user_post():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')
    email = data.get('email')
    password = data.get('password')
    user = User(first_name, last_name, email, age, password)  
    if '@' not in email:
            return jsonify({'error': 'Invalid email format'}), 400
    dmanager.save(user)
    return "saved"
    



@user_controller.route("/users", methods=['GET'])
def user_get():
    return dmanager.get_all(User)


@user_controller.route("/users/<user_id>", methods=['GET'])
def user_getid(user_id):
    return dmanager.get(user_id, User)

@user_controller.route("/users/<user_id>", methods=['DELETE'])
def deleteid(user_id):
    dmanager.delete(user_id, User)
    return "deleted"

@user_controller.route("/users/<user_id>", methods=['PUT'])
def user_udate(user_id):
    entity = db.session.query(User).filter_by(id=user_id).first()
    data = request.get_json()
    entity.first_name = data.get('first_name')
    entity.last_name = data.get('last_name')
    entity.email = data.get('email') 
    entity.age = data.get('age')
    return dmanager.update(entity)







@user_controller.route('/login', methods=['POST'])
def loginpost():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.email)  # Correctly use 'user.email'
        return jsonify(access_token=access_token), 200
    return 'Wrong username or password', 401


@user_controller.route('/login', methods=['GET'])
def login():
    return render_template("login.html")







@user_controller.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

 
    
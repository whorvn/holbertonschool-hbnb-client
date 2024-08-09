from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models.user import User
from api.user_controller import user_controller
from api.country_controller import country_controller
from api.place_controller import place_controller
from api.review_controller import review_controller
from api.amenity_controller import amenity_controller
from api.city_controller import city_controller
from models.db import db


app = Flask(__name__)
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_SECRET_KEY'] = 'c303282d-f2e6-46ca-a04a-35d3d873712d'  




jwt = JWTManager(app)
bcrypt = Bcrypt(app)
# Creating an SQLAlchemy instance

db.init_app(app)
# Settings for migrations
migrate = Migrate(app, db)
CORS(app) 
bcrypt.init_app(app)
jwt.init_app(app)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')



app.register_blueprint(user_controller)
app.register_blueprint(country_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(city_controller)

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000, debug=True)
   #app.debug = True







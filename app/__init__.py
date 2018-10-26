#this file will initialize our application
#brings together all components
import os
from flask import Flask,Blueprint
from flask_jwt_extended import JWTManager





def create_app(config_name):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'joanN'
    app.config['JWT_SECRET_KEY'] = 'joan'
    jwt = JWTManager(app)
    from .api.v1 import version1 as v1
    app.register_blueprint(v1)
    #app.config.from_object('config')
    # app.config.from_pyfile('config.py')

    # app.config["TESTING"] = True


    return app

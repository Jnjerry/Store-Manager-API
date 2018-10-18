#this file will initialize our application
#brings together all components
import os
from flask import Flask,Blueprint






def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    from .api.v1 import version1 as v1
    app.register_blueprint(v1)
    #app.config.from_object('config')
    # app.config.from_pyfile('config.py')

    # app.config["TESTING"] = True


    return app

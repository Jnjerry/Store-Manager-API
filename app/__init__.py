#this file will initialize our application
#brings together all components
import os
from flask import Flask,Blueprint
from flask_restful import Api


from .api.v1.views.products import product
from .api.v1.views.sales import sale





def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)


    #app.config.from_object('config')
    # app.config.from_pyfile('config.py')

    # app.config["TESTING"] = True
    app.register_blueprint(product)
    app.register_blueprint(sale)
    return app

#this file will initialize our application
#brings together all components
import os
from flask import Flask
from flask_restful import Api
from app.api.v1.views.products import Product,Product_list

from instance.config import app_config




def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    config_name= os.getenv('APP_SETTINGS')
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["TESTING"] = True

    api = Api(app,prefix='/api/v1')

    api.add_resource(Product_list,'/products')
    api.add_resource(Product,'/products/<int:productid>')
    return app

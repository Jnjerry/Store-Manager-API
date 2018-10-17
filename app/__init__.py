#this file will initialize our application
#brings together all components
from flask import Flask
from flask_restful import Api
from app.api.v1.views.products import Product,Product_list

from instance.config import app_config




def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app,prefix='/api/v1')

    api.add_resource(Product_list,'/products')
    api.add_resource(Product,'/products/<int:productid>')
    return app

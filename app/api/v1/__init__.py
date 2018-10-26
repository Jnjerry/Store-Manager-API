from flask_restful import Api
from flask import Blueprint

from .views.products import Product,Product_list
from .views.sales import Sale,Sale_list

version1 = Blueprint('api version1', __name__, url_prefix='/api/v1')

api = Api(version1)


api.add_resource(Product_list,'/products')
api.add_resource(Product,'/products/<int:productid>')
api.add_resource(Sale_list,'/sales')
api.add_resource(Sale,'/sales/<int:saleid>')

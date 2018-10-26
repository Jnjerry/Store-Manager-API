from flask_restful import Api
from flask import Blueprint

from .views.products import Product,Product_list
from .views.sales import Sale,Sale_list
from .views.user_auth import UserSignUp,UserLogin,UserLogout


#version using Blueprint
version1 = Blueprint('api version1', __name__, url_prefix='/api/v1')
api = Api(version1)

#api end points
api.add_resource(Product_list,'/products')
api.add_resource(Product,'/products/<int:productid>')
api.add_resource(Sale_list,'/sales')
api.add_resource(Sale,'/sales/<int:saleid>')
api.add_resource(UserSignUp,'/auth/register')
api.add_resource(UserLogin,'/auth/login')
# api.add_resource(Users,'/users')
api.add_resource(UserLogout,'/auth/logout')

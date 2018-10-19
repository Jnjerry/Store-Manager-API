# from flask_restful import Api
# from flask import Flask,Blueprint
#
# from .views.products import Product,Product_list
# from .views.sales import Sale,sale
# # from .views.authentication_endpoints auth
# version1 = Blueprint('api version1', __name__, url_prefix='/api/v1')
#
# api = Api(version1)
#
# app = Flask(__name__)
#
# api.add_resource(Product_list,'/products')
# api.add_resource(Product,'/products/<int:productid>')
# # api.add_resource(Sale_list,'/sales')
# api.add_resource(Sale,'/sales/<int:saleid>')
#
# app.register_blueprint(sale)
# # app.register_blueprint(auth)

from flask import Flask,Blueprint,jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
from flask_restful import Api,Resource,reqparse
from .models import products

product = Blueprint('product', __name__,url_prefix='/api/v1')


@product.route('/products',methods=['GET'])
def get_product_list():
    response=jsonify(products)
    response.status_code=200
    return response


@product.route('/product/<int:productid>',methods=['GET'])
def get_product_by_id(productid):
        for product in products:
            if(productid==product["productid"]):
                response=jsonify(product)
                response.status_code=200
                return response


#to get a single product
class Product(Resource):
    def get(self,productid):
        for product in products:
            if(productid==product["productid"]):
                return product,200







    def post(self, productid):
        parser = reqparse.RequestParser()
        parser.add_argument("productid")
        parser.add_argument("product_name")
        parser.add_argument("product_price")

        for product in products:
        		if(productid == product["productid"]):
        				return "product with ID number {} already exists".format(productid), 400

        args = parser.parse_args()

        product = {
            "product_name": args["product_name"],
            "product_price": args["product_price"],
            }
        products.append(product)
        return product, 201

from flask import Flask,Blueprint,jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
from flask_restful import Api,Resource,reqparse
from .models import sales

sale = Blueprint('sale', __name__,url_prefix='/api/v1')

@sale.route('/sales',methods=['GET'])
def get_sales_list():
    response=jsonify(sales)
    response.status_code=200
    return response


@sale.route('/sales/<int:saleid>',methods=['GET'])
def get_sale_by_id(saleid):
        for sale in sales:
            if(saleid==sale["saleid"]):
                response=jsonify(sale)
                response.status_code=200
                return response

@sale.route('/sales',methods=['POST'])
def post_sales():
    parser = reqparse.RequestParser()
    parser.add_argument("saleid")
    parser.add_argument("product_name")
    parser.add_argument("product_price")

    for sale in sales:
            if(saleid == sale["saleid"]):
                    return "sale with ID number {} already exists".format(saleid), 400

    args = parser.parse_args()

    sales = {
        "product_name": args["product_name"],
        "product_price": args["product_price"],
        }


    sales.append(sale)
    sales =[ {
        "product_name":"unga",
        "product_price":300,
        },
        {
            "product_name":"chapo",
            "product_price":30,
            }
]
    response=jsonify(sale)
    response.status_code=201
    return response




    # def post(self, saleid):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("productid")
    #     parser.add_argument("product_name")
    #     parser.add_argument("product_price")
    #
    #     for sale in sales:
    #     		if(saleid == sale["saleid"]):
    #     				return "sale with ID number {} already exists".format(saleid), 400
    #
    #     args = parser.parse_args()
    #
    #     product = {
    #         "product_name": args["product_name"],
    #         "product_price": args["product_price"],
    #         }
    #     sales.append(sale)
    #     return sale, 201

from flask import Flask
from flask_restful import Api,Resource,reqparse
from .models import sales




class Sale_list(Resource):
    def get(self):
        return sales,200


#to get a single product
class Sale(Resource):
    def get(self,saleid):
        for sale in sales:
            if(saleid==sale["saleid"]):
                return sale,200

    def post(self, saleid):
        parser = reqparse.RequestParser()
        parser.add_argument("productid")
        parser.add_argument("product_name")
        parser.add_argument("product_price")

        for sale in sales:
        		if(saleid == sale["saleid"]):
        				return "sale with ID number {} already exists".format(saleid), 400

        args = parser.parse_args()

        product = {
            "product_name": args["product_name"],
            "product_price": args["product_price"],
            }
        sales.append(sale)
        return sale, 201

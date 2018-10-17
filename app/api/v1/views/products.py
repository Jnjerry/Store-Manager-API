from flask import Flask
from flask_restful import Api,Resource,reqparse
from .models import products




class Product_list(Resource):
    def get(self):
        products,200


#to get a single product
class Product(Resource):
    def get(self,productid):
        for product in products:
            if(productid==product["productid"]):
                return product,200
                # return "Product {} doesn't exist",404

    

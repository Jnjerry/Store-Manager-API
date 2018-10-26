from flask import Flask
from flask_restful import Api,Resource,reqparse
from .models import products




class Product_list(Resource):
    def get(self):
        return products,200


#to get a single product
class Product(Resource):
    def get(self,productid):
        for product in products:
            if(productid==product["productid"]):
                return product,200

    def post(self,productid):
        parser = reqparse.RequestParser()
        parser.add_argument("productid")
        parser.add_argument("product_name")
        parser.add_argument("product_price")

        args = parser.parse_args()



        product = {
            "productid": productid,
            "product_name": args["product_name"],
            "product_price": args["product_price"],


        }

        products=[

            {
                "productid":1,
                "product_name":"unga",
                "product_price":300,

            },

        {
            "productid":2,
            "product_name":"chapo",
            "product_price":30,

        }



        ]



        products.append(product)


        return product, 201

from flask import Flask, jsonify, make_response
from flask_restful import Resource, reqparse
from ..products_models import Products
from flask_jwt_extended import jwt_required


products = {}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")
parser.add_argument('description', type=str, required=True, help="only strings allowed")

class Product_list(Resource):
	def get(self):
		products = Products.get_all(self)
		if not products:
			return {"message":"No products yet"},400
		return make_response(jsonify(
			{"message":"All products available","products":products,"status":"okay"}),200)
	@jwt_required
	def post(self):
		args = parser.parse_args()
		name = args['name'].strip()
		quantity = args['quantity']
		description = args['description'].strip()

		newproduct = Products(name, quantity, description)
		newproduct.save()
		if name=="":
			return {'Message':'Name cannot be empty'},400
		if quantity=="":
			return {'Message':'Quantity cannot be empty'},400
		if quantity==0:
			return {'Message':'Quantity cannot be 0'},400
		if description=="":
			return {'Message':'Description cannot be empty'},400

		return make_response(jsonify(
			{"message":"product successfully created","products":newproduct.__dict__}), 201)

class Product(Resource):

	def get(self,productid):
		single_product = Products.get_one(self,productid)
		if single_product == "Product not found":
			return make_response(jsonify(
				{"status":"not found"}), 404)
		return make_response(jsonify(
		{"product":single_product,"status":"okay"}), 200)

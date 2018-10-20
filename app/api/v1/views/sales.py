from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required
from .models import Sales


sales = {}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="only integers allowed")
parser.add_argument('description', type=str, required=True, help="only strings allowed")

#all sales list
class Sale_list(Resource):
	@jwt_required
	def get(self):
		"""gets all sales"""
		products = Sales.get_all(self)
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"products":products}),
		200)
	@jwt_required
	def post(self):
		"""posts a sale"""

		args = parser.parse_args()
		name = args['name']
		quantity = args['quantity']
		description = args['description']

		new_sale = Sales(name, quantity, description)
		new_sale.save()

		return make_response(jsonify(
			{"message":"success",
			"status":"created",
			"product":new_sale.__dict__}
			), 201)

class Sale(Resource):
	'''single product API'''
	@jwt_required
	def get(self, saleid):
		one_product = Sales.get_one(self, saleid)

		if one_product == "Product not found":
			return make_response(jsonify(
				{"status":"not found",
				"message":"product unavailbale",
				}), 404)

		return make_response(jsonify(
			{"status":"ok",
			"message":"success",
			"product":one_product}
			), 200)

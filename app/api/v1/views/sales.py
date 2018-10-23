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
		sales = Sales.get_all(self)

		return make_response(jsonify(
			{"sales":sales}),200)
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
			{"sales":new_sale.__dict__}), 201)

class Sale(Resource):
	'''single product API'''
	@jwt_required
	def get(self, saleid):
		"""find a sale by saleid and assign it to one_sale"""
		"""call the get_one method from sale models"""
		one_sale= Sales.get_one(self, saleid)
		return make_response(jsonify(
			{"status":"ok","sale":one_sale}), 200)

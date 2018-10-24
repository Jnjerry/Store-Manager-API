from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import jwt_required
from ..sales_models import Sales


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
		try:
			sales = Sales.get_all(self)
			if not sales:
				return {"message":"No sales made yet"},400


			return make_response(jsonify(
				{"message":"All sales made","sales":sales,"status":"okay"}),200)

		except Exception as xception:
	            print(exception)
	            return {'message': 'Oops,you need authentication to access this page.'}, 500
	@jwt_required
	def post(self):
		"""posts a sale"""

		args = parser.parse_args()
		name = args['name'].strip()
		quantity = args['quantity']
		description = args['description'].strip()

		new_sale = Sales(name, quantity, description)
		new_sale.save()

		return make_response(jsonify(
			{"message":"sale successfully created","sales":new_sale.__dict__}), 201)

class Sale(Resource):
	'''single product API'''
	@jwt_required
	def get(self, saleid):
		"""find a sale by saleid and assign it to one_sale"""
		"""call the get_one method from sale models"""
		one_sale= Sales.get_one(self, saleid)
		return make_response(jsonify(
			{"status":"ok","sale":one_sale}), 200)

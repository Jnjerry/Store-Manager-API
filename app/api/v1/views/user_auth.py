from flask import Flask, jsonify, make_response,session
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..user_models import User


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('password', required=True, help="password cannot be blank")
all_users=[]

class UserSignUp(Resource):

	def post(self):
		"""Register a new user"""
		"""Users input """
		args = parser.parse_args()
		email = args['email'].strip()
		password = args['password'].strip()


		validate_email = User.validate_email(self,email)
		new_user = User.get_one(self, email)

		if email=="" or password =="":
			return {'Message':'Password or email empty'},400

		if not validate_email:
			return {'Message': "Invalid email format"}, 400




		if new_user == "User not found":
			new_user = User(email,password)
			new_user.signup()
			return make_response(jsonify({"message":"User created!","user":new_user.__dict__}), 201)

		else:
		 	return make_response(jsonify({'message':'Email already exist,try another one.'}))

class UserLogin(Resource):
	'''user login class'''

	def post(self):
		args = parser.parse_args()
		email = args['email']
		password = args['password']

		message=User.login(email,password)
		token = create_access_token(identity=args['email'])
		return make_response(jsonify({'message': message, 'token': token}), 201)




class UserLogout(Resource):
	def get(self):
		"""remove user from session"""
		session.pop('username', None)
		return jsonify({"message":"successful logout"})

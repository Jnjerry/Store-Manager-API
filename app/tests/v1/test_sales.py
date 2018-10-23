import unittest
import json
import os
from ... import create_app


class SalesTestCase(unittest.TestCase):
	# method will run before each test case method


	def setUp(self):
		""""define our test variabes and initialize our app"""
		self.client= create_app('testing').test_client()
		self.sales_data = {"name":"books", "quantity":40, "description": "biographies"}


	def register_user(self,email="joan@tester.com", password="@254"):
		user_data = {
			'email': email,
			'password': password
		}
		return self.client.post('/api/v1/auth/register', data=user_data)

	def login_user(self, email="joan@test.com", password="@254"):
		user_data = {
			'email': email,
			'password': password
		}
		return self.client.post('/api/v1/auth/login', data=user_data)


	#test to check if admin or store attendant can get sale list
	def test_sale_list(self):

		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.get('/api/v1/sales',
			headers=dict(Authorization="Bearer " + access_token))
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 200)

	def test_get_one_sale(self):
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['access_token']
		result = self.client.get('/api.v1/sales/{}'.format(results['id']),
			headers=dict(Authorization="Bearer " + access_token))
		# assert that the bucketlist is actually returned given its ID
		self.assertEqual(result.status_code, 200)

	def test_create_sale(self):
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post('/api/v1/sales',
			data=self.sales_data,
			headers=dict(Authorization="Bearer " + access_token))

		self.assertEqual(response.status_code, 201)


	# test for invalid order
	def test_invalid_sales_id(self):
		response=self.client.get("api/v1/sale/900",content_type="application/json")
		self.assertEqual(response.status_code,404)

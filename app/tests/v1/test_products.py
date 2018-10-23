
import unittest
import json
import os
from ... import create_app


class ProductsTestCase(unittest.TestCase):
        def setUp(self):
            self.client= create_app('testing').test_client()
            self.product_data = {"name":"books", "quantity":40, "description": "biographies"}
            self.user = {'email': 'ngugijoan2@gmail.com', 'username': 'Joan', 'password': '@254'}

        def register_user(self,email="", password=""):
            user_data = self.user
            return self.client.post('/api/v1/auth/register', data=user_data)

        def login_user(self, email="", password=""):
            user_data =self.user
            return self.client.post('/api/v1/auth/login', data=user_data)

        #test to check if admin or store attendant can get product list
        def test_product_list(self):
            """send HTTP GET request to the application on specified path"""
            response=self.client.get('api/v1/products',content_type="application/json")
            self.assertEqual(response.status_code,200)

        def test_create_sale(self):
            self.register_user()
            result = self.login_user()
            access_token = json.loads(result.data.decode())['token']

            response = self.client.post('/api/v1/products',
                data=self.product_data,
                headers=dict(Authorization="Bearer " + access_token))

            self.assertEqual(response.status_code, 201)


        def test_get_one_product(self):
            response=self.client.get("api/v1/products/1",content_type="application/json")
            self.assertEqual(response.status_code,200)

        def test_invalid_product_id(self):
            response=self.client.get("api/v1/sale/900",content_type="application/json")
            self.assertEqual(response.status_code,404)

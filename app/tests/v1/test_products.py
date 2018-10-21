
import unittest
import json
import os
from ... import create_app


class ProductsTestCase(unittest.TestCase):
        def setUp(self):
            """"define our test variabes and initialize our app"""
            self.client= create_app('testing').test_client()
            self.sales_data = {"name":"books", "quantity":40, "description": "biographies"}


        def register_user(self,email="joan@tester.com", password="@254"):
            user_data = {
                'email': email,
                'password': password
            }
            return self.client.post('/auth/register_user', data=user_data)

        def login_user(self, email="joan@test.com", password="@254"):
            user_data = {
                'email': email,
                'password': password
            }
            return self.client.post('/auth/login_user', data=user_data)



        #test to check if admin or store attendant can get product list
        def test_product_list(self):
            """send HTTP GET request to the application on specified path"""
            response=self.client.get('api/v1/products',content_type="application/json")
            self.assertEqual(response.status_code,200)

        def test_create_product(self):
            data = {"product_name": "book","product_price": 50}
            response = self.client.post("/api/v1/products/30",data=json.dumps(data),content_type="application/json")
            self.assertEqual(response.status_code,201)


        def test_get_one_product(self):
            response=self.client.get("api/v1/products/1",content_type="application/json")
            self.assertEqual(response.status_code,200)

        def test_invalid_product_id(self):
            response=self.client.get("api/v1/sale/900",content_type="application/json")
            self.assertEqual(response.status_code,404)
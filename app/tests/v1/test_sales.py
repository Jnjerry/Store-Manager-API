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


    def register_user(self,email="joan@tester.com", username="username",password="@254"):
        user_data = {
            'email': email,
            'username':username,
            'password': password
        }
        return self.client.post('api/v1/auth/register', data=user_data)

    def login_user(self, email="joan@test.com", password="@254"):
        user_data = {
            'email': email,
            'password': password
        }
        return self.client.post('api/v1/auth/login', data=user_data)


    #test to check if admin or store attendant can get sale list
    def test_sale_list(self):

        self.register_user()
        result = self.login_user()
        access_token = json.loads(result.data.decode())['token']

        response = self.client.get('/api/v1/sales',
        	headers=dict(Authorization="Bearer " + access_token))
        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["message"], "success")

    def test_get_one_sale(self):
        self.register_user()
        result = self.login_user()
        access_token = json.loads(result.data.decode())['token']
        retrieve = self.client.post('/api/v1/sales/',headers=dict(Authorization="Bearer " + access_token),
            data=self.sales_data)
        self.assertEqual(retrieve.status_code, 201)
        # get the response data in json format
        results = json.loads(response.data.decode())
        result = self.client.get('/api.v1/sales/{}'.format(results['id']),
            headers=dict(Authorization="Bearer " + access_token))
        # assert that the bucketlist is actually returned given its ID
        self.assertEqual(result.status_code, 200)

    def test_sale_creation(self):
        """Tests whether our API can create a sale record"""
        response = self.client.post('/api/v1/sales',
                                 data=json.dumps(self.sales_data),
                                 content_type="application/json",
                                 headers={"x-access-token":token})
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Sale", response_msg["Message"])



    # test for invalid order
    def test_invalid_sales_id(self):
        response=self.client.get("api/v1/sale/900",content_type="application/json")
        self.assertEqual(response.status_code,404)

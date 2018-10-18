import unittest
import json
import os
from app import create_app
from instance.config import app_config

class SalesTestCase(unittest.TestCase):
    # method will run before each test case method
    def setUp(self):
        """"define our test variabes and initialize our app"""
        self.app = create_app(config="testing")
        self.client=self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    #test to check if admin or store attendant can get sales list
    def test_sales_list(self):
        """send HTTP GET request to the application on specified path"""
        response=self.client.get('api/v1/products',content_type="application/json")
        self.assertEqual(response.status_code,200)

    #
    # def test_create_product(self):
    #     payload = {'product_name': 'book', 'Product_price': 30}
    #     response=self.client.post('api/v1/products/2',content_type="application/json",data=json.dumps(payload))
    #     self.assertEqual(response.status_code, 201)

    def test_get_one_product(self):
        response=self.client.get("api/v1/products/1",content_type="application/json")
        self.assertEqual(response.status_code,200)




if __name__ == '__main__':
    unittest.main()

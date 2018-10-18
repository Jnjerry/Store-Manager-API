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

    #test to check if admin or store attendant can get sale list
    def test_sale_list(self):
        """send HTTP GET request to the application on specified path"""
        response=self.client.get('api/v1/sales',content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_get_one_sale(self):
        response=self.client.get("api/v1/sales/1",content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_create_sale(self):
        data = {"product_name": "book","product_price": 50}
        response = self.client.post("/api/v1/sales/30",data=json.dumps(data),content_type="application/json")
        self.assertEqual(response.status_code,201)

    # test for invalid order
    def test_invalid_sales_id(self):
        response=self.client.get("api/v1/sale/900",content_type="application/json")
        self.assertEqual(response.status_code,404)









if __name__ == '__main__':
    unittest.main()

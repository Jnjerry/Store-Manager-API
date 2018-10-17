import unittest
import json
import os
from app import create_app
from instance.config import app_config

class ProductsTestCase(unittest.TestCase):
    # method will run before each test case method
    def setUp(self):
        """"define our test variabes and initialize our app"""
        self.app = create_app(config="testing")
        self.client=self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    #test to check if admin or store attendant can get product list
    def test_product_list(self):
        """send HTTP GET request to the application on specified path"""
        response=self.client.get('api/v1/products',content_type="application/json")
        self.assertEqual(response.status_code,200)

    # def test_nonexistent_id(self):
    #     response = self.client.get('/api/v1/products/1000', content_type="application/json")
    #     self.assertEqual(response.status_code,404)


    def test_get_one_product(self):
        response=self.client.get("api/v1/products/1",content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_required_productvalue_missing(self):
        payload={'product_name':'book'}
        response = self.client.post('/api/v1/products',data= json.dumps(payload),content_type="application/json")
        self.assertEqual(response.status_code,404)







if __name__ == '__main__':
    unittest.main()

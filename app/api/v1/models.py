import random


class Products:
	products = {}

	productid = 1

	def __init__(self, name, quantity, description):
		self.productid =len(Products.products) + 1
		self.name = name
		self.quantity = quantity
		self.description = description



	def save(self):
		payload = dict(
			productid = self.productid,
			name = self.name,
			quantity = self.quantity,
			description = self.description
			)

		self.products.update({self.productid:payload})

	def get_all(self):
		return Products.products

	def get_one(self, productid):

		for key in Products.products:
			if key == productid:
				return Products.products[key]

		return "product not found"


class Sales:
	sales = {}

	saleid = 1

	def __init__(self, name, quantity, description):
		self.saleid =len(Sales.sales) + 1
		self.name = name
		self.quantity = quantity
		self.description = description


	def save(self):
		payload = dict(
			saleid = self.saleid,
			name = self.name,
			description = self.description,
		    quantity=self.quantity
			)

		self.sales.update({self.saleid:payload})

	def get_all(self):
		return Sales.sales

	def get_one(self, saleid):

		for sale in Sales.sales:
			if sale == saleid:
				return Sales.sales[sale]
		message = "sale not found"
		return message

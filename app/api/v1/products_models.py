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

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
    

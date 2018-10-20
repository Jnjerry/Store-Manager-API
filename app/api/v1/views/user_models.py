class User:
	'''Class represents operations related to products'''
	all_users = {}

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password


	def signup(self):
		payload = dict(
			email = self.email,
			username = self.username,
			password = self.password
			)

		self.all_users.update({self.email:payload})


	def get_one(self, email):

		for user in User.all_users:
			if user == email:
				return User.all_users[user]
		message = "User not found"
		return message

	def get_all(self,email):
		return User.all_users

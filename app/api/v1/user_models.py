import re
class User:

	all_users = {}

	def __init__(self, email, password):
		self.email = email
		self.password = password


	def signup(self):
		payload = dict(
			email = self.email,
			password = self.password
			)

		self.all_users.update({self.email:payload})


	def get_one(self, email):

		for key in User.all_users:
			if key == email:
				return User.all_users[key]
		message = "User not found"
		return message
	



	def validate_email(self,email):
		if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
			return True
		return False

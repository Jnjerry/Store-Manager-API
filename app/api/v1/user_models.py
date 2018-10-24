import re
class User:

	all_users = []

	def __init__(self, email, password):
		self.email = email
		self.password = password


	def signup(self):
		payload = dict(
			email = self.email,
			password = self.password
			)

		User.all_users.append(payload)


	def get_one(self, email):

		for key in User.all_users:
			if key.get("email")==email:
				return email
		message = "User not found"
		return message

	@classmethod
	def login(cls,email,password):
		for user in cls.all_users:
			if  user["email"]==email and user["password"]==password:
				return "successfully loggedin"
			return "invalid email or password"

	def validate_email(self,email):
		if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
			return True
		return False

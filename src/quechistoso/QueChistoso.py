import objects

class QueChistoso:
	
	def __init__(self):
		self.pages = {} # Array de paginas
		self.title = ''
		self.description = ''
		self.users = '' #Objetos usuario?
		self.posts = '' #Objetos post?
		self.comments = '' #Objetos comment?
		self.db = '' #Database object

	def create_user(self, email, username, password):
		import bcrypt
		from persist.mongoDB import mongoDB
		hashed = bcrypt.hashpw(password, bcrypt.gensalt(13))
		user = objects.User(email, username, hashed)
		mongo = mongoDB()
		mongo.insert_user(user)

	def authenticate_user(self, email, password):
		import uuid

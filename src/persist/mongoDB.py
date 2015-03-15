from pymongo import MongoClient
import pymongo

class mongoDB:

	def __init__(self):
		self.client = MongoClient()
		self.db_name = 'QueChistoso' #TODO: Maybe load this from ENVVARS / Config?
		self.db = self.client[self.db_name]
		# Prevent from adding repeated emails
		self.db['users'].ensure_index(
			[ ('email', pymongo.DESCENDING) ],
			unique=True,
			sparse=True )

	def insert_user(self, user):
		
		usr_document = {
			'username' : user.username,
			'email' : user.email,
			'password' : user.password
		}

		try:
			self.db['users'].insert(usr_document)
		except pymongo.errors.DuplicateKeyError:
			#TODO: return false?
			print 'Email: ' + user.email + ' not inserted'
from pymongo import MongoClient
from hashlib import sha512

client = MongoClient()

class UserManager:
    def __init__(self, db):
        self.db = client[db]

    def isRegistered(self, username):
        result = self.db.users.find_one({
            'username': username
        })

        return bool(result)
    
    def login(self, username, password):
        result = self.db.users.find_one({
          'username': username,
          'passhash': sha512(password).hexdigest()
        })

        if result is None:
            return True, 'Successfully logged in!'
        else:
            return False, 'Invalid username or password.'

    def register(self, username, password, confirm):
        if password != confirm:
            return False, 'Passwords must match.'
        elif self.isRegistered(username):
            return False, 'User already exists.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': sha512(password).hexdigest()
            })

            return True, 'Successfully registered!'

from pymongo import MongoClient
from util import hash_string

client = MongoClient()

class UserManager:
    def __init__(self, db):
        self.db = client[db]

    def login(self, username, password):
        result = self.db.users.find_one({
          'username': username,
          'passhash': hash_string(password)
        })
         
        if result is None:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def isRegistered(self, username):
        result = self.db.users.find_one({
            'username': username
        })

        return bool(result)

    def register(self, username, password, confirmationPassword):
        if self.isRegistered(username):
            return False, 'User already exists.'
        elif password != confirmationPassword:
            return False, 'Password do not match.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': hash_string(password)
            })

            return True, 'Successfully registered!'

    def dropUser(self, username):
        result = self.db.users.find_one({
            'username': username
        })
        if result:
            self.db.users.remove({
                'username': username
            })
            return True
        return False
        
    def isAdmin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })

        return bool(result)
            
    def makeAdmin(self, username):
        if self.isAdmin(username):
            return False, 'User is already an admin'
        result = self.db.users.find_one({
                'username': username,
            })
        if result is not None:            
            self.db.admins.insert_one({
                'username': username,
                'passhash': result['passhash']
            })
            return True, 'User is now an admin'

    def authAdmin(self, username, password):
        result = self.db.admins.find_one({
            'username': username,
            'passhash': hash_string(password)
        })

        if result is None:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def dropAdmin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })

        if result is None:
            return False
        else:
            self.db.admins.remove({
                'username': username
            })
            return True

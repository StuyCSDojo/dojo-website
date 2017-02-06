from pymongo import MongoClient
from util import hash_string

client = MongoClient()

class UserManager:
    def __init__(self, db):
        self.db = client[db]

    def is_registered(self, username):
        result = self.db.users.find_one({
            'username': username
        })
        return bool(result)

    def is_admin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })
        return bool(result)

    def is_developer(self, username):
        result = self.db.developers.find_one({
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

    def login(self, username, password):
        result = self.db.users.find_one({
          'username': username,
          'passhash': hash_string(password)
        })
         
        if not result:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def make_admin(self, username):
        if self.isAdmin(username):
            return False, 'User is already an admin.'
        result = self.db.users.find_one({
                'username': username
            })
        if result:            
            self.db.admins.insert_one({
                'username': username,
                'passhash': result['passhash']
            })
            return True, 'User is now an admin!'
        else:
            return False, 'User does not exists.'

    def make_developer(self, username):
        if self.isDeveloper(username):
            return False, 'User is already a developer.'
        result = self.db.users.find_one({
            'username': username
        })
        if result:
            self.db.developers.insert_one({
                'username': username,
                'passhash': result['passhash']
            })
            self.makeAdmin(username)
            return True, 'User is now a developer!'
        else:
            return False, 'User does not exists.'
        
    def drop_user(self, username):
        result = self.db.users.find_one({
            'username': username
        })
        if not result:
            return False, 'User is not found.'
        else:
            self.db.users.remove({
                'username': username
            })
            self.dropAdmin(username)
            self.dropDeveloper(username)
            return True, 'User is no longer registered!'
                    
    def drop_admin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })

        if not result:
            return False, 'User is not an admin.'
        else:
            self.db.admins.remove({
                'username': username
            })
            return True, 'User is no longer an admin!'

    def drop_developer(self, username):
        result = self.db.developers.find_one({
            'username': username
        })
        if not result:
            return False, 'User is not a developer.'
        else:
            self.db.developers.find_one({
                'username': username
            })
            return True, 'User is no longer a developer!'
        

    def auth_admin(self, username, password):
        result = self.db.admins.find_one({
            'username': username,
            'passhash': hash_string(password)
        })
        if not result:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def auth_developer(self, username, password):
        result = self.db.developers.find_one({
            'username': username,
            'passhash': hash_string(password)
        })
        if not result:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

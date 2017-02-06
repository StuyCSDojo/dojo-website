from pymongo import MongoClient
from util import hash_string

client = MongoClient()

class DBManager:
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

    def is_registered(self, username):
        result = self.db.users.find_one({
            'username': username
        })

        return bool(result)

    def register(self, username, password, confirm_password):
        if self.is_registered(username):
            return False, 'User already exists.'
        elif password != confirm_password:
            return False, 'Password do not match.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': hash_string(password)
            })

            return True, 'Successfully registered!'

    def drop_user(self, username):
        if self.is_registered(username):
            self.db.users.remove({
                'username': username
            })
            
            return True, 'User removed.'
        else:
            return False, 'User not found!'
        
    def is_admin(self, username):
        result = self.db.admins.find_one({
            'username': username
        })

        return bool(result)
            
    def make_admin(self, username):
        if not self.is_registered(username):
            return False, 'User not found!' 
        elif self.is_admin(username):
            return False, 'User is already an admin.'
        else:
            self.db.admins.insert_one({
                'username': username
            })
                
            return True, 'User is now an admin'

    def auth_admin(self, username, password):
        result = self.db.admins.find_one({
            'username': username,
            'passhash': hash_string(password)
        })

        if result is None:
            return False, 'Invalid username or password.'
        else:
            return True, 'Successfully logged in!'

    def drop_admin(self, username):
        if self.is_admin(username):
            self.db.admins.remove({
                'username': username
            })

            return True, 'Admin removed.'
        else:
            return False, 'Admin not found!'

    def create_post(self, title, author, body):
        result = self.db.posts.insert_one({
            'title': title,
            'author': author,
            'body': body
        })

        return result

    def get_post(self, _id):
        return self.db.posts.find_one({
            '_id': _id
        })

    def make_announcement(self, username, title, body, timestamp):
        result = self.db.announcements.insert_one({
            'username': username,
            'title': title,
            'body': body,
            'timestamp': timestamp
        })

        return result

    def get_announcements(self):
        return [announcement for announcement in self.db.announcements.find()]



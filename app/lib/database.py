from pymongo import MongoClient
from util import hash_string

client = MongoClient()

# Convert username into proper signatures for announcements
admin_names={
    'st234pa': 'Stephanie Yoon',
    'lvargas': 'Lorenz Vargas',
    'pchan': 'PChan'
}

class DBManager:

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

    def register(self, username, password, confirm_password):
        if self.is_registered(username):
            return False, 'User already exists.'
        elif password != confirm_password:
            return False, 'Password do not match.'
        else:
            self.db.users.insert_one({
                'username': username,
                'passhash': password
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
        if not self.is_registered(username):
            return False, 'User does not exist!'
        elif self.is_admin(username):
            return False, 'User is already an admin.'
        else:
            result = self.db.users.find_one({
                'username': username
            })
            self.db.admins.insert_one({
                'username': username,
                'passhash': result['passhash']
            })
            return True, 'User is now an admin!'

    def make_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist!'
        elif self.is_developer(username):
            return False, 'User is already a developer!'
        else:
            result = self.db.users.find_one({
                'username': username
            })
            self.db.developers.insert_one({
                'username': username,
                'passhash': result['passhash']
            })
            self.make_admin(username)
            return True, 'User is now a developer!'
        
    def drop_user(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist!'
        else:
            self.db.users.remove({
                'username': username
            })
            
            self.drop_admin(username)
            self.drop_developer(username)
            
            return True, 'User dropped!'
                    
    def drop_admin(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist!'
        elif not self.is_admin(username):
            return False, 'User is not an admin!'
        else:
            result = self.db.admins.remove({
                'username': username
            })

            return True, 'Admin dropped!'

    def drop_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist!'
        elif not self.is_developer(username):
            return False, 'User is not a developer!'
        else:
            self.db.developers.remove({
                'username': username
            })
            
            return True, 'Developer dropped!'
            
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
            'username': admin_names[username],
            'title': title,
            'body': body,
            'timestamp': timestamp
        })

        return result

    def get_announcements(self):
        announcements = [announcement for announcement in self.db.announcements.find()]
        announcements.reverse()
        return announcements

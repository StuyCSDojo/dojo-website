from pymongo import MongoClient

from util import hash_string

client = MongoClient()

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
        if password != confirm_password:
            return False, 'Passwords do not match.'
        elif self.is_registered(username):
            return False, 'User already exists.'
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

    def drop_user(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        else:
            self.db.users.remove({
                'username': username
            })
            
            self.drop_admin(username)
            self.drop_developer(username)
            
            return True, 'User dropped!'
            
    def make_admin(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif self.is_admin(username):
            return False, 'User is already an admin.'
        else:
            self.db.admins.insert_one({
                'username': username
            })

            return True, 'User is now an admin!'
        
    def drop_admin(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif not self.is_admin(username):
            return False, 'User is not an admin.'
        else:
            result = self.db.admins.remove({
                'username': username
            })

            return True, 'Admin dropped!'

    def make_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif self.is_developer(username):
            return False, 'User is already a developer.'
        else:
            self.db.developers.insert_one({
                'username': username,
            })

            self.make_admin(username)
            return True, 'User is now a developer!'

    def drop_developer(self, username):
        if not self.is_registered(username):
            return False, 'User does not exist.'
        elif not self.is_developer(username):
            return False, 'User is not a developer.'
        else:
            self.db.developers.remove({
                'username': username
            })
            
            return True, 'Developer dropped!'
            
    def make_announcement(self, username, title, body, timestamp):
        announcement = {
            'username': admin_names[username],
            'title': title,
            'body': body,
            'timestamp': timestamp
        }

        self.db.announcements.insert_one(announcement)
        return announcement

    def get_announcements(self):
        return list(self.db.announcements.find())[::-1]

    def get_topics(self):
        return list(self.db.topics.find())

    def make_topic(self, title, description):
        topic = {
            'title': title,
            'description': description
        }

        self.db.topics.insert_one(topic)
        return topic

    def get_topic_by_title(self, title):
        return self.db.topics.find_one({
            'title': title
        })

    def get_topic_by_id(self, topic_id):
        return self.db.topics.find_one({
            '_id': topic_id
        })

    def make_post(self, topic_id, title, author, body, timestamp):
        post = {
            'topic_id': topic_id,
            'title': title,
            'author': author,
            'body': body,
            'timestamp': timestamp
        }

        self.db.posts.insert_one(post)
        return post

    def get_posts_by_topic(self, topic_id):
        return self.db.posts.find({
            'topic_id': topic_id
        })

    def get_post_by_id(self, post_id):
        return self.db.posts.find_one({
            '_id': post_id
        })

    def make_comment(self, post_id, parent_id, author, body, timestamp):
        comment = {
            'post_id': post_id,
            'parent_id': parent_id,
            'author': author,
            'body': body,
            'timestamp': timestamp
        }

        self.db.comments.insert_one(comment)
        return comment

    def get_comment_by_id(self, comment_id):
        return self.db.comments.find_one({
            '_id': comment_id
        })
        
    def get_comments_from_post(self, post_id):
        return self.db.comments.find({
            'post_id': post_id
        })

    def get_child_comments(self, comment_id):
        return self.db.comments.find({
            'parent_id': comment_id
        })


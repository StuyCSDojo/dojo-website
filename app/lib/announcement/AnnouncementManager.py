import pymongo
import time

client = pymongo.MongoClient()

class AnnouncementManager(object):

    def __init__(self, db):
        self.db = client[db]
        self.admin_names = {
            'pchan': 'PChan',
            'JackieW00': 'Jackie',
            'jzaia': 'Jake Zaia',
            'TakingTheL': 'Leo',
            'st234pa': 'Stephanie Yoon',
            'lvargas': 'Lorenz Vargas',
        }

    def make_announcement(self, username, title, body):
        timestamp = time.strftime('%a %b %d %Y %I:%M:%S %p')
        announcement = {
            'username': self.admin_names[username],
            'title': title,
            'body': body,
            'timestamp': timestamp
        }
        self.db.announcements.insert_one(announcement)
        return announcement

    def get_announcements(self):
        return list(self.db.announcements.find())[::-1]

    def list_announcements(self):
        return self.db.announcements.find()

    def update_announcement(self, filter_dict, modified_dict):
        if not isinstance(filter_dict, dict):
            return False, 'First parameter must be a dictionary.'
        if not isinstance(modified_dict):
            return False, 'Second parameter must be a dictionary.'
        self.db.announcements.update_one(filter_dict, {'$set': modified_dict})
        return True,'Successfully updated.'

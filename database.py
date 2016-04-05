from pymongo import MongoClient

connection = MongoClient()

class Dojo_database_manager:
    """
    the middleware interface between databases and flask app, there are a few
    tables in the database

    users user {
        'user_id' : uq hash provided by mongo,
        'username': string (username),
        'pass_hash': hashed password (hex-string),
        'email': email (string),
        'access_level': access level of user (int)
    }

    forum TODO
    probably more TODO
    """

    def __init__(self, database):
        self.db = database

    def register_user(self, username, pass_hash, email, access_lv):
        """
        register_user: registers a new user in the database
    
        Args:
            self (type): TODO
	username (type): TODO
	pass_hash (type): TODO
	email (type): TODO
	access_lv (type): TODO
        
        Returns:
            True if successful, false otherwise
        
        Example:
            register_user('yeech', 'af1837c', 'abc@def.com', '5') --> True
        """

        us = list(self.db.users.find({'username' : username}))

        if us == []: # username avaliable
            t = {
                    'username': username,
                    'pass_hash': pass_hash,
                    'email': email,
                    'access_level': access_lv
                    }

            self.db.users.insert(t)
            return True
        
        return False

    def authenticate_user(self, username, password):
        """
        authenticate_user: checks if the username and password match
    
        Args:
            self (type): TODO
	username (type): TODO
	password (type): TODO
        
        Returns:
            True if the credentials match, False otherwise
        
        Example:
            authenticat
        
        Raises:
            TODO
        """


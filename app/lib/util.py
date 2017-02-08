from functools import wraps
from hashlib import sha512
from time import localtime, strftime, time

def hash_string(s):
    return sha512(s).hexdigest()

def format_announcement(username, title, body):
    return '''<h4>%s</h4>
    <p class='condensed light a_info'>Posted by %s on %s</p>
    <p>%s</p>''' % (title, username, strftime('%c', localtime()), body)

def get_timestamp():
    return strftime('%a %b %d %Y %I:%M:%S %p')
    
def log_name(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print func.func_name + '(' + str(*args) + str(','.join(kwargs.values())) + ')'
        return func(*args, **kwargs)
        
    return inner

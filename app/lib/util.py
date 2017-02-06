from functools import wraps

from time import time, strftime, localtime
from hashlib import sha512

def hash_string(s):
    return sha512(s).hexdigest()

admin_names = {
    'pchan': 'PChan',
    'st234pa': 'Stephanie Yoon',
    'lvargas': 'Lorenz Vargas'
}

def format_announcement(username, title, body):
    return '''<h4>%s</h4>
    <p class='condensed light a_info'>Posted by %s on %s</p>
    <p>%s</p>''' % (title, username, strftime('%c', localtime()), body)

def get_timestamp():
    return strftime('%a %b %d %Y %I:%M:%S %p')
    
def log_name(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print f.func_name + '(' + str(*args) + str(','.join(kwargs.values())) + ')'
        return f(*args, **kwargs)
        
    return inner

def log_time(f):
    @wraps(f)
    def inner(*args):
        init_t = time()
        ret_val = f(*args)
        fin_t = time()
        print 'Time: %f' % (fin_t - init_t)
        return ret_val
        
    return inner

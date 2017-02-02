from time import localtime, strftime

def getFromDict(d, key):
    if 'key' in d:
        return d[key]
    else:
        return None

def format_announcement(name, title, body):
    return '''<h4>%s</h4>
    <p class='condensed light a_info'>Posted by %s on %s</p>
    <p>%s</p>''' % (title, admin_names[name], strftime('%c', localtime()), body)

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

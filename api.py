################################################################################
# The main api for the dojo website written in flask                           #
#                                                                              #
# Authors                                                                      #
#  YEECH <alex-wyc>                                                            #
#                                                                              #
# Description                                                                  #
#  lawls                                                                       #
#                                                                              #
################################################################################

# TODO
#  TODO-List

# Dev Log
#  Project Created: 2016-02-25 16:46 - Yicheng W.

from flask import Flask, request, render_template, session, redirect, url_for
from functools import wraps
from hashlib import sha512
from sys import argv
from werkzeug.contrib.fixers import ProxyFix
from time import gmtime, strftime

def log_name(f):
    @wraps(f)
    def inner(*args, **kwargs):
        keyWordArgs = kwargs.values()
        print f.func_name + '(' + str(*args) + str(','.join(keyWordArgs)) + ')'
        return f(*args, **kwargs)
    return inner

def log_time(f):
    @wraps(f)
    def inner(*args):
        init_t = time()
        ret_val = f(*args)
        fin_t = time()
        print "Time: %f" % (fin_t - init_t)
        return ret_val
    return inner

admin_accounts = {
        'brandon' : 'b8a49162dce8ad8afb06a563ea862c04063b6f7a',
        'sophia': '6f516c4f69481dff8c01aec9da09c620f319cecd',
        'roz' : '6a5955fc112ecb6adf59c8d6023e1c41e1e9ae83',
    'pchan': 'ce57d8bc990447c7ec35557040756db2a9ff7cdab53911f3c7995bc6bf3572cda8c94fa53789e523a680de9921c067f6717e79426df467185fc7a6dbec4b2d57'
        }

admin_names = {
        'brandon' : 'Brandon Lin',
        'sophia' : 'Sophia Zheng',
        'roz' : 'Roz Joyce',
    'pchan' : 'PChan'
        }

def format_announcement(name, title, body):
    return """<h4>%s</h4>
<p class='condensed light a_info'>Posted by %s on %s</p>
<p>%s</p>""" % (title, admin_names[name], strftime('%c', gmtime()), body)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resources")
@log_name
def resources():
    return render_template("resources.html")

@app.route("/irc")
@log_name
def irc():
    return render_template("irc.html")

@app.route('/calendar')
@log_name
def calendar():
    return render_template('calendar.html')

@app.route("/tutorials/<tut>")
@log_name
def tutorial(tut):
    try:
        return render_template("./tutorials/" + tut)
    except:
        return render_template('404.html'), 404

@app.route('/admins')
@log_name
def admins():
    return render_template('make_announcement_admin.html')

@app.route('/admins', methods = ['POST'])
@log_name
def update_announcements():
    user = request.form['user']
    if user in admin_accounts:
        password = sha512()
        password.update(request.form['pass'])
        password = password.hexdigest()
        if admin_accounts[user] == password: # validated
            # do stuff TODO
            title = request.form['title']
            body = request.form['textarea1']
            oldpage = open('./templates/index.html', 'r').read().split('<h4>')
            newpage = open('./templates/index.html', 'w')
            newpage.write(oldpage[0] + format_announcement(user, title, body) + '\n<h4>' + '<h4>'.join(oldpage[1:]))
            return redirect(url_for('home'));

    return render_template('make_announcement_admin.html', err='Incorrect username/password')

@app.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html'), 404

app.wsgi_app = ProxyFix(app.wsgi_app)

try:
    app.secret_key = argv[argv.index('--key') + 1]
except ValueError:
    app.secret_key = "afsdhghjkasdfUASGFDHusdfhyaYYJHJSDF"

app.debug = True

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=5000)

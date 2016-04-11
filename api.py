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
from hashlib import sha1
from sys import argv
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/irc")
def irc():
    return render_template("irc.html")

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route("/tutorials/<tut>")
def tutorial(tut):
    try:
        return render_template("./tutorials/" + tut)
    except:
        return render_template('404.html'), 404

@app.route('/admins')
def admins():
    return render_template('make_announcement_admin.html')

@app.route('/admins', methods = ['POST'])
def update_announcements():
# TODO
    return redirect(url_for('home'));

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.wsgi_app = ProxyFix(app.wsgi_app)

try:
    app.secret_key = argv[argv.index('--key') + 1]
except ValueError:
    app.secret_key = "afsdhghjkasdfUASGFDHusdfhyaYYJHJSDF"

app.debug = True

if __name__ == "__main__":
    app.run()

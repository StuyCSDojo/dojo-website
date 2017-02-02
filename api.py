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

from flask import Flask, request, render_template, session, redirect, send_from_directory, url_for
from functools import wraps
from hashlib import sha512
from sys import argv
from werkzeug.contrib.fixers import ProxyFix
from lib.utils import get_from_dict, format_announcement, log_name, log_time

admin_accounts = {
    'pchan': '23066cad285c767bf0e63c67515d7f1d9955a158a6f2ecdd1d93eb10d782f4000947c0d91986f2436db799e198d086fc35ea117846e172dbb007f8deca2bb0bb',
    'st234pa': '14d60abd2dc5d59e023913ca2ec999970071da68cee4a0ec56dd4e44d442bc113ef4f09a548f348290ad329119963400c77b3684a412e588faedb4821d0e5c72',
    'lvargas': '9c373b042c68ffe0949ac51c893aa8a8206e56d463e5ec4425effb4a20c30b5d51546755ea191c99ab679c4a3c99366bd5ea1f1f1073dfd0d243be0214c4e0fd'
}

admin_names = {
    'pchan' : 'PChan',
    'st234pa' : 'Stephanie Yoon',
    'lvargas' : 'Lorenz Vargas'
}

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/resources/')
@log_name
def resources():
    return render_template('resources.html')

@app.route('/irc/')
@log_name
def irc():
    return render_template('irc.html')

@app.route('/calendar/')
@log_name
def calendar():
    return render_template('calendar.html')

@app.route('/tutorials/<tut>/')
@log_name
def tutorial(tut):
    try:
        return render_template('./tutorials/release/' + tut)
    except:
        return render_template('404.html'), 404

@app.route('/doc/')
@app.route('/doc/<path:filename>/')
@log_name
def docs(filename='index.html'):
    return send_from_directory('docs/build/html', filename)
    
@app.route('/admins/')
@log_name
def admins():
    return render_template('make_announcement_admin.html')

@app.route('/admins/', methods = ['POST'])
@log_name
def update_announcements():
    user = request.form['user']
    if user in admin_accounts:
        password = sha512(request.form['pass']).hexdigest()
        
        if admin_accounts[user] == password: # validated
            # do stuff TODO
            title = request.form['title']
            body = request.form['textarea1']
            oldpage = open('./templates/index.html', 'r').read().split('<h4>')
            newpage = open('./templates/index.html', 'w')
            newpage.write(oldpage[0] + format_announcement(user, title, body) + '\n<h4>' + '<h4>'.join(oldpage[1:]))
            return redirect(url_for('home'));

    return render_template('make_announcement_admin.html', err='Incorrect username/password')

@app.route('/register/', methods = ['POST'])
def register():
    username = get_from_dict(request.form, 'username')
    
@app.route('/forum/')
def forumRoot():
    return render_template('forum.html')

@app.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html'), 404

def run():
    app.wsgi_app = ProxyFix(app.wsgi_app)

    try:
        app.secret_key = argv[argv.index('--key') + 1]
    except ValueError:
        app.secret_key = 'afsdhghjkasdfUASGFDHusdfhyaYYJHJSDF'
    
    app.debug = True

    userManager = 
    
    app.run(host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
    run()
    

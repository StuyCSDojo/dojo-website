from flask import Blueprint, render_template, session

from lib.database import DBManager
from lib.util import log_name

public_views = Blueprint('public_views', __name__)
db_manager = DBManager('dojo_website')

@public_views.route('/loaderio-8281aaa87be94ab093606230a67f774e/')
def test_load():
    '''
    Temporary route to allow for load testing
    '''
    return render_template('loaderio-8281aaa87be94ab093606230a67f774e.html')

@public_views.route('/')
@public_views.route('/home/')
def home():
    return render_template('index.html', announcements = db_manager.get_announcements(), is_logged_in=session.get('username'))

@public_views.route('/about/')
def about():
    return render_template('about.html', is_logged_in=session.get('username'))

@public_views.route('/resources/')
@log_name
def resources():
    return render_template('resources.html', is_logged_in=session.get('username'))

@public_views.route('/irc/')
@log_name
def irc():
    return render_template('irc.html', is_logged_in=session.get('username'))

@public_views.route('/calendar/')
@log_name
def calendar():
    return render_template('calendar.html', is_logged_in=session.get('username'))

@public_views.route('/forum/')
def forum_root():
    return render_template('forum.html', is_logged_in=session.get('username'))

@public_views.route('/tutorials/<tutorial_name>/')
@log_name
def tutorial(tutorial_name):
    try:
        return render_template('./tutorials/release/' + tutorial_name, is_logged_in=session.get('username'))
    except:
        return render_template('404.html', is_logged_in=session.get('username')), 404

@public_views.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html', is_logged_in=session.get('username')), 404

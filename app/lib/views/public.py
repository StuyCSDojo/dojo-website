from flask import Blueprint, render_template

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
    return render_template('index.html', announcements=db_manager.get_announcements())

@public_views.route('/about/')
def about():
    return render_template('about.html')

@public_views.route('/resources/')
@log_name
def resources():
    return render_template('resources.html')

@public_views.route('/irc/')
@log_name
def irc():
    return render_template('irc.html')

@public_views.route('/calendar/')
@log_name
def calendar():
    return render_template('calendar.html')

@public_views.route('/forum/')
def forum_root():
    return render_template('forum.html')

@public_views.route('/tutorials/<tutorialName>/')
@log_name
def tutorial(tutorial_name):
    try:
        return render_template('./tutorials/release/' + tutorial_name)
    except:
        return render_template('404.html'), 404

@public_views.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html'), 404

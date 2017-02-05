from flask import Blueprint, render_template
from lib.util import log_name

publicViews = Blueprint('publicViews', __name__)

@publicViews.route('/loaderio-8281aaa87be94ab093606230a67f774e/')
def testLoad():
    '''
    Temporary route to allow for load testing
    '''
    return render_template('loaderio-8281aaa87be94ab093606230a67f774e.html')

@publicViews.route('/')
@publicViews.route('/home/')
def home():
    return render_template('index.html')

@publicViews.route('/about/')
def about():
    return render_template('about.html')

@publicViews.route('/resources/')
@log_name
def resources():
    return render_template('resources.html')

@publicViews.route('/irc/')
@log_name
def irc():
    return render_template('irc.html')

@publicViews.route('/calendar/')
@log_name
def calendar():
    return render_template('calendar.html')

@publicViews.route('/forum/')
def forumRoot():
    return render_template('forum.html')

@publicViews.route('/tutorials/<tutorialName>/')
@log_name
def tutorial(tutorialName):
    try:
        return render_template('./tutorials/release/' + tutorialName)
    except:
        return render_template('404.html'), 404

@publicViews.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html'), 404

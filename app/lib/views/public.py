import flask
import os.path

from lib.announcement import AnnouncementManager
from lib.utils import utils

public_views = flask.Blueprint('public_views', __name__)
announcement_manager = AnnouncementManager.AnnouncementManager('dojo_website')

@public_views.route('/loaderio-8281aaa87be94ab093606230a67f774e/')
def test_load():
    """
    Temporary route to allow for load testing
    """
    return flask.render_template('loaderio-8281aaa87be94ab093606230a67f774e.html')

@public_views.route('/')
@public_views.route('/home/')
def home():
    return flask.render_template('index.html', announcements=announcement_manager.get_announcements(),
                                 is_logged_in=flask.session.get('username'))

@public_views.route('/about/')
def about_page():
    return flask.render_template('about.html')

def resources():
    """
    The public resources section is served by Nginx for a performance boost
    """

@public_views.route('/calendar/')
@utils.log_name
def calendar():
    return flask.render_template('calendar.html', is_logged_in=flask.session.get('username'))

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
    return render_template('forum_root.html',
                           is_logged_in=session.get('username'),
                           topics = db_manager.get_topics())

@public_views.route('/forum/<topic_id>')
def forum_topic(topic_id):
    topic = db_manager.get_topic_by_id(topic_id)
    posts = db_manager.get_posts_by_topic(topic_id)

    print topic
    
    return render_template('forum_topic.html', topic = topic, posts = posts)
    
@public_views.route('/forum/<topic_id>/<post_id>')
def forum_post(topic_id, post_id):
    topic = db_manager.get_topic_by_id(topic_id)
    post = db_manager.get_post_by_id(post_id)
    comments = db_manager.get_comments_from_post(post_id)

    return render_template('forum_post.html',
                           topic = topic, post = post, comments = comments)

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

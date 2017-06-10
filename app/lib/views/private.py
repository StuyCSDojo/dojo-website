import flask
import os.path

from lib.announcement import AnnouncementManager
from lib.security import AuthManager
from lib.security import security
from lib.security import security_utils
from lib.utils import utils

private_views = flask.Blueprint('private_views', __name__)
announcement_manager = AnnouncementManager.AnnouncementManager('dojo_website')
auth_manager = AuthManager.AuthManager('dojo_website')

@private_views.route('/docs/')
@private_views.route('/docs/<path:filename>')
@utils.log_name
@security_utils.nocache
@security.login_required(developer_required=True)
def render_documentation(filename='index.html'):
    path = os.path.join('dojo-docs/docs/build/html', filename)
    return flask.current_app.send_static_file(path)

@private_views.route('/private/resources/')
@private_views.route('/private/resources/<path:filename>')
@utils.log_name
@security_utils.nocache
@security.login_required(developer_required=True)
def render_resources(filename='index.html'):
    path = os.path.join('resources/private_resources/build/html', filename)
    return flask.current_app.send_static_file(path)

@private_views.route('/admins/')
@utils.log_name
@security_utils.nocache
@security.login_required(admin_required=True)
def render_announcement_page():
    return flask.render_template('make_announcement_admin.html',
                                 is_logged_in=flask.session.get('username'))

@private_views.route('/admins/', methods=['POST'])
@utils.log_name
def update_announcements():
    username = flask.session.get('username')
    title = flask.request.form.get('title')
    message = flask.request.form.get('message')
    announcement_manager.make_announcement(username, title, message)
    return flask.redirect(flask.url_for('public_views.home'))

@private_views.route('/presentation/')
@private_views.route('/presentation/<path:filename>')
@security_utils.nocache
def presentation(filename='index.html'):
    path = os.path.join('presentation/build/html', filename)
    return flask.current_app.send_static_file(path)

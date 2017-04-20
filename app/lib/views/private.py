from flask import Blueprint, current_app, render_template, redirect, request, session, url_for
from os.path import join

from lib.database import DBManager
from lib.security.security import login_required
from lib.security.utils import nocache
from lib.util import format_announcement, get_timestamp, log_name

private_views = Blueprint('private_views', __name__)
db_manager = DBManager('dojo_website')

@private_views.route('/docs/')
@private_views.route('/docs/<path:filename>/')
@log_name
@nocache
@login_required(developer_required = True)
def render_documentation(filename = 'index.html'):
    path = join('docs/build/html', filename)
    return current_app.send_static_file(path)

@private_views.route('/private/resources/')
@private_views.route('/private/resources/<path:filename>/')
@log_name
@nocache
@login_required(developer_required = True)
def render_resources(filename = 'index.html'):
    path = join('resources/private_resources/build/html', filename)
    return current_app.send_static_file(path)
                                     
@private_views.route('/admins/')
@log_name
@nocache
@login_required(admin_required = True)
def admins():
    return render_template('make_announcement_admin.html', is_logged_in = session.get('username'))

@private_views.route('/admins/', methods = ['POST'])
@log_name
def update_announcements():
    username = session.get('username')
    title = request.form.get('title')
    body = request.form.get('textarea1')
    timestamp = get_timestamp()

    db_manager.make_announcement(username, title, body, timestamp)
    return redirect(url_for('public_views.home'))

@private_views.route('/presentation/')
@private_views.route('/presentation/<path:filename>/')
@nocache
@login_required(developer_required = True)
def presentation(filename = 'index.html'):
    if session['username'] != 'pchan' and session['username'] != 'stuycsteachers':
        return
    path = join('presentation/build/html', filename)
    return current_app.send_static_file(path)
        

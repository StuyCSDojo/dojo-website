from flask import Blueprint, render_template, redirect, request, send_from_directory, session, url_for

from lib.security.back import back
from lib.util import log_name, format_announcement, get_timestamp
from lib.security.security import login_required
from lib.database import DBManager

private_views = Blueprint('private_views', __name__)
db_manager = DBManager('dojo_website')

@private_views.route('/doc/')
@private_views.route('/doc/<path:filename>/')
@log_name
@back.anchor
@login_required(developer_required=True)
def render_documentation(filename='index.html'):
    if filename != 'index.html' and 'html' in filename[:filename.find('/')]:
        while 'html' in filename[:filename.find('/')] and filename.find('html') != len(filename) - 4:
            filename = filename[filename.find('/') + 1:]
    return send_from_directory('../docs/build/html', filename)

@private_views.route('/admins/')
@log_name
@back.anchor
@login_required(admin_required=True)
def admins():
    return render_template('make_announcement_admin.html')
                        
@private_views.route('/admins/', methods=['POST'])
@log_name
def update_announcements():
    username = session.get('username')
    title = request.form.get('title')
    body = request.form.get('textarea1')
    timestamp = get_timestamp()

    announcement = {
        'username': username,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }

    db_manager.make_announcement(username, title, body, timestamp)
    
    return redirect(url_for('public_views.home'))

from flask import Blueprint, render_template, redirect, request, send_from_directory, session, url_for

from lib.util import log_name, format_announcement
from lib.security.security import login_required

privateViews = Blueprint('privateViews', __name__)

@privateViews.route('/doc/')
@privateViews.route('/doc/<path:filename>/')
@log_name
def renderDocumenation(filename='index.html'):
    if filename != 'index.html' and 'html' in filename[:filename.find('/')]:
        while 'html' in filename[:filename.find('/')] and filename.find('html') != len(filename) - 4:
            filename = filename[filename.find('/') + 1:]
    return send_from_directory('../docs/build/html', filename)

@privateViews.route('/admins/')
@log_name
@login_required(admin_required=True)
def admins():
    return render_template('make_announcement_admin.html')
                        
@privateViews.route('/admins/', methods=['POST'])
@log_name
def update_announcements():
    username = session.get('username')
    title = request.form.get('title')
    body = request.form.get('textarea1')
    oldpage = open('./templates/index.html').read().split('<h4>')
    newpage = open('./templates/index.html', 'w')
    newpage.write(oldpage[0] + format_announcement(username, title, body) + '\n<h4>' + '<h4>'.join(oldpage[1:]))
    return redirect(url_for('publicViews.home'))

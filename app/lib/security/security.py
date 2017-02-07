from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from functools import wraps

from back import back
from lib.database import DBManager

security = Blueprint('security', __name__)
db_manager = DBManager('dojo_website')

def login_required(admin_required=False, developer_required=False):
    def actual_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if is_logged_in(admin_required=admin_required, developer_required=developer_required):
                return function(*args, **kwargs)
            return redirect(url_for('security.login_form'))
        return wrapper
    return actual_decorator
                                    
def is_logged_in(admin_required=False, developer_required=False):
    print developer_required
    print admin_required
    username = session.get('username')
    
    if not username:
        return False
    elif db_manager.is_registered(username) and (not admin_required and not developer_required):
        return True
    elif (admin_required and db_manager.is_admin(username)) or (developer_required and db_manager.is_developer(username)):
        return True
    elif admin_required or developer_required:
        return False
    else:
        session.pop('username')

@security.route('/register/')
def register_form(err=None):
    err = request.args.get('err')
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('register.html', err=err)

@security.route('/register/', methods = ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if not username or not password or not confirm_password:
        return redirect(url_for('security.register_form', err='Please fill out all fields!'))

    results = db_manager.register(username, password, confirm_password)

    if results[0]:
        return redirect(url_for('security.login_form'))
    else:
        return redirect(url_for('security.register_form', err=results[1]))

@security.route('/login/')
def login_form(err=None):
    err = request.args.get('err')
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('login.html', err=err)

@security.route('/login/', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return redirect(url_for('security.login_form', err='Please fill out all fields!'))
    else:
        results = db_manager.login(username, password)
        
        if results[0]:
            session['username'] = username
            return back.redirect()
        else:
            return redirect(url_for('security.login_form', err=results[1]))

@security.route('/logout/')
def logout():
    if is_logged_in():
        session.pop('username')
    return redirect(url_for('public_views.home'))

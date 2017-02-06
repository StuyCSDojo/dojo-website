from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from functools import wraps

from lib.database import DBManager

security = Blueprint('security', __name__)
db_manager = DBManager('dojo_website')

def login_required(admin_required = False):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            if is_logged_in(admin_required = admin_required):
                return function(*args, **kwargs)
            return redirect(url_for('security.login_form', next=request.url))
        return wrapper
    return actual_decorator
                                    
def is_logged_in(admin_required = False):
    username = session.get('username')
    
    if not username:
        return False
    elif not admin_required and db_manager.is_registered(username):
        return True
    elif admin_required and db_manager.is_admin(username):
        return True
    elif admin_required:
        return False
    else:
        session.pop('username')

@security.route('/register/')
def register_form():
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('register.html')

@security.route('/register/', methods = ['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if not username or not password or not confirm_password:
        flash('Please fill out all fields!')
        return redirect(url_for('security.register_form'))
    else:
        results = db_manager.register(username, password, confirm_password)
        flash(results[1])
        return redirect(url_for('security.login_form'))

@security.route('/login/')
def login_form():
    if is_logged_in():
        return redirect(url_for('public_views.home'))
    else:
        return render_template('login.html')

@security.route('/login/', methods = ['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    next_page = request.args.get('next')

    if not username or not password:
        flash('Please fill out all fields!')
        return redirect(url_for('security.login_form'))
    else:
        results = db_manager.login(username, password)
        
        if results[0]:
            session['username'] = username
            return next_page or redirect(url_for('public_views.home'))
        else:
            flash(results[1])
            return redirect(url_for('security.login_form'))

@security.route('/logout/')
def logout():
    if is_logged_in():
        session.pop('username')
        
    return redirect(url_for('public_views.home'))

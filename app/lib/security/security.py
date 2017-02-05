from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from functools import wraps

from lib.database import UserManager

security = Blueprint('security', __name__)
userManager = UserManager('DojoWebsite')

def login_required(admin_required=False):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            if isLoggedIn(admin_required=admin_required):
                return function(*args, **kwargs)
            return redirect(url_for('security.loginForm', next=request.url))
        return wrapper
    return actual_decorator
                                    
def isLoggedIn(admin_required=False):
    username = session.get('username')
    if not username:
        return False
    elif not admin_required and userManager.isRegistered(username):
        return True
    elif admin_required and userManager.isAdmin(username):
        return True
    elif admin_required:
        return False
    else:
        session.pop('username')

@security.route('/register/')
def registerForm():
    if isLoggedIn():
        return redirect(url_for('publicViews.home'))
    return render_template('register.html')

@security.route('/register/', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirmationPassword = request.form.get('confirmationPassword')
    
    if not username or not password or not confirmationPassword:
        flash('Please fill out all the fields!')
        return redirect(url_for('security.registerForm'))
    else:
        results = userManager.register(username, password, confirmationPassword)
        flash(results[1])
        return redirect(url_for('security.loginForm'))

@security.route('/login/')
def loginForm():
    if isLoggedIn():
        return redirect(url_for('publicViews.home'))
    return render_template('login.html')

@security.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    next = request.args.get('next')

    if not username or not password:
        flash('Please fill out all fields!')
        return redirect(url_for('security.loginForm'))
    else:
        results = userManager.login(username, password)
        if results[0]:
            session['username'] = username
            return next or redirect(url_for('publicViews.home'))
        else:
            flash(results[1])
            return redirect(url_for('security.loginForm'))

@security.route('/logout/')
def logout():
    if isLoggedIn():
        session.pop('username')
    return redirect(url_for('publicViews.home'))

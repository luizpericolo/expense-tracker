from app import app, lm
from flask import request, redirect, render_template, url_for, flash, Blueprint, session
from flask_login import login_user, logout_user

from app.forms import SignupForm, LoginForm
from app.models import User
from app.utils import flash_form_errors
from app.repository import find_user_by_name, insert_user, find_user

auth = Blueprint('auth', __name__, template_folder='../static/templates')


@auth.route('/signup', methods=['GET'])
def signup_get():
    return render_template('signup.html', title='Sign up', form=SignupForm())


@auth.route('/signup', methods=['POST'])
def signup_post():
    form = SignupForm(request.form)
    if form.validate():
        username = form.username.data
        password = form.password.data
        existing_user = find_user_by_name(username)
        if existing_user is None:
            new_user = User(username, password)
            new_user = insert_user(username, password)
            if new_user:
                flash("User '{}' created successfully. Please log in!".format(form.username.data), category='success')
            else:
                flash('Error creating user', category='danger')
            return redirect(url_for('auth.login_get'))
        else:
            flash("Username '{}' is already taken".format(form.username.data), category='danger')
    else:
        flash_form_errors(form)
    return render_template('signup.html', title='Sign up', form=form)


@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', title='Log in', form=LoginForm())


@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm(request.form)
    if form.validate():
        user = find_user_by_name(form.username.data)
        if user and User.validate_login(user.password, form.password.data):
            login_user_(user)
            return redirect(request.args.get('next') or url_for('site.home'))
        flash('Wrong username or password!', category='danger')
    return render_template('login.html', title='Log in', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    if 'username' in session:
        session.pop('username')
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login_get'))


@lm.user_loader
def load_user(user_id):
    return find_user(user_id)


def login_user_(user):
    if login_user(user):
        session['username'] = user.username
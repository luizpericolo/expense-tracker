from app import app, lm
from flask import request, redirect, render_template, url_for, flash, Blueprint, session
from flask_login import login_user, logout_user, login_required
from app.forms import SignupForm, LoginForm
from app.models import User

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
        existing_user = app.config['USERS_COLLECTION'].find_one({'name': username})
        if existing_user is None:
            new_user = User(username, password)
            app.config['USERS_COLLECTION'].insert({'name': new_user.username, 'password': new_user.password})
            flash("User '{}' created successfully. Please log in!".format(form.username.data), category='success')
            return redirect(url_for('auth.login_get'))
        else:
            flash("Username '{}' is already taken".format(form.username.data), category='error')
    else:
        for field, field_errors in form.errors.items():
            flash('{}: {}'.format(field, ','.join(field_errors)), category='error')
    return render_template('signup.html', title='Sign up', form=form)


@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', title='Log in', form=LoginForm())


@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm(request.form)
    if form.validate():
        user = app.config['USERS_COLLECTION'].find_one({'name': form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['name'], user['password'])
            login_user_(user_obj)
            return redirect(request.args.get('next') or url_for('expense.home'))
        flash('Wrong username or password!', category='error')
    return render_template('login.html', title='Log in', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    if 'username' in session:
        session.pop('username')
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login_get'))


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({'name': username})
    if not u:
        return None
    return User(u['name'], u['password'])


def login_user_(user):
    if login_user(user):
        session['username'] = user.username
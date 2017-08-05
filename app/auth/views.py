from app import app
from flask import request, redirect, render_template, url_for, flash, Blueprint
from flask_login import login_user, logout_user, login_required
from app.forms import SignupForm, LoginForm
from app.user import User

auth = Blueprint('auth', __name__, template_folder='../static/templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({'_id': form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['id'])
            login_user(user_obj)
            flash('Logged in successfully!', category='success')
            return redirect(request.args.get('next') or url_for('summary'))
        flash('Wrong username or password!', category='error')
    return render_template('signup.html', title='Sign up', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({'_id': form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['id'])
            login_user(user_obj)
            flash('Logged in successfully!', category='success')
            return redirect(request.args.get('next') or url_for('summary'))
        flash('Wrong username or password!', category='error')
    return render_template('login.html', title='Log in', form=form)
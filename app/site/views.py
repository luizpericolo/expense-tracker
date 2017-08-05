from flask import render_template, Blueprint, session, redirect, url_for

site = Blueprint('site', __name__, template_folder='../static/templates')


@site.route('/')
@site.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('auth.login_get'))

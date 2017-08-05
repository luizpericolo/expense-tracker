from flask import render_template, Blueprint, session, redirect, url_for

from app.repository import find_user_expenses

site = Blueprint('site', __name__, template_folder='../static/templates')


@site.route('/')
@site.route('/home')
def home():
    if 'user_id' in session:
        user_expenses = find_user_expenses(session.get('user_id'), limit=10)
        return render_template('home.html', expenses=list(user_expenses))
    else:
        return redirect(url_for('auth.login_get'))

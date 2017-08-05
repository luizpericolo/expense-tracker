from flask import render_template, Blueprint

site = Blueprint('expense', __name__, template_folder='../static/templates')

@site.route('/')
@site.route('/home')
def home():
    return render_template('home.html')
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='static/templates')
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.id_attribute = 'id'
lm.login_view = 'auth.login_get'

csrf = CSRFProtect(app)

from .site.views import site
from .auth.views import auth
from .expense.views import expense

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(expense)

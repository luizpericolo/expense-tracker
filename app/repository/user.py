from app import app
from app.models import User
from werkzeug.security import generate_password_hash

from bson.objectid import ObjectId


def find_user(user_id):
    user_data = app.config['USERS_COLLECTION'].find_one({'_id': ObjectId(user_id)})
    if user_data:
        return User(user_data.get('username'), password=user_data.get('password'), _id=user_data.get('_id'))
    return None

def find_user_by_name(username):
    user_data = app.config['USERS_COLLECTION'].find_one({'username': username})
    if user_data:
        return User(user_data.get('username'), password=user_data.get('password'), _id=user_data.get('_id'))
    return None


def insert_user(name, raw_password):
    password = generate_password_hash(raw_password, method=app.config['PASSWORD_HASH_METHOD'])
    user_data = {
        'username': name,
        'password': password,
    }
    return app.config['USERS_COLLECTION'].insert_one(user_data)

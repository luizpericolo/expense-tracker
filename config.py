import os

from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_NAME = 'expense_tracker'

MONGO_DB_USER = os.environ.get("MONGO_DB_USER")
MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_PASSWORD")

MONGODB_URI = "mongodb://{}:{}@ds135963.mlab.com:35963/{}".format(
    MONGO_DB_USER, MONGO_DB_PASSWORD, DB_NAME)

DATABASE = MongoClient(MONGODB_URI)[DB_NAME]
TAGS_COLLECTION = DATABASE.tags
USERS_COLLECTION = DATABASE.users
EXPENSES_COLLECTION = DATABASE.expenses


PASSWORD_HASH_METHOD = 'pbkdf2:sha512:10000'

DEBUG = True
import os # noqa

from pymongo import MongoClient # noqa

from tb_tutorial.settings.base import *  # noqa

DEBUG = False

mongodb_user = os.getenv("MONGO_USER")
mongodb_password = os.getenv("MONGO_PASSWORD")
MONGO_CLIENT = MongoClient(
    f"mongodb://{mongodb_user}:{mongodb_password}@ds027744.mlab.com:27744/tb_tutorial"
)
MONGO_DB = MONGO_CLIENT.telegram_bots

import os # noqa

from pymongo import MongoClient # noqa

from tb_tutorial.settings.base import *  # noqa

DEBUG = False

ALLOWED_HOSTS.append("tb-tutorial.herokuapp.com")

mongodb_user = os.getenv("MONGO_USER")
mongodb_password = os.getenv("MONGO_PASSWORD")
mongodb_host = os.getenv("MONGO_HOST")
MONGO_CLIENT = MongoClient(
    f"mongodb://{mongodb_user}:{mongodb_password}@{mongodb_host}"
)
MONGO_DB = MONGO_CLIENT.tb_tutorial

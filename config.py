from pymongo import MongoClient


DEBUG = True
client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('admin', 'admin'))
DATABASE =client['restfulapi'] # DB_NAME




from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


# use PyMongo driver to connect to Atlas cluster
client = MongoClient("mongodb+srv://test:test123@cluster0.6mzbxvi.mongodb.net/?retryWrites=true&w=majority")

# create db on your cluster
db = client.gettingStarted

# create a new collection for database
assistant = db.assistant
import os
from pymongo import MongoClient

def get_database(dbname: str):
    CONNECTION_STRING = os.environ.get('LINK_DATABASE')

    client = MongoClient(CONNECTION_STRING)

    return client[dbname]

db_transacao = get_database("transacao")
collection_transacao = db_transacao["transacao"]

# collection_name.insert_many([item_1,item_2])
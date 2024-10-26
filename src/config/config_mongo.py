import os
from pymongo import MongoClient

def get_database(dbname: str):
    CONNECTION_STRING = os.environ.get('LINK_DATABASE_MONGO', "must_be_set_in_env")

    client = MongoClient(CONNECTION_STRING)

    return client[dbname]

db_transaction = get_database("AllTransactions")
collection_transaction = db_transaction["Transaction"]

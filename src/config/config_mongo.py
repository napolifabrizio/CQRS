import os
from pymongo import MongoClient

class ConfigMongo():

    def __init__(self):
        self._linkDatabase = os.environ.get('LINK_DATABASE_MONGO', "must_be_set_in_env")

    def _client(self):
        return MongoClient(self._linkDatabase)

    def _database_all_transactions(self):
        client = self._client()
        return client["AllTransactions"]

    def collection_transaction(self):
        collection = self._database_all_transactions()
        return collection["Transaction"]

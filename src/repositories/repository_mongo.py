
class MongoRepo():

    def __init__(self, collection):
        self._collection = collection

    def insert_one_mongo(self, document: dict) -> bool:
        if self._collection.insert_one(document):
            return True
        return False

    def delete_one_mongo(self, cod: int) -> bool:
        if self._collection.delete_one({"CodCli": cod}):
            return True
        return False

    def get_one_mongo(self, cod: int) -> bool:
        if self._collection.find_one({"CodCli": cod}):
            return True
        return False

    def update_one_mongo(self, cod: int, new_valor: dict) -> bool:
        if self._collection.update_one({"CodCli": cod}, new_valor):
            return True
        return False

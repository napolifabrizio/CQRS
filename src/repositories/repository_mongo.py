from config.config import collection_transaction

def insert_one_mongo(document: dict) -> str:
    if not collection_transaction.insert_one(document):
        raise "Document can't be inserted"
    return "Document inserted"

def delete_one_mongo(cod):
    if not collection_transaction.delete_one({"CodCli": cod}):
        return "Document not found or wrong parameter"

def get_one_mongo(cod):
    if collection_transaction.find_one({"CodCli": cod}):
        return True
    return False

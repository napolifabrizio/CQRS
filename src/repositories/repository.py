from src.config.config import collection_transaction

def insert_one_mongo(document: dict) -> str:
    if not collection_transaction.insert_one(document):
        raise "Document can't be inserted"
    return "Document inserted"

def insert_many_mongo(documents: list[dict]) -> str:
    if not collection_transaction.insert_many(documents):
        raise "Document can't be inserted"
    return "Document inserted"

def delete_one_mongo(document: dict):
    if not collection_transaction.delete_one():
        return "Document not found or wrong parameter"

def delete_many_mongo(documents: list[dict]):
    if not collection_transaction.delete_one():
        return "Document not found or wrong parameter"
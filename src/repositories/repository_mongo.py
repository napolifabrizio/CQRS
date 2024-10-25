from config.config import collection_transaction

def insert_one_mongo(document: dict) -> str:
    if not collection_transaction.insert_one(document):
        raise "Document can't be inserted"
    return "Document inserted"

def delete_one_mongo(Cpf):
    if not collection_transaction.delete_one({"Cpf": Cpf}):
        return "Document not found or wrong parameter"

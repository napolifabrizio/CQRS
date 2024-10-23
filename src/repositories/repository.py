from src.config.config import collection_transaction
from src.models.Transaction import Transaction, PaymentMethod

def insert_one_mongo(document: Transaction) -> str:
    document_json = document.model_dump()
    if not collection_transaction.insert_one(document_json):
        raise "Document can't be inserted"
    return "Document inserted"

def insert_many_mongo(documents: list[Transaction]) -> str:
    documents_json = [d.model_dump() for d in documents]
    if not collection_transaction.insert_many(documents_json):
        raise "Document can't be inserted"
    return "Document inserted"

def delete_one_mongo(document: Transaction):
    document_json = document.model_dump()
    if not collection_transaction.delete_one():
        return "Document not found or wrong parameter"

def delete_many_mongo(documents: list[Transaction]):
    documents_json = [d.model_dump() for d in documents]
    if not collection_transaction.delete_one():
        return "Document not found or wrong parameter"
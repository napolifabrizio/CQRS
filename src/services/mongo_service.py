import uuid
from src.repositories.repository import insert_many_mongo, insert_one_mongo
from src.models.Transaction import Transaction, PaymentMethod

def add_document(document: Transaction):
    PaymentMethod.is_valid(document.PaymentMethod)
    document.id = uuid.uuid4()
    document_json = document.model_dump()
    insert_one_mongo(document_json)
    return True

def add_documents(documents: list[Transaction]):
    documents_json = []
    for document in documents:
        PaymentMethod.is_valid(document.PaymentMethod)
        document.id = uuid.uuid4()
        documents_json.append(document.model_dump())
    insert_many_mongo(documents_json)
    return True





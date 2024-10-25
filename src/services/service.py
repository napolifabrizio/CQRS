import uuid

import bson
from repositories.repository_mongo import insert_one_mongo, delete_one_mongo
from models.Transaction import Transaction, PaymentMethod

def add_document(document: Transaction):
    PaymentMethod.is_valid(document.PaymentMethod)
    # id = uuid.uuid4()
    # document.id = bson.Binary.from_uuid(id)
    document_json = document.model_dump()
    insert_one_mongo(document_json)
    return True

def delete_document(cpf):
    delete_one_mongo(cpf)
    return True


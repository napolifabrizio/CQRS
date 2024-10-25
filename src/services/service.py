from repositories.repository_mongo import insert_one_mongo, delete_one_mongo, get_one_mongo
from models.Transaction import Transaction, PaymentMethod

def add_document(document: Transaction):
    if get_one_mongo(document.CodCli):
        print("The account already exists")
        return False
    document_json = document.model_dump()
    insert_one_mongo(document_json)
    return True

def delete_document(cod):
    if get_one_mongo(cod):
        delete_one_mongo(cod)
        return True
    print("Account nof found")
    return False

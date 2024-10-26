from repositories.repository_mongo import insert_one_mongo, delete_one_mongo, get_one_mongo, update_one_mongo
from models.Transaction import Transaction

def add_document(document: Transaction):
    if get_one_mongo(document.CodCli):
        print("The account already exists")
        return False
    document_json = document.model_dump()
    insert_one_mongo(document_json)
    return True

def delete_document(cod: int):
    if get_one_mongo(cod):
        delete_one_mongo(cod)
        return True
    print("Account nof found")
    return False

def update_document(cod: int, new_valor: dict):
    if update_one_mongo(cod, {"$set": new_valor}):
        return True
    print("There is something wrong")
    return False
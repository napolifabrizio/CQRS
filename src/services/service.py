from repositories.repository_mongo import insert_one_mongo, delete_one_mongo, get_one_mongo, update_one_mongo
from repositories.repository_sql import insert_sql, update_sql, delete_sql
from models.Transaction import Transaction

def add_document(document: Transaction):
    if get_one_mongo(document.CodCli):
        print("The account already exists")
        return False
    document_json = document.model_dump()
    insert_one_mongo(document_json)
    insert_sql(document_json)
    return True

def delete_document(codcli: int):
    if get_one_mongo(codcli):
        delete_one_mongo(codcli)
        delete_sql(codcli)
        return True
    print("Account nof found")
    return False

def update_document(new_valor: dict, document: Transaction):
    update_one_mongo(document.CodCli, {"$set": new_valor})
    update_sql(document.model_dump())
    return True

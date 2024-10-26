from config.config_mongo import collection_transaction

def insert_one_mongo(document: dict) -> bool:
    if collection_transaction.insert_one(document):
        return True
    return False

def delete_one_mongo(cod: int) -> bool:
    if collection_transaction.delete_one({"CodCli": cod}):
        return True
    return False

def get_one_mongo(cod: int) -> bool:
    if collection_transaction.find_one({"CodCli": cod}):
        return True
    return False

def update_one_mongo(cod: int, new_valor: dict) -> bool:
    if collection_transaction.update_one({"CodCli": cod}, new_valor):
        return True
    return False

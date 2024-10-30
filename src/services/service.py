from repositories.repository_mongo import MongoRepo
from repositories.repository_sql import SqlRepo
from models.Transaction import Transaction

class Service():

    def __init__(self, mongo_repo: MongoRepo, sql_repo: SqlRepo):
        self._mongoRepo = mongo_repo
        self._sqlRepo = sql_repo

    def add_document(self, document: Transaction):
        if self._mongoRepo.get_one_mongo(document.CodCli):
            print("The account already exists")
            return False
        document_json = document.model_dump()
        self._mongoRepo.insert_one_mongo(document_json)
        self._sqlRepo.insert_sql(document_json)
        return True

    def delete_document(self, codcli: int):
        if self._mongoRepo.get_one_mongo(codcli):
            self._mongoRepo.delete_one_mongo(codcli)
            self._sqlRepo.delete_sql(codcli)
            return True
        print("Account nof found")
        return False

    def update_document(self, new_valor: dict, document: Transaction):
        self._mongoRepo.update_one_mongo(document.CodCli, {"$set": new_valor})
        self._sqlRepo.update_sql(document.model_dump())
        return True

    def get_document(self, codcli: int):
        res = self._sqlRepo.select_sql(codcli)
        return res

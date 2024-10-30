from repositories.repository_mongo import MongoRepo
from repositories.repository_sql import RepoSql
from models.Transaction import Transaction

class Service():

    def __init__(self, repo_mongo: MongoRepo, repo_sql: RepoSql):
        self._repoMongo = repo_mongo
        self._repoSql = repo_sql

    def add_document(self, document: Transaction):
        if self._repoMongo.get_one_mongo(document.CodCli):
            print("The account already exists")
            return False
        document_json = document.model_dump()
        self._repoMongo.insert_one_mongo(document_json)
        self._repoSql.insert_sql(document_json)
        return True

    def delete_document(self, codcli: int):
        if self._repoMongo.get_one_mongo(codcli):
            self._repoMongo.delete_one_mongo(codcli)
            self._repoSql.delete_sql(codcli)
            return True
        print("Account nof found")
        return False

    def update_document(self, new_valor: dict, document: Transaction):
        self._repoMongo.update_one_mongo(document.CodCli, {"$set": new_valor})
        self._repoSql.update_sql(document.model_dump())
        return True

    def get_document(self, codcli: int):
        res = self._repoSql.select_sql(codcli)
        return res

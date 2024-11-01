from models.Transaction import Transaction
from services.service import Service
from repositories.repository_mongo import MongoRepo
from repositories.repository_sql import SqlRepo
from config.config_sql import ConfigSql
from config.config_mongo import ConfigMongo

config_sql = ConfigSql()
config_mongo = ConfigMongo()

sql_repo = SqlRepo(config_sql)
mongo_repo = MongoRepo(config_mongo)

service = Service(mongo_repo, sql_repo)

test = Transaction(
    Cpf="12345678901",
    Name="Fabrizio",
    Price=10,
    CodCli=30,
    Product="Iphone X",
    PaymentMethod="Debit Card",
    Company="Apple",
)

# service.add_document(test)
service.delete_document(30)

# print(test.model_dump().items())
# service.delete_document(100)
from models.Transaction import Transaction
from services.service import Service
from repositories.repository_mongo import MongoRepo
from repositories.repository_sql import SqlRepo
from config.config_sql import ConfigSql

service = Service()

test = Transaction(
    CodCli=1,
    Cpf="12345678901",
    Name="Fabrizio",
    Price=10,
    Company="Apple",
    Product="Iphone X",
    PaymentMethod="Debit Card"
)


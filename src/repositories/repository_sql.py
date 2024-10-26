
from sqlalchemy import insert, delete, select, update, Column, Table
from config.config_sql import engine

TABLE_TRANSACTIONS = Table(
    "transactions",
    Column("codcli"),
    Column("cpf"),
    Column("name"),
    Column("price"),
    Column("company"),
    Column("paymentmethod"),
    Column("product")
)

def insert_sql(document):
    stmt = (
        insert(TABLE_TRANSACTIONS)
        .values()
    )
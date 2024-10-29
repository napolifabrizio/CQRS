
from sqlalchemy import insert, delete, select, update, Column, Table, INTEGER, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from config.config_sql import engine

Base = declarative_base()

TABLE_TRANSACTIONS = Table(
    "transactions",
    Base.metadata,
    Column("codcli", INTEGER, primary_key=True),
    Column("cpf", VARCHAR(30), nullable=False),
    Column("name", VARCHAR(100), nullable=False),
    Column("price", FLOAT, nullable=False),
    Column("company", VARCHAR(50), nullable=False),
    Column("paymentmethod", VARCHAR(20), nullable=False),
    Column("product", VARCHAR(30), nullable=True)
)

def insert_sql(document: dict):
    stmt = (
        insert(TABLE_TRANSACTIONS)
        .values(
            codcli=document["CodCli"],
            cpf=document["Cpf"],
            name=document["Name"],
            price=document["Price"],
            company=document["Company"],
            paymentmethod=document["PaymentMethod"],
            product=document["Product"]
        )
    )

    with engine.connect() as conn:
        res = conn.execute(stmt)
        conn.commit()

def update_sql(document: dict):
    stmt = (
        update(TABLE_TRANSACTIONS)
        .where(TABLE_TRANSACTIONS.c.codcli == document["CodCli"])
        .values(
            codcli=document["CodCli"],
            cpf=document["Cpf"],
            name=document["Name"],
            price=document["Price"],
            company=document["Company"],
            paymentmethod=document["PaymentMethod"],
            product=document["Product"]
        )
    )

    with engine.connect() as conn:
        res = conn.execute(stmt)
        conn.commit()

def delete_sql(codcli: int):
    stmt = (
        delete(TABLE_TRANSACTIONS)
        .where(TABLE_TRANSACTIONS.c.codcli == codcli)
    )

    with engine.connect() as conn:
        res = conn.execute(stmt)
        conn.commit()
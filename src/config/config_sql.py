import os
from sqlalchemy import create_engine, Column, Table, INTEGER, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base

link_database = os.environ.get('LINK_DATABASE_SQL', "must_be_set_in_env")

engine = create_engine(link_database)

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
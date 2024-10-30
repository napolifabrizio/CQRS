import os
from sqlalchemy import create_engine, Column, Table, INTEGER, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base

class ConfigSql():
    def __init__(self):
        self._base = declarative_base()
        self._linkDatabase = os.environ.get('LINK_DATABASE_SQL', "must_be_set_in_env")

    def engine(self):
        engine = create_engine(self._linkDatabase)
        return engine

    def table(self):
        table = Table(
            "transactions",
            self._base.metadata,
            Column("codcli", INTEGER, primary_key=True),
            Column("cpf", VARCHAR(30), nullable=False),
            Column("name", VARCHAR(100), nullable=False),
            Column("price", FLOAT, nullable=False),
            Column("company", VARCHAR(50), nullable=False),
            Column("paymentmethod", VARCHAR(20), nullable=False),
            Column("product", VARCHAR(30), nullable=True)
        )
        return table
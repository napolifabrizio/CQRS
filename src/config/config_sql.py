import os
from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, FLOAT
from sqlalchemy.engine import URL
from sqlalchemy.schema import Table, MetaData

class ConfigSql():
    def __init__(self):
        pass

    def engine(self):
        url = URL.create(
            drivername="postgresql",
            host=os.environ.get("POSTGRE_HOST"),
            port=os.environ.get("POSTGRE_PORT"),
            username=os.environ.get("POSTGRE_USERNAME"),
            password=os.environ.get("POSTGRE_PASSWORD"),
            database=os.environ.get("POSTGRE_DATABASE"),
        )
        engine = create_engine(url)
        return engine

    def table(self):
        table = Table(
            "Transactions",
            MetaData(),
            Column("CodCli", INTEGER, primary_key=True),
            Column("Cpf", VARCHAR(30), nullable=False),
            Column("Name", VARCHAR(100), nullable=False),
            Column("Price", FLOAT, nullable=False),
            Column("Company", VARCHAR(50), nullable=False),
            Column("PaymentMethod", VARCHAR(20), nullable=False),
            Column("Product", VARCHAR(30), nullable=True)
        )
        return table
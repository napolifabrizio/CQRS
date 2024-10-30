
from sqlalchemy import insert, delete, select, update

class RepoSql():

    def __init__(self, engine, table):
        self._engine = engine
        self._table = table

    def insert_sql(self, document: dict):
        stmt = (
            insert(self._table)
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

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()

    def update_sql(self, document: dict):
        stmt = (
            update(self._table)
            .where(self._table.c.codcli == document["CodCli"])
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

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()

    def delete_sql(self, codcli: int):
        stmt = (
            delete(self._table)
            .where(self._table.c.codcli == codcli)
        )

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()


    def select_sql(self, codcli: int):
        stmt = (
            select(self._table)
            .where(self._table.c.codcli == codcli)
        )

        with self._engine.connect() as conn:
            for row in conn.execute(stmt):
                return row
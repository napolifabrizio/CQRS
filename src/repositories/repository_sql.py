
import json
from sqlalchemy import insert, delete, select, update
from config.config_sql import ConfigSql
from models.Transaction import Transaction

class SqlRepo():

    def __init__(self, config: ConfigSql):
        self._engine = config.engine()
        self._table = config.table()

    def insert_sql(self, document: dict):
        stmt = (
            insert(self._table)
            .values(document)
        )

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()

    def update_sql(self, document: dict):
        stmt = (
            update(self._table)
            .where(self._table.c.codcli == document["CodCli"])
            .values(document)
        )

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()

    def delete_sql(self, codcli: int):
        stmt = (
            delete(self._table)
            .where(self._table.c.CodCli == codcli)
        )

        with self._engine.connect() as conn:
            res = conn.execute(stmt)
            conn.commit()


    def select_sql(self, codcli: int):
        stmt = (
            select(self._table)
            .where(self._table.c.Codcli == codcli)
        )

        with self._engine.connect() as conn:
            for row in conn.execute(stmt):
                return row
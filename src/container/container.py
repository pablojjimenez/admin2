import sqlite3
from abc import ABC, abstractmethod
from model.IlegalArgumentError import IllegalArgumentsError
from utils import get_epoch, next_month, MONTHS_NAMES


class Container(ABC):
    def __init__(self, **kwargs):
        """
        :params: db, name, opc:schema
        """
        self.sql_insert = "INSERT INTO {table} ({fields}) VALUES ({values});"
        state = 'db' and 'name' in kwargs.keys()
        if not state: raise (IllegalArgumentsError('ntable and db mandatory!'))
        self.ntable = kwargs.get('name')
        self.conn = sqlite3.connect(kwargs.get('db'))
        self.schema = kwargs.get('schema')
        if 'schema' in kwargs.keys():
            self._create_schema(self.schema)

    def _create_schema(self, schema: str):
        try:
            self.conn.cursor().execute(schema)
        except:
            pass

    def insert(self, obj):
        fields = [i for i in obj._dir()]
        values = [getattr(obj, f) for f in fields]

        f = self.sql_insert.format(
            table=self.ntable,
            fields=str(fields)[1:-1],
            values=str(values)[1:-1]
        )
        self.conn.cursor().execute(f)
        self.conn.commit()

    def list(self, month: int = None):
        if month:
            sql = f'SELECT * FROM {self.ntable} WHERE fecha>={get_epoch(1, month)} AND fecha<{get_epoch(1, next_month(month))} '
        else:
            sql = f'SELECT * FROM {self.ntable}'
        iter = self.conn.cursor().execute(sql)
        return iter.fetchall()

    def count_list(self) -> int:
        r = self.conn.cursor().execute(f'select count(*) from {self.ntable};')
        return r.fetchall()[0][0]

    def sum(self, month=None) -> int:
        if month:
            str = f'select sum(precio) from {self.ntable} where fecha>={get_epoch(1, month)} and fecha<{get_epoch(1, next_month(month))}'
        else:
            str = f'select sum(precio) from {self.ntable}'
        r = self.conn.cursor().execute(str)
        sum = r.fetchall()[0][0]
        return sum if sum is not None else 0.0

    def reset_table(self):
        self.conn.execute(f'DROP TABLE IF EXISTS {self.ntable}')
        self.conn.commit()
        self._create_schema(self.schema)
        self.conn.commit()

    def count_group(self):
        expected = {}
        mes = 1
        for i in MONTHS_NAMES:
            expected.setdefault(i, self.sum(mes))
            mes += 1
        return expected



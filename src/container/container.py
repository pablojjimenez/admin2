import sqlite3
from abc import ABC, abstractmethod
from src.model.IlegalArgumentError import IllegalArgumentsError
from src.utils import get_epoch, next_month


class Container(ABC):
    def __init__(self, **kwargs):
        """
        :params: db, name, opc:schema
        """
        self.sql_insert = "INSERT INTO {table} ({fields}) VALUES ({values});"
        self.sql_select = "SELECT * FROM {table} WHERE fecha>={fi} AND fecha<{ff}"
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

    def list(self):
        f = self.sql_select.format(
            table=self.ntable,
            fi=get_epoch(1),
            ff=get_epoch(1, next_month())
        )
        iter = self.conn.cursor().execute(f)
        return iter.fetchall()

    def count_list(self) -> int:
        r = self.conn.cursor().execute(f'select count(*) from {self.ntable};')
        return r.fetchall()[0][0]

    @abstractmethod
    def sum(self):
        pass

    def reset_table(self):
        self.conn.execute(f'DROP TABLE IF EXISTS {self.ntable}')
        self.conn.commit()
        self._create_schema(self.schema)
        self.conn.commit()

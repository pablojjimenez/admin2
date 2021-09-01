from typing import Dict
from src.color import C
from src.factories import AbstractFactory
from src.model.model import Model
from src.utils import today_epoch
from rich.console import Console
from rich.table import Table
from rich import box

class Controller:

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    @classmethod
    def _ask_for_data(cls, data: Model) -> Dict:
        dat = {}
        print(C.KYEL)
        for d in data._dir():
            dat.setdefault(d, None)
            dat[d] = input('%12s : ' % d.upper())
            if not dat[d]:
                dat[d] = today_epoch()
        print(C.RST)
        return dat

    def _show_data(self, header_names:[], v: []):
        console = Console()
        table = Table(show_header=True, header_style="bold blue", box=box.ROUNDED)
        for i in header_names:
            table.add_column(i.upper())
        for i in v:
            content = i.get_tuple()
            table.add_row(*content)

        console.print(table)

    def insertar(self):
        data_model = self.factory.create_model()
        dat = Controller._ask_for_data(data_model)
        data_model._fill(dat)
        self.factory.create_container().insert(data_model)

    def listar(self):
        v = self.factory.create_container().list()
        v = [self.factory.create_model().from_tuple(i) for i in v]
        self._show_data(self.factory.create_model()._dir(), v)

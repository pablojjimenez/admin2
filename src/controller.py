from typing import Dict
from src.color import C
from src.factories import AbstractFactory
from src.utils import today_epoch, current_month
from rich.console import Console
from rich.table import Table
from rich import box


class Controller:
    def __init__(self, factory: AbstractFactory):
        self.container = factory.create_container()
        self.model = factory.create_model()

    def _ask_for_data(self) -> Dict:
        print(C.KCYN + self.container.show_before_insert())
        dat = {}
        print(C.KYEL)
        for d in self.model._dir():
            dat.setdefault(d, None)
            if d != 'fecha':
                dat[d] = input('%12s : ' % d.upper())
            else:
                dat[d] = today_epoch()
        print(C.RST)
        return dat

    def _show_data(self, header_names: [], v: [], month: int = current_month()):
        console = Console()
        table = Table(show_header=True, header_style="bold blue", box=box.SIMPLE_HEAVY, show_footer=True)
        first = True
        for i in header_names:
            if first:
                table.add_column(i.upper(), footer=f'[bold blue]{self.container.sum(month)}€[/bold blue]')
                first = False
            else:
                table.add_column(i.upper())
        for i in v:
            content = i.get_tuple()
            table.add_row(*content)

        console.print(table)

    def insertar(self):
        dat = self._ask_for_data()
        self.model._fill(dat)
        self.container.insert(self.model)

    def listar(self, month: int = current_month()):
        model_list = self.container.list(month)
        model_list = [self.model.from_tuple(i) for i in model_list]
        self._show_data(self.model._dir(), model_list, month)

    def sum_prince(self, mes=None) -> float:
        return round(self.container.sum(mes), 2)

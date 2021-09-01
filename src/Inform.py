from rich.console import Console
from rich.table import Table
from rich import box

from src.color import C
from src.controller import Controller
from src.factories import IngresoFactory, ClaseFactory
from src.utils import MONTHS_NAMES, current_month


class Inform:

    def show_inf(self):
        self.show_info_month()
        self.show_info_all()

    def show_info_all(self):
        ganado = Controller(IngresoFactory()).sum_prince() + Controller(ClaseFactory()).sum_prince()
        ganado = round(ganado, 2)
        console = Console()
        table = Table(title=f'{C.UNDL}{C.KCYN}INFORME ABSOLUTO',
                      box=box.MINIMAL_HEAVY_HEAD, show_footer=True, show_header=False)
        table.add_column(footer='[dodger_blue2]RESTO [/dodger_blue2]', width=12)
        table.add_column(footer='[dodger_blue2]200 €[/dodger_blue2]', width=12)
        table.add_row('[green]GANADO[/green]', f'[green]{ganado} €[/green]')
        table.add_row('[red]GASTADO[/red]', '[red]200 €[/red]')
        console.print(table)

    def show_info_month(self):
        ganado = Controller(IngresoFactory()).sum_prince(current_month()) + Controller(ClaseFactory()).sum_prince(current_month())

        console = Console()
        table = Table(title=f'{C.UNDL}{C.KCYN}INFORME DE {MONTHS_NAMES[current_month() - 1]}',
                      box=box.MINIMAL_HEAVY_HEAD, show_footer=True, show_header=False)
        table.add_column(footer='[dodger_blue2]RESTO [/dodger_blue2]', width=12)
        table.add_column(footer='[dodger_blue2]200 €[/dodger_blue2]', width=12)
        table.add_row('[green]GANADO[/green]', f'[green]{ganado} €[/green]')
        table.add_row('[red]GASTADO[/red]', '[red]200 €[/red]')
        console.print(table)
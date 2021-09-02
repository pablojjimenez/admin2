from rich.console import Console
from rich.table import Table
from rich import box
from src.color import C
from src.controller import Controller
from src.factories import IngresoFactory, ClaseFactory, GastoFactory
from src.utils import MONTHS_NAMES, current_month


class Inform:

    def show_inf(self):
        self.show_info_all()

    def show_info_all(self):
        ingresos = Controller(IngresoFactory())
        clases = Controller(ClaseFactory())
        gastos = Controller(GastoFactory())
        console = Console()
        table = Table(
            title='INFORME ABSOLUTO',
            box=box.ROUNDED,
            show_footer=True,
            show_header=True
        )

        total = round(ingresos.sum_prince()+clases.sum_prince(), 2)
        total2= gastos.sum_prince()
        save= total - total2
        table.add_column(footer='[dodger_blue2]TOTAL [/dodger_blue2]', width=12, justify="right")
        table.add_column('ganado (i, c)', footer=f'[dodger_blue2] {total} € [/dodger_blue2]', width=20)
        table.add_column('gastado', footer=f'[red] {total2}€ [/red]', justify='center')
        table.add_column('resto', footer=f'[green] {save}€ [/green]', width=12)
        for month in range(len(MONTHS_NAMES)):
            g1 = ingresos.sum_prince(month+1)
            g2 = clases.sum_prince(month+1)

            str = '[green]{:>{w}}€ {:>{w}}€[/green]'.format(g1, g2, w=8)
            gastado = f'[red]{gastos.sum_prince(month+1)}€[/red]'
            left = f'[dark_orange]{round((g1+g2)-gastos.sum_prince(month+1), 2)}€[/dark_orange]'
            table.add_row(MONTHS_NAMES[month], str, gastado, left)

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
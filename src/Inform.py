from rich.console import Console
from rich.table import Table
from rich import box

from src.color import C
from src.utils import MONTHS_NAMES, current_month


class Inform:

    def show_inf(self):
        console = Console()
        table = Table(title=f'{C.UNDL}{C.KCYN}INFORME DE {MONTHS_NAMES[current_month()-1]}', box=box.MINIMAL_HEAVY_HEAD, show_footer=True, show_header=False)
        table.add_column(footer='RESTO €',width=12)
        table.add_column(footer='200 €', width=12)
        print(C.KGRN)
        table.add_row('GANADO', '200 €')
        print(C.RST)
        table.add_row(C.KRED+'GASTADO'+C.RST, '200 €')
        console.print(table)


import sys
from platform import system
from src.color import C
from src.controller import Controller
from src.factories import GastoFactory, IngresoFactory


def handler(arg):
    if arg == 'ig':
        Controller(GastoFactory()).insertar()
    elif arg == 'lg':
        Controller(GastoFactory()).listar()
    elif arg == 'ii':
        Controller(IngresoFactory()).insertar()
    elif arg == 'li':
        Controller(IngresoFactory()).listar()


def clean():
    os_name = sys.platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':
    sms = f'''{C.KMAG}
        1. gastos.          (ig, lg)
        2. ingresos.        (ii, li)
        3. clases.          (ic, lc)
        4. informe.         (inf)
        5. clases por mes.  (infc) 
        {C.RST}
        '''
    clean()
    if len(sys.argv) > 1:
        handler(sys.argv[1])
    else:
        print(sms)

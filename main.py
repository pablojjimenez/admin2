import sys
import os
from src.color import C
from src.controller import Controller
from src.factories import GastoFactory, IngresoFactory, ClaseFactory, AlumnoFactory


def handler(arg):
    if arg == 'ig':
        Controller(GastoFactory()).insertar()
    elif arg == 'lg':
        Controller(GastoFactory()).listar()
    elif arg == 'ii':
        Controller(IngresoFactory()).insertar()
    elif arg == 'li':
        Controller(IngresoFactory()).listar()
    elif arg == 'ic':
        Controller(ClaseFactory()).insertar()
    elif arg == 'lc':
        Controller(ClaseFactory()).listar()
    elif arg == 'ia':
        Controller(AlumnoFactory()).insertar()
    elif arg == 'la':
        Controller(AlumnoFactory()).listar()


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    sms = '''{}
        1. gastos.          (ig, lg)
        2. ingresos.        (ii, li)
        3. clases.          (ic, lc)
        4. informe.         (inf)
        5. clases por mes.  (infc) 
        {}
    '''.format(C.KMAG, C.RST)
    clean()

    if len(sys.argv) > 1:
        handler(sys.argv[1])
    else:
        print(sms)

import sys
import os

from src.Inform import Inform
from src.color import C
from src.controller import Controller
from src.factories import GastoFactory, IngresoFactory, ClaseFactory, AlumnoFactory, HistoryFactory


def handler(arg):
    if len(sys.argv) == 2:
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
        elif arg == 'inf':
            Inform().show_inf()
        elif arg == 'h':
            Controller(HistoryFactory()).listar()
        elif arg == 'ih':
            Controller(HistoryFactory()).insertar()
    else:
        if arg == 'lg':
            Controller(GastoFactory()).listar(int(sys.argv[2]))
        elif arg == 'li':
            Controller(IngresoFactory()).listar(int(sys.argv[2]))
        elif arg == 'lc':
            Controller(ClaseFactory()).listar(int(sys.argv[2]))
        elif arg == 'la':
            Controller(AlumnoFactory()).listar(int(sys.argv[2]))


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    sms = '''{}
        1. gastos.          (ig, lg)
        2. ingresos.        (ii, li)
        3. clases.          (ic, lc)
        4. alumnos.         (ia, la)
        5. histotial.       (ih, h) 
        6. informe.         (inf)
        7. clases por mes.  (infc) 
        {}
    '''.format(C.KMAG, C.RST)
    clean()

    if len(sys.argv) > 1:
        handler(sys.argv[1])
    else:
        print(sms)

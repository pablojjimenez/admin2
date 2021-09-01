from src.controller import Controller
from src.factories import IngresoFactory


c = Controller(IngresoFactory())

c.insertar()
c.listar()

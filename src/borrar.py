from src.controller import Controller
from src.factories import IngresoFactory, GastoFactory

c = Controller(GastoFactory())

c.insertar()
c.listar()

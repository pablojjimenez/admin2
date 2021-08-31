from typing import Dict

from src.color import C
from src.factories import AbstractFactory
from src.model.model import Model


class Controller:

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def _ask_for_data(self, data: Model) -> Dict:
        dat = {}
        print(C.KYEL)
        for d in data._dir():
            dat.setdefault(d, None)
            dat[d] = input('%12s : ' % d.upper())
        return dat

    def _show_data(self, v: []):
        pass

    def insertar(self):
        data_model = self.factory.create_model()

        dat = self._ask_for_data(data_model)
        data_model._fill(dat)
        print(data_model)
       # self.factory.create_container().insert(data_model)

    def listar(self):
        v = self.factory.create_container().list()
        self._show_data(v)

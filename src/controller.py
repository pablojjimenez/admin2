from typing import Dict
from src.color import C
from src.factories import AbstractFactory
from src.model.model import Model
from src.utils import today_epoch


class Controller:

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    @classmethod
    def _ask_for_data(cls, data: Model) -> Dict:
        dat = {}
        print(C.KYEL)
        for d in data._dir():
            dat.setdefault(d, None)
            dat[d] = input('%12s : ' % d.upper())
            if not dat[d]:
                dat[d] = today_epoch()
        print(C.RST)
        return dat

    def _show_data(self, v: []):
        for i in v: print(i)

    def insertar(self):
        data_model = self.factory.create_model()
        dat = Controller._ask_for_data(data_model)
        data_model._fill(dat)
        self.factory.create_container().insert(data_model)

    def listar(self):
        v = self.factory.create_container().list()
        v = [self.factory.create_model().from_tuple(i) for i in v]
        self._show_data(v)

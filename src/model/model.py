from typing import Iterable, Dict


class Model:
    def __init__(self, data: Dict):
        if data: self._fill_attrs(data)

    def _dir(self) -> Iterable[str]:
        return list(filter(lambda x: x[:1] != '_', self.__dir__()))

    def _fill_attrs(self, data: Dict):
        for i in data.keys():
            setattr(self, i, data.get(i))

class IngresoM(Model):
    def __init__(self, data: Dict = None):
        self.ingreso = None
        self.concepto = None
        self.fecha = None
        self.pagador = None
        super().__init__(data)

    def fill(self):
        print('arreglameeee')
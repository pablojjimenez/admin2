from typing import Dict

from src.model.model import Model


class IngresoM(Model):
    def __init__(self, data: Dict = None):
        self.ingreso = None
        self.concepto = None
        self.fecha = None
        self.pagador = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_params(cls, ingreso, concepto, fecha, pagador):
        return cls({
            'ingreso': ingreso,
            'concepto': concepto,
            'fecha': fecha,
            'pagador': pagador
        })

    def __str__(self) -> str:
        return super().__str__()

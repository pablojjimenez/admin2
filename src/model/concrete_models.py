from typing import Dict, Tuple
from src.model.model import Model
from src.utils import translate_from_epoch


class IngresoM(Model):
    def __init__(self, data: Dict = None):
        self.precio = None
        self.concepto = None
        self.fecha = None
        self.pagador = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_tuple(cls, tuple: Tuple):
        return cls({
            'precio': tuple[1],
            'concepto': tuple[2],
            'fecha': translate_from_epoch(tuple[3]),
            'pagador': tuple[4]
        })

    def __str__(self) -> str:
        return super().__str__()


class GastoM(Model):
    def __init__(self, data: Dict = None):
        self.precio = None
        self.establecimiento = None
        self.fecha = None
        self.comentario = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_tuple(cls, tuple: Tuple):
        return cls({
            'precio': tuple[1],
            'establecimiento': tuple[2],
            'fecha': translate_from_epoch(tuple[3]),
            'comentario': tuple[4]
        })

    def __str__(self) -> str:
        return super().__str__()


class AlumnoM(Model):
    def __init__(self, data: Dict = None):
        self.nombre = None
        self.tlf = None
        self.mail = None
        self.estudios = None
        self.comentarios = None
        self.activo = None
        self.precio = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_tuple(cls, tuple: Tuple):
        return cls({
            'nombre': tuple[1],
            'tlf': tuple[2],
            'mail': tuple[3],
            'estudios': tuple[4],
            'comentarios': tuple[5],
            'activo': tuple[6],
            'precio': tuple[7]
        })

    def __str__(self) -> str:
        return super().__str__()


class ClaseM(Model):
    def __init__(self, data: Dict = None):
        self.alumno = None
        self.tech = None
        self.duracion = None
        self.precio = None
        self.fecha = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_tuple(cls, tuple: Tuple):
        return cls({
            'alumno': tuple[1],
            'tech': tuple[2],
            'duracion': tuple[3],
            'precio': tuple[4],
            'fecha': translate_from_epoch(tuple[5]),
        })

    def __str__(self) -> str:
        return super().__str__()


class HistoryM(Model):
    def __init__(self, data: Dict = None):
        self.txt = None
        self.fecha = None
        super().__init__(data)

    def _fill(self, data: Dict):
        super()._fill_attrs(data)

    @classmethod
    def from_tuple(cls, tuple: Tuple):
        return cls({
            'txt': tuple[1],
            'fecha': tuple[2],
        })

    def __str__(self) -> str:
        return super().__str__()

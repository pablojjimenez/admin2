from typing import Dict

from src.model.model import Model


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
    def from_params(cls, ingreso, concepto, fecha, pagador):
        return cls({
            'precio': ingreso,
            'concepto': concepto,
            'fecha': fecha,
            'pagador': pagador
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
    def from_params(cls, ingreso, concepto, fecha, pagador):
        return cls({
            'precio': ingreso,
            'establecimiento': concepto,
            'fecha': fecha,
            'comentario': pagador
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
    def from_params(cls, nombre, tlf, mail, estudios, comentarios, activo, precio):
        return cls({
            'nombre': nombre,
            'tlf': tlf,
            'mail': mail,
            'estudios': estudios,
            'comentarios': comentarios,
            'activo': activo,
            'precio': precio
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
    def from_params(cls, alumno, tech, duracion, precio, fecha):
        return cls({
            'alumno': alumno,
            'tech': tech,
            'duracion': duracion,
            'precio': precio,
            'fecha': fecha,
        })

    def __str__(self) -> str:
        return super().__str__()

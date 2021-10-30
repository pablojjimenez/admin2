from abc import ABC, abstractmethod
from src.container.container import Container
from src.container.concrete_containers import IngresoCont, GastosCont, ClaseCont, AlumnosCont, HistoryCont
from src.db_schemas import INGRESOS_SH, GASTOS_SH, ALUMNOS_SH, CLASES_SH
from src.model.concrete_models import IngresoM, GastoM, ClaseM, AlumnoM, HistoryM
from src.model.model import Model


class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self) -> Container:
        pass

    @abstractmethod
    def create_model(self) -> Model:
        pass


DB_NAME = '/Users/pablojj/MEGA/admin/nueva_bd_2.db'


class IngresoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return IngresoCont(schema=INGRESOS_SH, db=DB_NAME, name='Ingresos')

    def create_model(self) -> Model:
        return IngresoM()


class GastoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return GastosCont(schema=GASTOS_SH,db=DB_NAME, name='Gastos')

    def create_model(self) -> Model:
        return GastoM()


class ClaseFactory(AbstractFactory):
    def create_container(self) -> Container:
        return ClaseCont(schema=CLASES_SH,db=DB_NAME, name='Clases')

    def create_model(self) -> Model:
        return ClaseM()


class AlumnoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return AlumnosCont(schema=ALUMNOS_SH, db=DB_NAME, name='Alumnos')

    def create_model(self) -> Model:
        return AlumnoM()


class HistoryFactory(AbstractFactory):
    def create_container(self) -> Container:
        return HistoryCont(db=DB_NAME, name='History')

    def create_model(self) -> Model:
        return HistoryM()

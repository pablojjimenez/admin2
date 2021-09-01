from abc import ABC, abstractmethod
from container.container import Container
from container.concrete_containers import IngresoCont, GastosCont
from model.concrete_models import IngresoM, GastoM
from model.model import Model


class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self) -> Container:
        pass

    @abstractmethod
    def create_model(self) -> Model:
        pass


schema = '''CREATE TABLE "Ingresos" (
	"id"	INTEGER NOT NULL,
	"ingreso"	REAL NOT NULL,
	"concepto"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"pagador"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)'''


class IngresoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return IngresoCont(db='test.db', name='Ingresos', schema=schema)

    def create_model(self) -> Model:
        return IngresoM()


class GastoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return GastosCont(db='test.db', name='Gastos', schema=schema)

    def create_model(self) -> Model:
        return GastoM()

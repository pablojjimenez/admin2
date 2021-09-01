from abc import ABC, abstractmethod
from src.container.container import Container
from src.container.concrete_containers import IngresoCont
from src.model.concrete_models import IngresoM
from src.model.model import Model


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

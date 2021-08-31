from abc import ABC, abstractmethod
from src.container import Container
from src.model.model import Model, IngresoM


class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self) -> Container:
        pass

    @abstractmethod
    def create_model(self) -> Model:
        pass


class IngresoCont:
    pass


class IngresoFactory(AbstractFactory):
    def create_container(self) -> Container:
        return IngresoCont()

    def create_model(self) -> Model:
        return IngresoM()

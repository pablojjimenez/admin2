from abc import abstractmethod, ABC
from typing import Iterable, Dict

from src.color import C


class Model(ABC):
    def __init__(self, data: Dict):
        if data: self._fill_attrs(data)

    def _dir(self) -> Iterable[str]:
        return list(filter(lambda x: x[:1] != '_' and '_' not in x, self.__dir__()))

    def _fill_attrs(self, data: Dict):
        for i in data.keys():
            setattr(self, i, data.get(i))

    @abstractmethod
    def _fill(self, data: Dict):
        pass

    def __str__(self) -> str:
        out = f'{C.FBLU} {C.BOLD} {C.KWHT}'
        for i in self._dir():
            prop = getattr(self, i)
            out += '{:>{w}}'.format(prop, w=20)
        out += '{:>{w}}'.format(C.RST, w=20)
        return out

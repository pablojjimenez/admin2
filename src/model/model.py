from typing import Iterable, Dict


class Model:
    def __init__(self, data: Dict):
        for i in data.keys():
            setattr(self, i, data.get(i))

    def _dir(self) -> Iterable[str]:
        return list(filter(lambda x: x[:1] != '_', self.__dir__()))

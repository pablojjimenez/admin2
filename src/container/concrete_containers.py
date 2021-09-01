from src.container.container import Container


class IngresoCont(Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def sum(self):
        v = super().list()
        return sum(i[1] for i in v)

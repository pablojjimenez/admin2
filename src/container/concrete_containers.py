from src.container import Container


class IngresoCont(Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GastosCont(Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AlumnosCont(Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ClaseCont(Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def most_techs_money(self):
        iter = self.conn.cursor().execute('select tech, sum(precio) from Clases GROUP by tech;')
        f = open('f.txt', 'w')
        f.write(str(iter))
        out = {key: tuple(rest) for key, rest in iter}

        f.write(str(out))

        return sorted(out)
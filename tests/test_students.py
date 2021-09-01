import pytest
from src.container.concrete_containers import AlumnosCont
from src.db_schemas import ALUMNOS_SH
from src.model.concrete_models import GastoM, AlumnoM

OBJS = [
    AlumnoM.from_params('name', 637263547, 'algo@gmail.com', 'info', 'comment', 1, 9),
    AlumnoM.from_params('name2', 637263547, 'algo@gmail.com', 'info', 'comment', 1, 10),
]

@pytest.fixture
def test_db():
    cont = AlumnosCont(db='TEST_DB.db', name='Alumnos', schema=ALUMNOS_SH)
    cont.reset_table()
    for i in OBJS:
        cont.insert(i)
    return cont


@pytest.mark.usefixtures('test_db')
class TestAlumnos:

    def test_empty_model(self, test_db):
        assert test_db.count_list() == 2

    def test_list(self, test_db):
        ing = test_db.list()
        ing = AlumnoM.from_params(ing[0][1], ing[0][2], ing[0][3], ing[0][4], ing[0][5], ing[0][6], ing[0][7])
        assert ing.precio == OBJS[0].precio
        assert ing.mail == OBJS[0].mail

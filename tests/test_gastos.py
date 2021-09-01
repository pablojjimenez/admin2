import pytest
from src.container.concrete_containers import GastosCont
from src.model.concrete_models import GastoM
from src.utils import today_epoch, get_epoch, current_month, MONTHS_NAMES

s = '''
CREATE TABLE "Gastos" (
	"id"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"establecimiento"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"comentario"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''

OBJS = [
    GastoM.from_params(10, 'establec', today_epoch(), 'comment'),
    GastoM.from_params(20, 'establec1', today_epoch(), 'comment'),
    GastoM.from_params(1, 'establec', today_epoch(), 'comment'),
    GastoM.from_params(10.33, 'establec2', today_epoch(), 'comment'),
    GastoM.from_params(10.1, 'establec3', get_epoch(10, 8, 2021), 'comment'),
]


@pytest.fixture
def test_db():
    cont = GastosCont(db='TEST_DB.db', name='Gastos', schema=s)
    cont.reset_table()
    for i in OBJS:
        cont.insert(i)
    return cont


@pytest.mark.usefixtures('test_db')
class TestGastos:

    def test_empty_model(self, test_db):
        assert test_db.count_list() == 5

    def test_sum(self, test_db):
        assert test_db.sum() == 51.43

    def test_sum_this_month(self, test_db):
        assert test_db.sum(current_month()) == 41.33

    def test_sum_1_month(self, test_db):
        assert test_db.sum(1) == 0.0

    def test_list(self, test_db):
        ing = test_db.list()
        ing = GastoM.from_params(ing[3][1], ing[3][2], ing[3][3], ing[3][4])
        assert ing.precio == OBJS[3].precio
        assert ing.fecha == OBJS[3].fecha

    def test_sum_group_month(self, test_db):
        expected = {}
        for i in MONTHS_NAMES:
            expected.setdefault(i, 0)
        expected[MONTHS_NAMES[current_month() - 1]] = 41.33
        expected['AGOSTO'] = 10.1

        assert expected == test_db.count_group()


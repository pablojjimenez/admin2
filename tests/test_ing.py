import pytest

from src.container.concrete_containers import IngresoCont
from src.model.concrete_models import IngresoM
from src.utils import today_epoch, get_epoch, current_month, MONTHS_NAMES

s = '''
CREATE TABLE "Ingresos" (
	"id"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"concepto"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"pagador"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''

OBJS = [
    IngresoM.from_params(10, 'conceto', today_epoch(), 'pagador'),
    IngresoM.from_params(20, 'conceto', today_epoch(), 'pagador'),
    IngresoM.from_params(1, 'conceto', today_epoch(), 'pagador'),
    IngresoM.from_params(10.33, 'conceto', today_epoch(), 'pagador'),
    IngresoM.from_params(10.1, 'conceto', get_epoch(10, 8, 2021), 'pagador'),
]


@pytest.fixture
def test_db():
    cont = IngresoCont(db='TEST_DB.db', name='Ingresos', schema=s)
    cont.reset_table()
    for i in OBJS:
        cont.insert(i)
    return cont


@pytest.mark.usefixtures('test_db')
class TestIngresos:

    def test_empty_model(self, test_db):
        assert test_db.count_list() == 5

    def test_sum(self, test_db):
        assert test_db.sum() == 51.43

    def test_sum_this_month(self, test_db):
        assert test_db.sum(current_month()) == 41.33

    def test_sum_1_month(self, test_db):
        assert test_db.sum(1) == 0.0

    def test_list(self, test_db):
        ing = IngresoM.from_params(
            test_db.list()[3][1],
            test_db.list()[3][2],
            test_db.list()[3][3],
            test_db.list()[3][4]
        )
        assert ing.precio == OBJS[3].precio
        assert ing.fecha == OBJS[3].fecha

    def test_sum_group_month(self, test_db):
        expected = {}
        for i in MONTHS_NAMES:
            expected.setdefault(i, 0)
        expected[MONTHS_NAMES[current_month()-1]] = 41.33
        expected['AGOSTO'] = 10.1

        assert expected == test_db.count_group()

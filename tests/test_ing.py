import pytest
from src.container.concrete_containers import IngresoCont
from src.model.concrete_models import IngresoM
from src.utils import today_epoch, get_epoch

s = '''
CREATE TABLE "Ingresos" (
	"id"	INTEGER NOT NULL,
	"ingreso"	REAL NOT NULL,
	"concepto"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"pagador"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''


@pytest.fixture
def test_db():
    objs = [
        IngresoM.from_params(10, 'conceto', today_epoch(), 'pagador'),
        IngresoM.from_params(20, 'conceto', today_epoch(), 'pagador'),
        IngresoM.from_params(1, 'conceto', today_epoch(), 'pagador'),
        IngresoM.from_params(10.33, 'conceto', today_epoch(), 'pagador'),
        IngresoM.from_params(10.33, 'conceto', get_epoch(10, 8, 2021), 'pagador'),
    ]
    cont = IngresoCont(db='TEST_DB.db', name='Ingresos', schema=s)
    cont.reset_table()
    for i in objs:
        cont.insert(i)
    return cont


@pytest.mark.usefixtures('test_db')
class TestIngresos:

    def test_empty_model(self, test_db):
        assert test_db.count_list() == 4

    def test_sum(self, test_db):
        assert test_db.sum() == 41.33

    def test_sum_this_month(self, test_db):
        pass

    def test_list(self, test_db):
        pass

    def test_sum_group_month(self, test_db):
        pass


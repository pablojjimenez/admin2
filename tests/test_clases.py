import pytest
from src.container.concrete_containers import GastosCont, ClaseCont
from src.db_schemas import CLASES_SH
from src.model.concrete_models import GastoM, ClaseM
from src.utils import today_epoch, get_epoch, current_month, MONTHS_NAMES


OBJS = [
    ClaseM.from_params(1, 'JAVA', 60, 9, today_epoch()),
    ClaseM.from_params(1, 'JAVA', 60, 9, today_epoch()),
    ClaseM.from_params(1, 'SQL', 60, 9, today_epoch()),
    ClaseM.from_params(2, 'PHP', 60, 9, today_epoch()),
    ClaseM.from_params(3, 'C++', 60, 9, get_epoch(8, 8)),
]


@pytest.fixture
def test_db():
    cont = ClaseCont(db='TEST_DB.db', name='Clases', schema=CLASES_SH)
    cont.reset_table()
    for i in OBJS:
        cont.insert(i)
    return cont


@pytest.mark.usefixtures('test_db')
class TestClases:

    def test_empty_model(self, test_db):
        assert test_db.count_list() == 5

    def test_sum(self, test_db):
        assert test_db.sum() == 45

    def test_sum_this_month(self, test_db):
        assert test_db.sum(current_month()) == 36

    def test_sum_1_month(self, test_db):
        assert test_db.sum(1) == 0.0

    def test_list(self, test_db):
        ing = test_db.list()
        ing = ClaseM.from_params(ing[3][1], ing[3][2], ing[3][3], ing[3][4], ing[3][5])
        assert ing.precio == OBJS[3].precio
        assert ing.fecha == OBJS[3].fecha

    def test_sum_group_month(self, test_db):
        expected = {}
        for i in MONTHS_NAMES:
            expected.setdefault(i, 0)
        expected[MONTHS_NAMES[current_month() - 1]] = 36
        expected['AGOSTO'] = 9

        assert expected == test_db.count_group()

    def test_most_techs_money(self, test_db):
        # expected = {
        #     'JAVA': 2*9,
        #     'SQL': 9,
        #     'PHP': 9,
        #     'C++': 9
        # }
        # assert expected == test_db.most_techs_money()
        pass

    def test_group_hours_months(self, test_db):
        # expected = {}
        # for i in MONTHS_NAMES:
        #     expected.setdefault(i, 0)
        # expected[MONTHS_NAMES[current_month() - 1]] = 240
        # expected['AGOSTO'] = 60
        #
        # assert expected == test_db.count_group_hours_months()
        pass
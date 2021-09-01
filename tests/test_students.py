import pytest
from src.container.concrete_containers import AlumnosCont
from src.model.concrete_models import GastoM, AlumnoM

s = '''
CREATE TABLE "Alumnos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"tlf"	INTEGER NOT NULL,
	"mail"	TEXT,
	"estudios"	TEXT,
	"comentarios"	TEXT,
	"activo"	INTEGER DEFAULT 1,
	"precio"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''

OBJS = [
    AlumnoM.from_params('name', 637263547, 'algo@gmail.com', 'info', 'comment', 1, 9),
    AlumnoM.from_params('name2', 637263547, 'algo@gmail.com', 'info', 'comment', 1, 10),
]


@pytest.fixture
def test_db():
    cont = AlumnosCont(db='TEST_DB.db', name='Alumnos', schema=s)
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

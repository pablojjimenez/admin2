from sqlite3 import connect

conn = connect('/Users/pablojj/MEGA/admin/nueva_bd_2.db')
curs = conn.cursor()

conn1 = connect('/Users/pablojj/MEGA/admin/miData2.db')
curs1 = conn1.cursor()

"""curs.execute(
    '''CREATE TABLE "Alumnos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"tlf"	INTEGER NOT NULL,
	"mail"	TEXT,
	"estudios"	TEXT,
	"comentarios"	TEXT,
	"activo"	INTEGER DEFAULT 1,
	"precio"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
)'''
)
"""
a = curs1.execute('select * from Alumnos;')
b=a.fetchall()
for i in b:
    curs1.execute('insert into Alumnos values ' + str(i))


import sqlite3

INGRESOS_SH = '''
CREATE TABLE "Ingresos" (
	"id"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"concepto"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"pagador"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)'''

GASTOS_SH = '''
CREATE TABLE "Gastos" (
	"id"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"establecimiento"	TEXT NOT NULL,
	"fecha"	INTEGER NOT NULL,
	"comentario"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''

ALUMNOS_SH = '''
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

CLASES_SH = '''
CREATE TABLE "Clases" (
	"id"	INTEGER NOT NULL,
	"alumno"	INTEGER,
	"tech"	INTEGER,
	"duracion"	INTEGER NOT NULL,
	"precio"	REAL NOT NULL,
	"fecha"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("alumno") REFERENCES "Alumno"("id")
)
'''
'''
conn = sqlite3.connect("./miData2.db")
# stm = conn.cursor().execute(INGRESOS_SH)
# stm = conn.cursor().execute(GASTOS_SH)
# stm = conn.cursor().execute(ALUMNOS_SH)
# stm = conn.cursor().execute(CLASES_SH)

with open('../populate.sql') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        a = conn.cursor().execute(line + ';')
        print(str(a.fetchall()))
conn.close()'''
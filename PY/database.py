import sqlite3

def connect():
    return sqlite3.connect("emails.db")

def createTableTrendmicro():
    db = connect()
    db.execute("""CREATE TABLE IF NOT EXISTS "alertassoc" (
            "registro_id"	INTEGER,
            "Fecha_y_Hora" TEXT,
            "user_ID"	TEXT,
            "Endpoint"	TEXT,
            "BU"	TEXT,
            "Politica"	TEXT,
            "Regla" TEXT,
            "Canal_DLP"	TEXT,
            "count"	INTEGER,
            "severidad"	TEXT,
            "Accion_DLP"	TEXT,
            "escalamiento"	TEXT,
            "CC"	TEXT,
            "argos_capa"	TEXT,
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")
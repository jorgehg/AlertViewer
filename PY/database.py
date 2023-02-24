import sqlite3

def connect():
    return sqlite3.connect("emails.db")

def createTableTrendmicro():
    db = connect()
    db.execute("""CREATE TABLE IF NOT EXISTS "alertassoc" (
            "registro_id"	INTEGER,
            "Fecha_y_Hora" TEXT,
            "BU"	TEXT,
            "User_ID"	TEXT,
            "Endpoint"	TEXT,
            "Politica"	TEXT,
            "Regla" TEXT,
            "Template"	TEXT,
            "Severidad"	TEXT,
            "Accion_DLP"	TEXT,
            "Canal_DLP"	TEXT,
            "Fileserver"	TEXT,
            "File_Path"	TEXT,
            "Filename"	TEXT,
            "Extension" TEXT,
            "Request" TEXT,
            "Asunto" TEXT,
            "Remitente" TEXT,
            "Destinatario_Dominio" TEXT,
            "Destinatario" TEXT,
            "Fuente" TEXT,
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")


def createTableOffice():
    db = connect()
    db.execute("""CREATE TABLE IF NOT EXISTS "alertasoffice" (
            "registro_id"	INTEGER,
            "Fecha_Hora" TEXT,
            "Dia_Habil"	TEXT,
            "Usuario"	TEXT,
            "Email"	TEXT,
            "Destinatario"	TEXT,
            "BU" TEXT,
            "Pais"	TEXT,
            "Politica"	INTEGER,
            "Regla"	TEXT,
            "Accion"	TEXT,
            "Producto"	TEXT,
            "Severidad"	TEXT,
            "Asunto"	TEXT,
            "Filename" TEXT,
            "Extension" TEXT,
            "TipoDataConfidencial" TEXT,
            "Fuente" TEXT,
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")

def createTableRegistros():
    db = connect()
    db.execute("""CREATE TABLE IF NOT EXISTS "historial" (
            "registro_id"	INTEGER,
            "Fecha_Hora" TEXT,
            "Nombre"	TEXT,
            "Cantidad_registros"
            "Tipo"      TEXT,
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")
from PyQt5 import QtCore, QtGui, QtQuickWidgets, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, re, win32com.client, sqlite3, csv

db = sqlite3.connect("datatest.db")
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
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")


registerCount = 0
fileCount = 0
errorCount = 0
resultText = ''

folder_path_emails = os.path.normpath(r"C:\Users\ext_johirayg\Documents\AlertViewer\office")
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items




for message in messages:
    if message.Subject.startswith('RV: Splunk Reporte DLP Office 365 - FIF CMR MX') and message.Unread == True:
        message.Unread = False
        print(message)
        for attachment in message.Attachments: 
            if str(attachment.FileName).endswith(".csv"):
                attachment.SaveASFile(os.path.join(folder_path_emails, attachment.FileName)) 



file_list = [file for file in os.listdir(folder_path_emails) if file.endswith(".csv")]
for i, _ in enumerate(file_list):
            with open(os.path.join(folder_path_emails,file_list[i]), 'r') as file:
                try:
                    reader = list(csv.reader(file))
                except Exception as e: 
                    errorCount+=1
                    resultText = resultText + "\nArchivo: "+file_list[i]+" Error: "+str(e)
                    print(e)

                for row in reader[1:]:
                    rowString = str(row)
                    rowString = rowString.replace("'", '')
                    rowString = rowString.replace("[", '')
                    input_list = rowString.split(",")
                    db.execute("INSERT INTO alertasoffice (Fecha_Hora,Dia_Habil,Usuario,Email,Destinatario,BU,Pais,Politica,Regla,Accion,Producto,Severidad,Asunto,Filename,Extension,TipoDataConfidencial) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(input_list[0],input_list[1][1:],input_list[2][1:],input_list[3][1:],input_list[4][1:],input_list[5][1:],input_list[6][1:],input_list[7][1:],input_list[8][1:],input_list[9][1:],input_list[10][1:], input_list[11][1:],input_list[12][1:],input_list[13][1:],input_list[14][1:],input_list[15][1:]))
                    #print(row)
                    registerCount+=1
            print(file_list[i])
            fileCount+=1
        
db.commit()
print("Se han cargado con éxito "+str(fileCount)+" archivos con "+str(registerCount)+" registros con "+str(errorCount)+" error(es)."+resultText)
    

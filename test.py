from PyQt5 import QtCore, QtGui, QtQuickWidgets, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, re, win32com.client, sqlite3, csv

db = sqlite3.connect("datatest.db")
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
            PRIMARY KEY("registro_id" AUTOINCREMENT)
        )""")

registerCount = 0
fileCount = 0
errorCount = 0
resultText = ''
file_list = []

folder_path_emails = os.path.normpath(r"C:\Users\Jorge\Documents\AlertViewer\trendmicro")
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items

for message in messages:
            if message.Subject.startswith('RV: Splunk Report: Reporte DLP Trend Micro - FIF CMR MX') and message.Unread == True:
                for attachment in message.Attachments: 
                    if str(attachment.FileName).endswith(".csv"):
                        try:
                            attachment.SaveASFile(os.path.join(folder_path_emails, attachment.FileName)) 
                            file_list.append(attachment.FileName)
                            print(attachment.FileName)
                            message.Unread = False
                        except Exception as e:
                            print(e)

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
                    db.execute("INSERT INTO alertassoc (Fecha_y_Hora,BU,User_ID,Endpoint,Politica,Regla,Template,Severidad,Accion_DLP,Canal_DLP,Fileserver,File_Path,Filename,Extension,Request,Asunto,Remitente,Destinatario_Dominio,Destinatario) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5],input_list[6],input_list[7],input_list[8],input_list[9],input_list[10], input_list[11],input_list[12],input_list[13],input_list[14],input_list[15],input_list[16],input_list[17],input_list[18]))
                    #print(row)
                    registerCount+=1
            #print(file_list[i])
            fileCount+=1

db.commit()
print(("Se han cargado con éxito "+str(fileCount)+" archivos con "+str(registerCount)+" registros con "+str(errorCount)+" error(es)."+resultText))




    

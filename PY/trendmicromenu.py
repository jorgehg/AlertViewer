from PyQt5 import QtCore, QtGui, QtQuickWidgets, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os, re, win32com.client, database, csv


class TrendmicroMenu(object):
    
    def loadFiles(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Importe de datos")
        registerCount = 0
        fileCount = 0
        errorCount = 0
        resultText = ''
        file_list = []

        db = database.connect()
        database.createTableTrendmicro()

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
                            db.execute("INSERT INTO alertassoc (Fecha_y_Hora,BU,User_ID,Endpoint,Politica,Regla,Template,Severidad,Accion_DLP,Canal_DLP,Fileserver,File_Path,Filename,Extension,Request,Asunto,Remitente,Destinatario_Dominio,Destinatario, Fuente) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],file_list[i]))
                            print(row)
                            registerCount+=1
                    #print(file_list[i])
                    fileCount+=1

        db.commit()
        dialog.setText("Se han cargado con éxito "+str(fileCount)+" archivos con "+str(registerCount)+" registros con "+str(errorCount)+" error(es)."+resultText)
        dialog.exec_()

    def loadAlerts(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Importe de datos")
        
        folder_path_emails = os.path.normpath(r"C:\Users\Jorge\Documents\AlertViewer\trendmicro")
        file_list = [file for file in os.listdir(folder_path_emails) if file.endswith(".msg")]
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        db = database.connect()
        database.createTableTrendmicro()

        for i, _ in enumerate(file_list):
            print(i)
            msg = outlook.OpenSharedItem(os.path.join(folder_path_emails,file_list[i]))
            text = msg.HTMLBody
            print(msg.SentOn)
            body = re.search(r"Fecha_y_Hora</p([\s\S]*?)Data<", text)
            body = body.group()
            body = body.replace("Fecha_y_Hora</pre>", '')
            body = ''.join(body.split())
            body = body.replace("""</td><tdstyle="text-align:left;padding:4px8px;margin-top:0px;margin-bottom:0px;border-bottom:1pxdotted#c3cbd4;"><prestyle="font-family:helvetica,arial,sans-serif;white-space:pre-wrap;margin:0px;">""",'')
            body = body.replace("/pre>",'')
            input_list = body.split("<")
            db.execute("INSERT INTO alertassoc (Fecha_y_Hora,user_ID,Endpoint,BU,Politica,Regla,Canal_DLP,count,severidad,Accion_DLP,escalamiento,CC,argos_capa) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(str(msg.sentOn),input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5],input_list[6],input_list[7],input_list[8],input_list[9],input_list[10], input_list[11]))
            print(input_list)

        db.commit()
        dialog.setText("Se han cargado con éxito "+str(len(file_list))+" registros.")
        dialog.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, -40, 539, 262))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setStyleSheet("background-color: rgb(216, 217, 207);\n"
"background-color: rgb(237, 237, 237);")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(250, 150, 250, 200)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonSubirArchivos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonSubirArchivos.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonSubirArchivos.setObjectName("pushButtonSubirArchivos")
        self.verticalLayout.addWidget(self.pushButtonSubirArchivos)
        self.pushButtonTablas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonTablas.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonTablas.setObjectName("pushButtonTablas")
        self.verticalLayout.addWidget(self.pushButtonTablas)
        self.pushButtonAlertas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAlertas.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonAlertas.setObjectName("pushButtonAlertas")
        self.verticalLayout.addWidget(self.pushButtonAlertas)
        self.pushButtonAtras = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAtras.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonAtras.setObjectName("pushButtonAtras")
        self.verticalLayout.addWidget(self.pushButtonAtras)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trendmicro - Inicio"))
        self.label.setText(_translate("MainWindow", "Office"))
        self.pushButtonSubirArchivos.setText(_translate("MainWindow", "Subir Archivos"))
        self.pushButtonTablas.setText(_translate("MainWindow", "Tablas"))
        self.pushButtonAlertas.setText(_translate("MainWindow", "Alertas"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.label_2.setText(_translate("MainWindow", "Trendmicro"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrendmicroMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

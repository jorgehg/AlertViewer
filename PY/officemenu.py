from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from officetabla import OfficeTabla
from datetime import datetime
import os, csv, database, win32com

class OfficeMenu(object):

    def loadFiles(self):
        dialog = QMessageBox()
        registerCount = 0
        fileCount = 0
        errorCount = 0
        resultText = ''
        file_list = []
        dialog.setWindowTitle("Importe de datos")
        dialog.setIcon(QMessageBox.Information)
        folder_path_emails = os.path.join(os.getcwd(), 'office')
        if not os.path.exists(folder_path_emails):
            os.mkdir(folder_path_emails)
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        messages = inbox.Items
        db = database.connect()
        database.createTableOffice()

        for message in messages:
            if message.Subject.startswith('RV: Splunk Reporte DLP Office 365 - FIF CMR MX') and message.Unread == True:
                for attachment in message.Attachments: 
                    if str(attachment.FileName).endswith(".csv"):
                        try:
                            print(attachment.FileName)
                            attachment.SaveASFile(os.path.join(folder_path_emails, attachment.FileName)) 
                            file_list.append(attachment.FileName)
                            message.Unread = False
                        except Exception as e:
                            print(e)

        
        for i, _ in enumerate(file_list):
            with open(os.path.join(folder_path_emails,file_list[i]), encoding="utf8") as file:
                try:
                    reader = list(csv.reader(file))
                    for row in reader[1:]:
                        date = datetime.strptime(row[0], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                        db.execute("INSERT INTO alertasoffice (Fecha_Hora,Dia_Habil,Usuario,Email,Destinatario,BU,Pais,Politica,Regla,Accion,Producto,Severidad,Asunto,Filename,Extension,TipoDataConfidencial, Fuente) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(date,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11],row[12],row[13],row[14],row[15],file_list[i]))
                        #print(row)
                        registerCount+=1
                    fileCount+=1
                except Exception as e: 
                    errorCount+=1
                    resultText = resultText + "\nArchivo: "+file_list[i]+" Error: "+str(e)
                    print(e)
            #print(file_list[i])
        
        db.commit()
        dialog.setText("Se han cargado con éxito "+str(fileCount)+" archivos con "+str(registerCount)+" registros con "+str(errorCount)+" error(es)."+resultText)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Office - Inicio"))
        self.label.setText(_translate("MainWindow", "Office"))
        self.pushButtonSubirArchivos.setText(_translate("MainWindow", "Subir Archivos"))
        self.pushButtonTablas.setText(_translate("MainWindow", "Tablas"))
        self.pushButtonAlertas.setText(_translate("MainWindow", "Alertas"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.label_2.setText(_translate("MainWindow", "Office"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OfficeMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


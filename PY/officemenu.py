from PyQt5 import QtCore, QtGui, QtWidgets
from officetabla import OfficeTabla
import os, csv, database

class OfficeMenu(object):

    def loadFiles(self):
        folder_path_emails = os.path.normpath(r"C:\Users\ext_johirayg\Documents\AlertViewer\office")
        email_list = [file for file in os.listdir(folder_path_emails) if file.endswith(".csv")]
        db = database.connect()
        database.createTableOffice()


        for i, _ in enumerate(email_list):
            with open(os.path.join(folder_path_emails,email_list[i]), 'r') as file:
                reader = list(csv.reader(file))
                for row in reader[1:]:
                    print(row)
                    rowString = str(row)
                    rowString = rowString.replace("'", '')
                    rowString = rowString.replace("[", '')
                    input_list = rowString.split(",")
                    db.execute("INSERT INTO alertasoffice (Fecha_Hora,Dia_Habil,Usuario,Email,Destinatario,BU,Pais,Politica,Regla,Accion,Producto,Severidad,Asunto,Filename,Extension,TipoDataConfidencial) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(input_list[0],input_list[1][1:],input_list[2][1:],input_list[3][1:],input_list[4][1:],input_list[5][1:],input_list[6][1:],input_list[7][1:],input_list[8][1:],input_list[9][1:],input_list[10][1:], input_list[11][1:],input_list[12][1:],input_list[13][1:],input_list[14][1:],input_list[15][1:]))
                    db.commit()

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


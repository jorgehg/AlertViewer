from PyQt5 import QtCore, QtGui, QtWidgets
import database

class TrendmicroTabla(object):
    
    def updateTable(self, fieldListNames):
        if fieldListNames == False:
            fieldListNames = ["registro_id", "Fecha_y_Hora", "user_ID", "Endpoint", "BU", "Politica", "Regla", "Canal_DLP", "count", "severidad", "Accion_DLP", "escalamiento", "CC", "argos_capa"]
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 1321, 541))
        self.tableWidget.setObjectName("tableWidget")

        print(fieldListNames)
        self.tableWidget.setColumnCount(len(fieldListNames))

        counter = 0
        _translate = QtCore.QCoreApplication.translate
        
        sqlquery = ""

        for i in fieldListNames:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(counter, item)
            item = self.tableWidget.horizontalHeaderItem(counter)
            item.setText(_translate("MainWindow", i))
            counter+=1
            sqlquery = sqlquery + " " + i + ","

        sqlquery = sqlquery[:-1]

        sqlquery  = "SELECT"+sqlquery+" FROM alertassoc"
        self.pushButtonLimpiar.setText(_translate("MainWindow", sqlquery))
        
        db = database.connect()
        cur = db.cursor()

        self.tableWidget.setRowCount(50)
        tableRow = 0
        print(sqlquery)

        for row in cur.execute(sqlquery):
            counter = 0
            for i in row:
                self.tableWidget.setItem(tableRow, counter, QtWidgets.QTableWidgetItem(str(i)))
                counter +=1
            tableRow+=1

        self.centralwidget.update()
                


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.widget.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.widget.setObjectName("widget")      
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1059, 10, 271, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonActualizar = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonActualizar.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonActualizar.setObjectName("pushButtonActualizar")
        self.horizontalLayout_2.addWidget(self.pushButtonActualizar)
        self.pushButtonAtras = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonAtras.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonAtras.setObjectName("pushButtonAtras")
        self.horizontalLayout_2.addWidget(self.pushButtonAtras)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 90, 801, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Fieldselector = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Fieldselector.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButton_Fieldselector.setObjectName("pushButton_Fieldselector")
        self.horizontalLayout_3.addWidget(self.pushButton_Fieldselector)
        self.dateEditDesde = QtWidgets.QDateEdit(self.horizontalLayoutWidget_3)
        self.dateEditDesde.setObjectName("dateEditDesde")
        self.horizontalLayout_3.addWidget(self.dateEditDesde)
        self.dateEditHasta = QtWidgets.QDateEdit(self.horizontalLayoutWidget_3)
        self.dateEditHasta.setObjectName("dateEditHasta")
        self.horizontalLayout_3.addWidget(self.dateEditHasta)
        self.comboBoxBuscarCampo = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBoxBuscarCampo.setObjectName("comboBoxBuscarCampo")
        self.horizontalLayout_3.addWidget(self.comboBoxBuscarCampo)
        self.lineEditBuscarCampo = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEditBuscarCampo.setObjectName("lineEditBuscarCampo")
        self.horizontalLayout_3.addWidget(self.lineEditBuscarCampo)
        self.pushButtonAplicar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonAplicar.setStyleSheet("background-color: rgb(255, 135, 135);\n"
"")
        self.pushButtonAplicar.setObjectName("pushButtonAplicar")
        self.horizontalLayout_3.addWidget(self.pushButtonAplicar)
        self.pushButtonLimpiar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonLimpiar.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonLimpiar.setObjectName("pushButtonLimpiar")
        self.horizontalLayout_3.addWidget(self.pushButtonLimpiar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.comboBoxBuscarCampo.addItem('ID Registro')
        self.comboBoxBuscarCampo.addItem('Fecha y Hora')
        self.comboBoxBuscarCampo.addItem('ID Usuario')
        self.comboBoxBuscarCampo.addItem('Endpoint')
        self.comboBoxBuscarCampo.addItem('BU')
        self.comboBoxBuscarCampo.addItem('Politica')
        self.comboBoxBuscarCampo.addItem('Regla')
        self.comboBoxBuscarCampo.addItem('Canal DLP')
        self.comboBoxBuscarCampo.addItem('Count')
        self.comboBoxBuscarCampo.addItem('Severidad')
        self.comboBoxBuscarCampo.addItem('Accion DLP')
        self.comboBoxBuscarCampo.addItem('Escalamiento')
        self.comboBoxBuscarCampo.addItem('CC')
        self.comboBoxBuscarCampo.addItem('Argos Capa')
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trendmicro - Tabla"))
        
        self.pushButtonActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_Fieldselector.setText(_translate("MainWindow", "Seleccionar campos"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrendmicroTabla()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
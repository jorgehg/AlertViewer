from PyQt5 import QtCore, QtGui, QtWidgets
import database

class TrendmicroTabla(object):
    
    def loadData(self):
        db = database.connect()
        cur = db.cursor()
        sqlquery = "SELECT * FROM alertassoc"

        self.tableWidget.setRowCount(50)
        tableRow = 0

        for row in cur.execute(sqlquery):
            print(cur)
            self.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tableRow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(tableRow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(tableRow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.tableWidget.setItem(tableRow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.tableWidget.setItem(tableRow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.tableWidget.setItem(tableRow, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.tableWidget.setItem(tableRow, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.tableWidget.setItem(tableRow, 13, QtWidgets.QTableWidgetItem(row[13]))
            tableRow+=1


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.widget.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 1321, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Registro"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha y Hora"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID Usuario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Endpoint"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BU"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Politica"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Regla"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Canal DLP"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Count"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Severidad"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Accion DLP"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Escalamiento"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "CC"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Argos Capa"))
        self.pushButtonActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_Fieldselector.setText(_translate("MainWindow", "Seleccionar campos"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.pushButtonLimpiar.setText(_translate("MainWindow", "Limpiar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrendmicroTabla()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
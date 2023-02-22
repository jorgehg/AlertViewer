from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from datetime import date,datetime
import database, csv

class TrendmicroTabla(object):
    comboBoxContent = ""
    
    def updateTable(self, fieldListNames,typeCall):
        if fieldListNames == False:
            fieldListNames = ["registro_id","Fecha_y_Hora","BU","User_ID","Endpoint","Politica","Regla","Template","Severidad","Accion_DLP","Canal_DLP","Fileserver","File_Path","Filename","Extension","Request","Asunto","Remitente","Destinatario_Dominio","Destinatario", "Fuente"]
        
        comboBoxContent = self.comboBoxBuscarCampo.currentText()
        self.tableWidget.setColumnCount(len(fieldListNames))

        counter = 0
        _translate = QtCore.QCoreApplication.translate
        
        db = database.connect()
        cur = db.cursor()
        sqlquery = ""
        
        header = self.tableWidget.horizontalHeader()
        self.comboBoxBuscarCampo.clear()

        for i in fieldListNames:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(counter, item)
            item = self.tableWidget.horizontalHeaderItem(counter)
            item.setText(_translate("MainWindow", i))
            self.comboBoxBuscarCampo.addItem(i)
            header.setSectionResizeMode(counter, QtWidgets.QHeaderView.ResizeToContents)
            counter+=1
            sqlquery = sqlquery + " " + i + ","

        self.comboBoxBuscarCampo.setCurrentText(comboBoxContent)
        sqlquery = sqlquery[:-1]

        if typeCall == 1 or typeCall == 2:
            dateDesde = str(cur.execute("SELECT MIN(Fecha_y_Hora) FROM alertassoc").fetchone()[0])
            print(dateDesde)
            dateDesde = datetime.strptime(dateDesde, '%Y-%m-%d %H:%M:%S')
            self.dateEditDesde.setDate(dateDesde)
            print(list)
            dateHasta = date.today()
            self.dateEditHasta.setDate(dateHasta)
            self.lineEditBuscarCampo.clear()

        dateDesde = self.dateEditDesde.date() 
        dateDesde = str(dateDesde.toPyDate())
        dateHasta = self.dateEditHasta.date().addDays(1)
        dateHasta = str(dateHasta.toPyDate())

        if self.lineEditBuscarCampo.text() == '':
            sqlquery  = "SELECT"+sqlquery+" FROM alertassoc WHERE Fecha_y_Hora > '"+dateDesde+"' AND Fecha_y_Hora < '"+dateHasta+"';" 
        else:
            sqlquery  = "SELECT"+sqlquery+" FROM alertassoc WHERE "+comboBoxContent+"= '"+self.lineEditBuscarCampo.text()+"' and Fecha_y_Hora > '"+dateDesde+"' AND Fecha_y_Hora < '"+dateHasta+"';" 

        tableRow = 0
        self.tableWidget.setRowCount(100000)
        print(sqlquery)
        
        for row in cur.execute(sqlquery):
            counter = 0
            for i in row:
                self.tableWidget.setItem(tableRow, counter, QtWidgets.QTableWidgetItem(str(i)))
                counter +=1
            tableRow+=1
            #print(row)
        self.tableWidget.setRowCount(tableRow)

        self.centralwidget.update()

    def exportTable(self,directory):
        print(directory)
        columns = range(self.tableWidget.columnCount())
        header = [self.tableWidget.horizontalHeaderItem(column).text() for column in columns]
        with open(directory,'w',encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for row in range(self.tableWidget.rowCount()):
                writer.writerow(self.tableWidget.item(row,column).text() for column in columns)

        
        
                
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
        self.pushButtonAtras = QtWidgets.QPushButton(self.widget)
        self.pushButtonAtras.setGeometry(QtCore.QRect(1200, 15, 120, 25))
        self.pushButtonAtras.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonAtras.setObjectName("pushButtonAtras")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 90, 800, 70))
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
        self.dateEditDesde.setDisplayFormat("dd-MM-yyyy")
        self.horizontalLayout_3.addWidget(self.dateEditDesde)
        self.dateEditHasta = QtWidgets.QDateEdit(self.horizontalLayoutWidget_3)
        self.dateEditHasta.setObjectName("dateEditHasta")
        self.dateEditHasta.setDisplayFormat("dd-MM-yyyy")
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
        self.pushButtonExportar = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonExportar.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonExportar.setObjectName("pushButtonLimpiar")
        self.horizontalLayout_3.addWidget(self.pushButtonExportar)
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trendmicro - Tabla")) 
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.pushButton_Fieldselector.setText(_translate("MainWindow", "Seleccionar campos"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.pushButtonLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.pushButtonExportar.setText(_translate("MainWindow", "Exportar"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrendmicroTabla()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
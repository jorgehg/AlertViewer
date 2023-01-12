from PyQt5 import QtCore, QtGui, QtWidgets

class OfficeFieldSelector(object):
    
    """
    """

    fieldListNames = ["registro_id","Fecha_Hora","Dia_Habil","Usuario","Email","Destinatario","BU","Pais","Politica","Regla","Accion","Producto","Severidad","Asunto","Filename","Extension","TipoDataConfidencial"]
    fieldListStatus = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    switcher = False

    def setFields(self):
        self.fieldListStatus[0] = 1 if self.checkBox_IDRegistro.isChecked() else 0
        self.fieldListStatus[1] = 1 if self.checkBox_Fecha_Hora.isChecked() else 0
        self.fieldListStatus[2] = 1 if self.checkBox_Dia_Habil.isChecked() else 0
        self.fieldListStatus[3] = 1 if self.checkBox_Usuario.isChecked() else 0
        self.fieldListStatus[4] = 1 if self.checkBox_Email.isChecked() else 0
        self.fieldListStatus[5] = 1 if self.checkBox_Destinatario.isChecked() else 0
        self.fieldListStatus[6] = 1 if self.checkBox_BU.isChecked() else 0
        self.fieldListStatus[7] = 1 if self.checkBox_Pais.isChecked() else 0
        self.fieldListStatus[8] = 1 if self.checkBox_Politica.isChecked() else 0
        self.fieldListStatus[9] = 1 if self.checkBox_Regla.isChecked() else 0
        self.fieldListStatus[10] = 1 if self.checkBox_Accion.isChecked() else 0
        self.fieldListStatus[11] = 1 if self.checkBox_Producto.isChecked() else 0
        self.fieldListStatus[12] = 1 if self.checkBox_Severidad.isChecked() else 0
        self.fieldListStatus[13] = 1 if self.checkBox_Asunto.isChecked() else 0
        self.fieldListStatus[14] = 1 if self.checkBox_Filename.isChecked() else 0
        self.fieldListStatus[15] = 1 if self.checkBox_Extension.isChecked() else 0
        self.fieldListStatus[16] = 1 if self.checkBox_TipoDataConfidencial.isChecked() else 0

        counter = 0
        fieldListNamesUsed = []
        for i in self.fieldListStatus:
            if i == 1:
                fieldListNamesUsed.append(self.fieldListNames[counter])
            counter+=1

        return fieldListNamesUsed
    
    def setCheckboxes(self):
        self.checkBox_IDRegistro.setChecked(True) if self.fieldListStatus[0] == 1 else self.checkBox_IDRegistro.setChecked(False)
        self.checkBox_Fecha_Hora.setChecked(True) if self.fieldListStatus[1] == 1 else self.checkBox_Fecha_Hora.setChecked(False)
        self.checkBox_Dia_Habil.setChecked(True) if self.fieldListStatus[2] == 1 else self.checkBox_Dia_Habil.setChecked(False)
        self.checkBox_Usuario.setChecked(True) if self.fieldListStatus[3] == 1 else self.checkBox_Usuario.setChecked(False)
        self.checkBox_Email.setChecked(True) if self.fieldListStatus[4] == 1 else self.checkBox_Email.setChecked(False)
        self.checkBox_Destinatario.setChecked(True) if self.fieldListStatus[5] == 1 else self.checkBox_Destinatario.setChecked(False)
        self.checkBox_BU.setChecked(True) if self.fieldListStatus[6] == 1 else self.checkBox_BU.setChecked(False)
        self.checkBox_Pais.setChecked(True) if self.fieldListStatus[7] == 1 else self.checkBox_Pais.setChecked(False)
        self.checkBox_Politica.setChecked(True) if self.fieldListStatus[8] == 1 else self.checkBox_Politica.setChecked(False)
        self.checkBox_Regla.setChecked(True) if self.fieldListStatus[9] == 1 else self.checkBox_Regla.setChecked(False)
        self.checkBox_Accion.setChecked(True) if self.fieldListStatus[10] == 1 else self.checkBox_Accion.setChecked(False)
        self.checkBox_Producto.setChecked(True) if self.fieldListStatus[11] == 1 else self.checkBox_Producto.setChecked(False)
        self.checkBox_Severidad.setChecked(True) if self.fieldListStatus[12] == 1 else self.checkBox_Severidad.setChecked(False)
        self.checkBox_Asunto.setChecked(True) if self.fieldListStatus[13] == 1 else self.checkBox_Asunto.setChecked(False)
        self.checkBox_Filename.setChecked(True) if self.fieldListStatus[14] == 1 else self.checkBox_Filename.setChecked(False)
        self.checkBox_Extension.setChecked(True) if self.fieldListStatus[15] == 1 else self.checkBox_Extension.setChecked(False)
        self.checkBox_TipoDataConfidencial.setChecked(True) if self.fieldListStatus[16] == 1 else self.checkBox_TipoDataConfidencial.setChecked(False)
        
    def switcher(self):
        self.switcher = not bool(self.switcher)
        self.checkBox_IDRegistro.setChecked(self.switcher)
        self.checkBox_Fecha_Hora.setChecked(self.switcher) 
        self.checkBox_Dia_Habil.setChecked(self.switcher)  
        self.checkBox_Usuario.setChecked(self.switcher)  
        self.checkBox_Email.setChecked(self.switcher)  
        self.checkBox_Destinatario.setChecked(self.switcher) 
        self.checkBox_BU.setChecked(self.switcher)  
        self.checkBox_Pais.setChecked(self.switcher)  
        self.checkBox_Politica.setChecked(self.switcher)
        self.checkBox_Regla.setChecked(self.switcher)  
        self.checkBox_Accion.setChecked(self.switcher) 
        self.checkBox_Producto.setChecked(self.switcher)  
        self.checkBox_Severidad.setChecked(self.switcher)  
        self.checkBox_Asunto.setChecked(self.switcher)  
        self.checkBox_Filename.setChecked(self.switcher)  
        self.checkBox_Extension.setChecked(self.switcher)  
        self.checkBox_TipoDataConfidencial.setChecked(self.switcher)  
        
        
        self.centralwidget.update()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 0, 50, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_Pais = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Pais.setObjectName("checkBox_Pais")
        self.gridLayout.addWidget(self.checkBox_Pais, 2, 1, 1, 1)
        self.checkBox_Email = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Email.setObjectName("checkBox_Email")
        self.gridLayout.addWidget(self.checkBox_Email, 1, 1, 1, 1)
        self.checkBox_BU = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_BU.setObjectName("checkBox_BU")
        self.gridLayout.addWidget(self.checkBox_BU, 2, 0, 1, 1)
        self.checkBox_Fecha_Hora = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Fecha_Hora.setObjectName("checkBox_Fecha_Hora")
        self.gridLayout.addWidget(self.checkBox_Fecha_Hora, 0, 1, 1, 1)
        self.checkBox_Regla = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Regla.setObjectName("checkBox_Regla")
        self.gridLayout.addWidget(self.checkBox_Regla, 3, 0, 1, 1)
        self.checkBox_Politica = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Politica.setObjectName("checkBox_Politica")
        self.gridLayout.addWidget(self.checkBox_Politica, 2, 2, 1, 1)
        self.checkBox_Producto = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Producto.setObjectName("checkBox_Producto")
        self.gridLayout.addWidget(self.checkBox_Producto, 3, 2, 1, 1)
        self.checkBox_Dia_Habil = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Dia_Habil.setObjectName("checkBox_Dia_Habil")
        self.gridLayout.addWidget(self.checkBox_Dia_Habil, 0, 2, 1, 1)
        self.checkBox_Accion = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Accion.setObjectName("checkBox_Accion")
        self.gridLayout.addWidget(self.checkBox_Accion, 3, 1, 1, 1)
        self.checkBox_Destinatario = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Destinatario.setObjectName("checkBox_Destinatario")
        self.gridLayout.addWidget(self.checkBox_Destinatario, 1, 2, 1, 1)
        self.checkBox_IDRegistro = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_IDRegistro.setObjectName("checkBox_IDRegistro")
        self.gridLayout.addWidget(self.checkBox_IDRegistro, 0, 0, 1, 1)
        self.pushButtonAplicar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonAplicar.setObjectName("pushButtonAplicar")
        self.gridLayout.addWidget(self.pushButtonAplicar, 6, 2, 1, 1)
        self.pushButtonSwitch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSwitch.setObjectName("pushButtonSwitch")
        self.gridLayout.addWidget(self.pushButtonSwitch, 6, 0, 1, 1)
        self.checkBox_Asunto = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Asunto.setObjectName("checkBox_Asunto")
        self.gridLayout.addWidget(self.checkBox_Asunto, 4, 1, 1, 1)
        self.checkBox_Severidad = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Severidad.setObjectName("checkBox_Severidad")
        self.gridLayout.addWidget(self.checkBox_Severidad, 4, 0, 1, 1)
        self.checkBox_Usuario = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Usuario.setObjectName("checkBox_Usuario")
        self.gridLayout.addWidget(self.checkBox_Usuario, 1, 0, 1, 1)
        self.checkBox_Filename = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Filename.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Filename, 4, 2, 1, 1)
        self.checkBox_Extension = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Extension.setObjectName("checkBox_Extension")
        self.gridLayout.addWidget(self.checkBox_Extension, 5, 0, 1, 1)
        self.checkBox_TipoDataConfidencial = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_TipoDataConfidencial.setObjectName("checkBox_TipoDataConfidencial")
        self.gridLayout.addWidget(self.checkBox_TipoDataConfidencial, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.setCheckboxes()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seleccionar campos"))
        self.checkBox_Pais.setText(_translate("MainWindow", "Pais"))
        self.checkBox_Email.setText(_translate("MainWindow", "Email"))
        self.checkBox_BU.setText(_translate("MainWindow", "BU"))
        self.checkBox_Fecha_Hora.setText(_translate("MainWindow", "Fecha_Hora"))
        self.checkBox_Regla.setText(_translate("MainWindow", "Regla"))
        self.checkBox_Politica.setText(_translate("MainWindow", "Politica"))
        self.checkBox_Producto.setText(_translate("MainWindow", "Producto"))
        self.checkBox_Dia_Habil.setText(_translate("MainWindow", "Dia_Habil"))
        self.checkBox_Accion.setText(_translate("MainWindow", "Accion"))
        self.checkBox_Destinatario.setText(_translate("MainWindow", "Destinatario"))
        self.checkBox_IDRegistro.setText(_translate("MainWindow", "ID Registro"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.pushButtonSwitch.setText(_translate("MainWindow", "Todos/Ninguno"))
        self.checkBox_Asunto.setText(_translate("MainWindow", "Asunto"))
        self.checkBox_Severidad.setText(_translate("MainWindow", "Severidad"))
        self.checkBox_Usuario.setText(_translate("MainWindow", "Usuario"))
        self.checkBox_Filename.setText(_translate("MainWindow", "Filename"))
        self.checkBox_Extension.setText(_translate("MainWindow", "Extension"))
        self.checkBox_TipoDataConfidencial.setText(_translate("MainWindow", "TipoDataConfid"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OfficeFieldSelector()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
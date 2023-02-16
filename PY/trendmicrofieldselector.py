from PyQt5 import QtCore, QtGui, QtWidgets

class TrendmicroFieldSelector(object):
    
    """
    0 = registro_id
    1 = Fecha_y_Hora
    2 = user_ID
    3 = Endpoint
    4 = BU
    5 = Politica
    6 = Regla 
    7 = Canal_DLP
    8 = count
    9 = severidad
    10 = Accion_DLP
    11 = escalamiento
    12 = CC 
    13 = argos_capa
    """

    fieldListNames = ["registro_id","Fecha_y_Hora","BU","User_ID","Endpoint","Politica","Regla","Template","Severidad","Accion_DLP","Canal_DLP","Fileserver","File_Path","Filename","Extension","Request","Asunto","Remitente","Destinatario_Dominio","Destinatario", "Fuente"]
    fieldListStatus = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    switcher = False

    def setFields(self):
        self.fieldListStatus[0] = 1 if self.checkBox_IDRegistro.isChecked() else 0
        self.fieldListStatus[1] = 1 if self.checkBox_FechayHora.isChecked() else 0
        self.fieldListStatus[2] = 1 if self.checkBox_BU.isChecked() else 0
        self.fieldListStatus[3] = 1 if self.checkBox_User_ID.isChecked() else 0
        self.fieldListStatus[4] = 1 if self.checkBox_Endpoint.isChecked() else 0
        self.fieldListStatus[5] = 1 if self.checkBox_Politica.isChecked() else 0
        self.fieldListStatus[6] = 1 if self.checkBox_Regla.isChecked() else 0
        self.fieldListStatus[7] = 1 if self.checkBox_Template.isChecked() else 0
        self.fieldListStatus[8] = 1 if self.checkBox_Severidad.isChecked() else 0
        self.fieldListStatus[9] = 1 if self.checkBox_Accion_DLP.isChecked() else 0
        self.fieldListStatus[10] = 1 if self.checkBox_Canal_DLP.isChecked() else 0
        self.fieldListStatus[11] = 1 if self.checkBox_Fileserver.isChecked() else 0
        self.fieldListStatus[12] = 1 if self.checkBox_File_Path.isChecked() else 0
        self.fieldListStatus[13] = 1 if self.checkBox_Filename.isChecked() else 0
        self.fieldListStatus[14] = 1 if self.checkBox_Extension.isChecked() else 0
        self.fieldListStatus[15] = 1 if self.checkBox_Request.isChecked() else 0
        self.fieldListStatus[16] = 1 if self.checkBox_Asunto.isChecked() else 0
        self.fieldListStatus[17] = 1 if self.checkBox_Remitente.isChecked() else 0
        self.fieldListStatus[18] = 1 if self.checkBox_Destinatario_Dominio.isChecked() else 0
        self.fieldListStatus[19] = 1 if self.checkBox_Destinatario.isChecked() else 0
        self.fieldListStatus[20] = 1 if self.checkBox_Fuente.isChecked() else 0


        counter = 0
        fieldListNamesUsed = []
        for i in self.fieldListStatus:
            if i == 1:
                fieldListNamesUsed.append(self.fieldListNames[counter])
            counter+=1

        return fieldListNamesUsed
    
    def setCheckboxes(self):
        self.checkBox_IDRegistro.setChecked(True) if self.fieldListStatus[0] == 1 else self.checkBox_IDRegistro.setChecked(False)
        self.checkBox_FechayHora.setChecked(True) if self.fieldListStatus[1] == 1 else self.checkBox_FechayHora.setChecked(False)
        self.checkBox_BU.setChecked(True) if self.fieldListStatus[2] == 1 else self.checkBox_BU.setChecked(False)
        self.checkBox_User_ID.setChecked(True) if self.fieldListStatus[3] == 1 else self.checkBox_User_ID.setChecked(False)
        self.checkBox_Endpoint.setChecked(True) if self.fieldListStatus[4] == 1 else self.checkBox_Endpoint.setChecked(False)
        self.checkBox_Politica.setChecked(True) if self.fieldListStatus[5] == 1 else self.checkBox_Politica.setChecked(False)
        self.checkBox_Regla.setChecked(True) if self.fieldListStatus[6] == 1 else self.checkBox_Regla.setChecked(False)
        self.checkBox_Template.setChecked(True) if self.fieldListStatus[7] == 1 else self.checkBox_Template.setChecked(False)
        self.checkBox_Severidad.setChecked(True) if self.fieldListStatus[8] == 1 else self.checkBox_Severidad.setChecked(False)
        self.checkBox_Accion_DLP.setChecked(True) if self.fieldListStatus[9] == 1 else self.checkBox_Accion_DLP.setChecked(False)
        self.checkBox_Canal_DLP.setChecked(True) if self.fieldListStatus[10] == 1 else self.checkBox_Canal_DLP.setChecked(False)
        self.checkBox_Fileserver.setChecked(True) if self.fieldListStatus[11] == 1 else self.checkBox_Fileserver.setChecked(False)
        self.checkBox_File_Path.setChecked(True) if self.fieldListStatus[12] == 1 else self.checkBox_File_Path.setChecked(False)
        self.checkBox_Filename.setChecked(True) if self.fieldListStatus[13] == 1 else self.checkBox_Filename.setChecked(False)
        self.checkBox_Extension.setChecked(True) if self.fieldListStatus[14] == 1 else self.checkBox_Extension. setChecked(False)
        self.checkBox_Request.setChecked(True) if self.fieldListStatus[15] == 1 else self.checkBox_Request.setChecked(False)
        self.checkBox_Asunto.setChecked(True) if self.fieldListStatus[16] == 1 else self.checkBox_Asunto.setChecked(False)
        self.checkBox_Remitente.setChecked(True) if self.fieldListStatus[17] == 1 else self.checkBox_Remitente.setChecked(False)
        self.checkBox_Destinatario_Dominio.setChecked(True) if self.fieldListStatus[18] == 1 else self.checkBox_Destinatario_Dominio.setChecked(False)
        self.checkBox_Destinatario.setChecked(True) if self.fieldListStatus[19] == 1 else self.checkBox_Destinatario.setChecked(False)
        self.checkBox_Fuente.setChecked(True) if self.fieldListStatus[20] == 1 else self.checkBox_Fuente.setChecked(False)
        
    def switcher(self):
        self.switcher = not bool(self.switcher)
        self.checkBox_FechayHora.setChecked(self.switcher) 
        self.checkBox_BU.setChecked(self.switcher)  
        self.checkBox_User_ID.setChecked(self.switcher)  
        self.checkBox_Endpoint.setChecked(self.switcher)  
        self.checkBox_Politica.setChecked(self.switcher) 
        self.checkBox_Regla.setChecked(self.switcher)  
        self.checkBox_Template.setChecked(self.switcher)  
        self.checkBox_Severidad.setChecked(self.switcher)
        self.checkBox_Accion_DLP.setChecked(self.switcher)  
        self.checkBox_Canal_DLP.setChecked(self.switcher) 
        self.checkBox_Fileserver.setChecked(self.switcher)  
        self.checkBox_File_Path.setChecked(self.switcher)  
        self.checkBox_Filename.setChecked(self.switcher)  
        self.checkBox_IDRegistro.setChecked(self.switcher)
        self.checkBox_Extension.setChecked(self.switcher)
        self.checkBox_Request.setChecked(self.switcher)
        self.checkBox_Asunto.setChecked(self.switcher)
        self.checkBox_Remitente.setChecked(self.switcher)
        self.checkBox_Destinatario_Dominio.setChecked(self.switcher)
        self.checkBox_Destinatario.setChecked(self.switcher)
        self.checkBox_Fuente.setChecked(self.switcher)
        
        self.centralwidget.update()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 0, 50, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_IDRegistro = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_IDRegistro.setObjectName("checkBox_IDRegistro")
        self.gridLayout.addWidget(self.checkBox_IDRegistro, 0, 0, 1, 1)
        self.checkBox_FechayHora = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_FechayHora.setObjectName("checkBox_FechayHora")
        self.gridLayout.addWidget(self.checkBox_FechayHora, 0, 1, 1, 1)
        self.checkBox_BU = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_BU.setObjectName("checkBox_BU")
        self.gridLayout.addWidget(self.checkBox_BU, 0, 2, 1, 1)
        self.checkBox_User_ID = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_User_ID.setObjectName("checkBox_User_ID")
        self.gridLayout.addWidget(self.checkBox_User_ID, 0, 3, 1, 1)
        self.checkBox_Endpoint = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Endpoint.setObjectName("checkBox_Endpoint")
        self.gridLayout.addWidget(self.checkBox_Endpoint, 1, 0, 1, 1)
        self.checkBox_Politica = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Politica.setObjectName("checkBox_Politica")
        self.gridLayout.addWidget(self.checkBox_Politica, 1, 1, 1, 1)
        self.checkBox_Regla = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Regla.setObjectName("checkBox_Regla")
        self.gridLayout.addWidget(self.checkBox_Regla, 1, 2, 1, 1)
        self.checkBox_Template = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Template.setObjectName("checkBox_Template")
        self.gridLayout.addWidget(self.checkBox_Template, 1, 3, 1, 1)
        self.checkBox_Severidad = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Severidad.setObjectName("checkBox_Severidad")
        self.gridLayout.addWidget(self.checkBox_Severidad, 2, 0, 1, 1)              
        self.checkBox_Accion_DLP = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Accion_DLP.setObjectName("checkBox_Accion_DLP")
        self.gridLayout.addWidget(self.checkBox_Accion_DLP, 2, 1, 1, 1)
        self.checkBox_Canal_DLP = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Canal_DLP.setObjectName("checkBox_Canal_DLP")
        self.gridLayout.addWidget(self.checkBox_Canal_DLP, 2, 2, 1, 1)        
        self.checkBox_Fileserver = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Fileserver.setObjectName("checkBox_Fileserver")
        self.gridLayout.addWidget(self.checkBox_Fileserver, 2, 3, 1, 1)
        self.checkBox_File_Path = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_File_Path.setObjectName("checkBox_File_Path")
        self.gridLayout.addWidget(self.checkBox_File_Path, 3, 0, 1, 1)
        self.checkBox_Filename = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Filename.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Filename, 3, 1, 1, 1)
        self.checkBox_Extension = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Extension.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Extension, 3, 2, 1, 1)
        self.checkBox_Request = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Request.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Request, 3, 3, 1, 1)
        self.checkBox_Asunto = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Asunto.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Asunto, 4, 0, 1, 1)
        self.checkBox_Remitente = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Remitente.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Remitente, 4, 1, 1, 1)
        self.checkBox_Destinatario_Dominio = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Destinatario_Dominio.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Destinatario_Dominio, 4, 2, 1, 1)
        self.checkBox_Destinatario = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Destinatario.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Destinatario, 4, 3, 1, 1)
        self.checkBox_Fuente = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Fuente.setObjectName("checkBox_Filename")
        self.gridLayout.addWidget(self.checkBox_Fuente, 5, 0, 1, 1)
        self.pushButtonSwitch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonSwitch.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButtonSwitch, 5, 2, 1, 1)
        self.pushButtonAplicar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonAplicar.setObjectName("pushButtonAplicar")
        self.gridLayout.addWidget(self.pushButtonAplicar, 5, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.setCheckboxes()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seleccionar campos"))
        self.checkBox_Endpoint.setText(_translate("MainWindow", "Endpoint"))
        self.checkBox_Template.setText(_translate("MainWindow", "Template"))
        self.checkBox_FechayHora.setText(_translate("MainWindow", "Fecha y Hora"))
        self.checkBox_Accion_DLP.setText(_translate("MainWindow", "Accion DLP"))
        self.checkBox_Regla.setText(_translate("MainWindow", "Regla"))
        self.checkBox_IDRegistro.setText(_translate("MainWindow", "ID Registro"))
        self.checkBox_BU.setText(_translate("MainWindow", "BU"))
        self.checkBox_Canal_DLP.setText(_translate("MainWindow", "Canal DLP"))
        self.checkBox_Severidad.setText(_translate("MainWindow", "Severidad"))
        self.checkBox_Politica.setText(_translate("MainWindow", "Politica"))
        self.checkBox_Fileserver.setText(_translate("MainWindow", "Fileserver"))
        self.checkBox_User_ID.setText(_translate("MainWindow", "User_ID"))
        self.checkBox_File_Path.setText(_translate("MainWindow", "File Path"))
        self.checkBox_Filename.setText(_translate("MainWindow", "Filename"))
        self.checkBox_Extension.setText(_translate("MainWindow", "Extension"))
        self.checkBox_Request.setText(_translate("MainWindow", "Request"))
        self.checkBox_Asunto.setText(_translate("MainWindow", "Asunto"))
        self.checkBox_Remitente.setText(_translate("MainWindow", "Remitente"))
        self.checkBox_Destinatario_Dominio.setText(_translate("MainWindow", "Destinatario_Dominio"))
        self.checkBox_Destinatario.setText(_translate("MainWindow", "Destinatario"))
        self.checkBox_Fuente.setText(_translate("MainWindow", "Fuente"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))
        self.pushButtonSwitch.setText(_translate("MainWindow", "Todos/Ninguno"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrendmicroFieldSelector()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
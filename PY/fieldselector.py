from PyQt5 import QtCore, QtGui, QtWidgets

class FieldSelector(object):
    
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

    fieldListNames = ["registro_id", "Fecha_y_Hora", "user_ID", "Endpoint", "BU", "Politica", "Regla", "Canal_DLP", "count", "severidad", "Accion_DLP", "escalamiento", "CC", "argos_capa"]
    fieldListStatus = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    def setFields(self):
        self.fieldListStatus[0] = 1 if self.checkBox_FechayHora.isChecked() else 0
        self.fieldListStatus[1] = 1 if self.checkBox_ID_Usuario.isChecked() else 0
        self.fieldListStatus[2] = 1 if self.checkBox_Endpoint.isChecked() else 0
        self.fieldListStatus[3] = 1 if self.checkBox_BU.isChecked() else 0
        self.fieldListStatus[4] = 1 if self.checkBox_Politica.isChecked() else 0
        self.fieldListStatus[5] = 1 if self.checkBox_Regla.isChecked() else 0
        self.fieldListStatus[6] = 1 if self.checkBox_CanalDLP.isChecked() else 0
        self.fieldListStatus[7] = 1 if self.checkBox_Count.isChecked() else 0
        self.fieldListStatus[8] = 1 if self.checkBox_Severidad.isChecked() else 0
        self.fieldListStatus[9] = 1 if self.checkBox_AccionDLP.isChecked() else 0
        self.fieldListStatus[10] = 1 if self.checkBox_Escalamiento.isChecked() else 0
        self.fieldListStatus[11] = 1 if self.checkBox_CC.isChecked() else 0
        self.fieldListStatus[12] = 1 if self.checkBox_ArgosCapa.isChecked() else 0
        self.fieldListStatus[13] = 1 if self.checkBox_IDRegistro.isChecked() else 0

        print(self.fieldListStatus)
        print("vetealaverga")

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
        self.checkBox_CanalDLP = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_CanalDLP.setObjectName("checkBox_CanalDLP")
        self.gridLayout.addWidget(self.checkBox_CanalDLP, 2, 1, 1, 1)
        self.checkBox_BU = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_BU.setObjectName("checkBox_BU")
        self.gridLayout.addWidget(self.checkBox_BU, 1, 1, 1, 1)
        self.checkBox_FechayHora = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_FechayHora.setObjectName("checkBox_FechayHora")
        self.gridLayout.addWidget(self.checkBox_FechayHora, 0, 1, 1, 1)
        self.checkBox_AccionDLP = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_AccionDLP.setObjectName("checkBox_AccionDLP")
        self.gridLayout.addWidget(self.checkBox_AccionDLP, 3, 1, 1, 1)
        self.checkBox_ID_Usuario = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ID_Usuario.setObjectName("checkBox_ID_Usuario")
        self.gridLayout.addWidget(self.checkBox_ID_Usuario, 0, 2, 1, 1)
        self.checkBox_Severidad = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Severidad.setObjectName("checkBox_Severidad")
        self.gridLayout.addWidget(self.checkBox_Severidad, 3, 0, 1, 1)
        self.checkBox_IDRegistro = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_IDRegistro.setObjectName("checkBox_IDRegistro")
        self.gridLayout.addWidget(self.checkBox_IDRegistro, 0, 0, 1, 1)
        self.checkBox_Regla = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Regla.setObjectName("checkBox_Regla")
        self.gridLayout.addWidget(self.checkBox_Regla, 2, 0, 1, 1)
        self.checkBox_Count = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Count.setObjectName("checkBox_Count")
        self.gridLayout.addWidget(self.checkBox_Count, 2, 2, 1, 1)
        self.checkBox_Politica = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Politica.setObjectName("checkBox_Politica")
        self.gridLayout.addWidget(self.checkBox_Politica, 1, 2, 1, 1)
        self.checkBox_Escalamiento = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Escalamiento.setObjectName("checkBox_Escalamiento")
        self.gridLayout.addWidget(self.checkBox_Escalamiento, 3, 2, 1, 1)
        self.checkBox_CC = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_CC.setObjectName("checkBox_CC")
        self.gridLayout.addWidget(self.checkBox_CC, 4, 0, 1, 1)
        self.checkBox_ArgosCapa = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ArgosCapa.setObjectName("checkBox_ArgosCapa")
        self.gridLayout.addWidget(self.checkBox_ArgosCapa, 4, 1, 1, 1)
        self.checkBox_Endpoint = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Endpoint.setObjectName("checkBox_Endpoint")
        self.gridLayout.addWidget(self.checkBox_Endpoint, 1, 0, 1, 1)
        self.pushButtonAplicar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonAplicar.setObjectName("pushButtonAplicar")
        self.gridLayout.addWidget(self.pushButtonAplicar, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.checkBox_FechayHora.setChecked(True) if self.fieldListStatus[0] == 1 else self.checkBox_FechayHora.setChecked(False)
        self.checkBox_ID_Usuario.setChecked(True) if self.fieldListStatus[1] == 1 else self.checkBox_ID_Usuario.setChecked(False)
        self.checkBox_Endpoint.setChecked(True) if self.fieldListStatus[2] == 1 else self.checkBox_Endpoint.setChecked(False)
        self.checkBox_BU.setChecked(True) if self.fieldListStatus[3] == 1 else self.checkBox_BU.setChecked(False)
        self.checkBox_Politica.setChecked(True) if self.fieldListStatus[4] == 1 else self.checkBox_Politica.setChecked(False)
        self.checkBox_Regla.setChecked(True) if self.fieldListStatus[5] == 1 else self.checkBox_Regla.setChecked(False)
        self.checkBox_CanalDLP.setChecked(True) if self.fieldListStatus[6] == 1 else self.checkBox_CanalDLP.setChecked(False)
        self.checkBox_Count.setChecked(True) if self.fieldListStatus[7] == 1 else self.checkBox_Count.setChecked(False)
        self.checkBox_Severidad.setChecked(True) if self.fieldListStatus[8] == 1 else self.checkBox_Severidad.setChecked(False)
        self.checkBox_AccionDLP.setChecked(True) if self.fieldListStatus[9] == 1 else self.checkBox_AccionDLP.setChecked(False)
        self.checkBox_Escalamiento.setChecked(True) if self.fieldListStatus[10] == 1 else self.checkBox_Escalamiento.setChecked(False)
        self.checkBox_CC.setChecked(True) if self.fieldListStatus[11] == 1 else self.checkBox_CC.setChecked(False)
        self.checkBox_ArgosCapa.setChecked(True) if self.fieldListStatus[12] == 1 else self.checkBox_ArgosCapa.setChecked(False)
        self.checkBox_IDRegistro.setChecked(True) if self.fieldListStatus[13] == 1 else self.checkBox_IDRegistro.setChecked(False)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seleccionar campos"))
        self.checkBox_CanalDLP.setText(_translate("MainWindow", "Canal DLP"))
        self.checkBox_BU.setText(_translate("MainWindow", "BU"))
        self.checkBox_FechayHora.setText(_translate("MainWindow", "Fecha y Hora"))
        self.checkBox_AccionDLP.setText(_translate("MainWindow", "Accion DLP"))
        self.checkBox_ID_Usuario.setText(_translate("MainWindow", "ID Usuario"))
        self.checkBox_Severidad.setText(_translate("MainWindow", "Severidad"))
        self.checkBox_IDRegistro.setText(_translate("MainWindow", "ID Registro"))
        self.checkBox_Regla.setText(_translate("MainWindow", "Regla"))
        self.checkBox_Count.setText(_translate("MainWindow", "Count"))
        self.checkBox_Politica.setText(_translate("MainWindow", "Politica"))
        self.checkBox_Escalamiento.setText(_translate("MainWindow", "Escalamiento"))
        self.checkBox_CC.setText(_translate("MainWindow", "CC"))
        self.checkBox_ArgosCapa.setText(_translate("MainWindow", "Argos Capa"))
        self.checkBox_Endpoint.setText(_translate("MainWindow", "Endpoint"))
        self.pushButtonAplicar.setText(_translate("MainWindow", "Aplicar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FieldSelector()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
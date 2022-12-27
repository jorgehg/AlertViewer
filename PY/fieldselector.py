
from PyQt5 import QtCore, QtGui, QtWidgets
import array as arr



class FieldSelector(object):
    fieldList = list[1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    def setFields(self):
        ad = 1
         
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
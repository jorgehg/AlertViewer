# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trendmicromenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(700, 20, 71, 51))
        self.pushButtonBack.setObjectName("pushButtonBack")
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
        self.pushButtonBack.setText(_translate("MainWindow", "Atrás"))
        self.pushButtonSubirArchivos.setText(_translate("MainWindow", "Subir Archivos"))
        self.pushButtonTablas.setText(_translate("MainWindow", "Tablas"))
        self.pushButtonAlertas.setText(_translate("MainWindow", "Alertas"))
        self.pushButtonAtras.setText(_translate("MainWindow", "Atrás"))
        self.label_2.setText(_translate("MainWindow", "Trendmicro"))
import trendmicroinciorsc_rc
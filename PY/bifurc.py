from PyQt5 import QtCore, QtGui, QtWidgets
from trendmicromenu import TrendmicroMenu
from officemenu import OfficeMenu

class Bifurc(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    background-color: rgb(237, 237, 237)\n"
";}")
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(150, 0, 150, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTrendmicro = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonTrendmicro.setStyleSheet("\n"
"background-color: rgb(255, 135, 135);")
        self.pushButtonTrendmicro.setObjectName("pushButtonTrendmicro")
        self.horizontalLayout.addWidget(self.pushButtonTrendmicro)
        self.pushButtonOffice = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonOffice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonOffice.setAutoFillBackground(False)
        self.pushButtonOffice.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.pushButtonOffice.setObjectName("pushButtonOffice")
        self.horizontalLayout.addWidget(self.pushButtonOffice)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlertViewer"))
        self.pushButtonTrendmicro.setText(_translate("MainWindow", "Trendmicro"))
        self.pushButtonOffice.setText(_translate("MainWindow", "Office"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Bifurc()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






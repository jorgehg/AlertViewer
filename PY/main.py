from PyQt5 import QtCore, QtGui, QtWidgets
from bifurc import Bifurc
from trendmicromenu import TrendmicroMenu
from officemenu import OfficeMenu
from trendmicrotabla import TrendmicroTabla
from officetabla import OfficeTabla
from fieldselector import FieldSelector


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.bifurc = QtWidgets.QMainWindow()
        self.ui = Bifurc()
        self.ui.setupUi(self.bifurc)
        self.bifurc.show()
        self.btnAbrirTrendmicro = self.ui.pushButtonTrendmicro
        self.btnAbrirTrendmicro.clicked.connect(self.open_trendmicromenu)
        self.btnAbrirOffice = self.ui.pushButtonOffice
        self.btnAbrirOffice.clicked.connect(self.open_officemenu)

    def open_trendmicromenu(self):
        self.trendmicromenu = QtWidgets.QMainWindow()
        self.ui = TrendmicroMenu()
        self.ui.setupUi(self.trendmicromenu)
        self.trendmicromenu.show()
        self.bifurc.hide()

        self.ui.pushButtonSubirArchivos.clicked.connect(self.ui.loadFiles)
        self.ui.pushButtonTablas.clicked.connect(self.open_trendmicrotabla)
        #self.ui.pushButtonAlertas.clicked.connect(open_trendmicroalertas)
        self.ui.pushButtonAtras.clicked.connect(self.back_trendmicromenu)

    def open_officemenu(self):
        self.officemenu = QtWidgets.QMainWindow()
        self.ui = OfficeMenu()
        self.ui.setupUi(self.officemenu)
        self.officemenu.show()
        self.bifurc.hide()
        #self.ui.pushButtonSubirArchivos.clicked.connect(self.ui.loadFiles)
        self.ui.pushButtonTablas.clicked.connect(self.open_officetabla)
        #self.ui.pushButtonAlertas.clicked.connect(self.open_officealertas)
        self.ui.pushButtonAtras.clicked.connect(self.back_officemenu)

    def open_trendmicrotabla(self):
        self.trendmicrotabla = QtWidgets.QMainWindow()
        self.ui = TrendmicroTabla()
        self.ui.setupUi(self.trendmicrotabla)
        self.trendmicrotabla.show()
        self.trendmicromenu.hide()
        self.ui.pushButton_Fieldselector.clicked.connect(self.open_fieldselector)
        #self.ui.pushButtonAplicar.clicked.connect(self.ui.applyChanges)
        #self.ui.pushButtonLimpiar.clicked.connect(self.ui.cleanChanges)
        self.ui.pushButtonActualizar.clicked.connect(self.ui.loadData)
        self.ui.pushButtonAtras.clicked.connect(self.back_trendmicrotabla)

    def open_officetabla(self):
        self.officetabla = QtWidgets.QMainWindow()
        self.ui = OfficeTabla()
        self.ui.setupUi(self.officetabla)
        self.officetabla.show()
        self.officemenu.hide()
        #self.ui.pushButtonActualizar.clicked.connect(self.ui.loadData)
        self.ui.pushButtonAtras.clicked.connect(self.back_officetabla)

    def open_fieldselector(self):
        self.fieldselector = QtWidgets.QMainWindow()
        self.ui = FieldSelector()
        self.ui.setupUi(self.fieldselector)
        self.fieldselector.show()
        self.ui.pushButtonAplicar.clicked.connect(self.apply_fieldselector)
        

    
    def back_trendmicromenu(self):
        self.bifurc.show()
        self.trendmicromenu.hide()
    
    def back_officemenu(self):
        self.bifurc.show()
        self.officemenu.hide()

    def back_trendmicrotabla(self):
        self.trendmicromenu.show()
        self.trendmicrotabla.hide()

    def back_officetabla(self):
        self.officemenu.show()
        self.officetabla.show()


    def apply_fieldselector(self):
        self.ui.setFields
        self.fieldselector.hide()





    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    input()

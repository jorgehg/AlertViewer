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
        self.ui_trendmicromenu = TrendmicroMenu()
        self.ui_trendmicromenu.setupUi(self.trendmicromenu)
        self.trendmicromenu.show()
        self.bifurc.hide()

        self.ui_trendmicromenu.pushButtonSubirArchivos.clicked.connect(self.ui_trendmicromenu.loadFiles)
        self.ui_trendmicromenu.pushButtonTablas.clicked.connect(self.open_trendmicrotabla)
        #self.ui.pushButtonAlertas.clicked.connect(open_trendmicroalertas)
        self.ui_trendmicromenu.pushButtonAtras.clicked.connect(self.back_trendmicromenu)

    def open_officemenu(self):
        self.officemenu = QtWidgets.QMainWindow()
        self.ui_officemenu = OfficeMenu()
        self.ui_officemenu.setupUi(self.officemenu)
        self.officemenu.show()
        self.bifurc.hide()
        #self.ui.pushButtonSubirArchivos.clicked.connect(self.ui.loadFiles)
        self.ui_officemenu.pushButtonTablas.clicked.connect(self.open_officetabla)
        #self.ui.pushButtonAlertas.clicked.connect(self.open_officealertas)
        self.ui_officemenu.pushButtonAtras.clicked.connect(self.back_officemenu)

    def open_trendmicrotabla(self):
        self.trendmicrotabla = QtWidgets.QMainWindow()
        self.ui_trendmicrotabla = TrendmicroTabla()
        self.ui_trendmicrotabla.setupUi(self.trendmicrotabla)
        self.ui_trendmicrotabla.updateTable(False)
        self.trendmicrotabla.show()
        self.trendmicromenu.hide()
        self.ui_trendmicrotabla.pushButton_Fieldselector.clicked.connect(self.open_fieldselector)
        #self.ui.pushButtonAplicar.clicked.connect(self.ui.applyChanges)
        #self.ui.pushButtonLimpiar.clicked.connect(self.ui.cleanChanges)
        #self.ui_trendmicrotabla.pushButtonActualizar.clicked.connect(self.ui_trendmicrotabla.loadData)
        self.ui_trendmicrotabla.pushButtonAtras.clicked.connect(self.back_trendmicrotabla)

    def open_officetabla(self):
        self.officetabla = QtWidgets.QMainWindow()
        self.ui_officetabla = OfficeTabla()
        self.ui_officetabla.setupUi(self.officetabla)
        self.officetabla.show()
        self.officemenu.hide()
        #self.ui_officetabla.pushButtonActualizar.clicked.connect(self.ui_officetabla.loadData)
        self.ui_officetabla.pushButtonAtras.clicked.connect(self.back_officetabla)

    def open_fieldselector(self):
        self.fieldselector = QtWidgets.QMainWindow()
        self.ui_fieldselector = FieldSelector()
        self.ui_fieldselector.setupUi(self.fieldselector)
        self.fieldselector.show()
        self.ui_fieldselector.pushButtonAplicar.clicked.connect(self.apply_fieldselector)
        self.ui_fieldselector.pushButtonSwitch.clicked.connect(self.ui_fieldselector.switcher)
        
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
        self.officetabla.hide()
        

    def apply_fieldselector(self):
        print(self.ui_fieldselector.setFields())
        self.ui_trendmicrotabla.updateTable(self.ui_fieldselector.setFields())
        self.fieldselector.hide()

    #def switch_fieldselector(self):
        
        





    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    input()

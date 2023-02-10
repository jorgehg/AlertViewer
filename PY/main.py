from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bifurc import Bifurc
from trendmicromenu import TrendmicroMenu
from officemenu import OfficeMenu
from trendmicrotabla import TrendmicroTabla
from officetabla import OfficeTabla
from trendmicrofieldselector import TrendmicroFieldSelector
from officefieldselector import OfficeFieldSelector


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
        self.ui_officemenu.pushButtonSubirArchivos.clicked.connect(self.ui_officemenu.loadFiles)
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
        self.ui_trendmicrotabla.pushButton_Fieldselector.clicked.connect(self.open_trendmicrofieldselector)
        self.ui_trendmicrotabla.pushButtonAplicar.clicked.connect(self.applyChanges_trendmicrotabla)
        #self.ui_trendmicrotabla.pushButtonLimpiar.clicked.connect(self.ui_trendmicrotabla.updateTable(False))
        #self.ui_trendmicrotabla.pushButtonActualizar.clicked.connect(self.ui_trendmicrotabla.loadData)
        self.ui_trendmicrotabla.pushButtonAtras.clicked.connect(self.back_trendmicrotabla)

    def open_officetabla(self):
        self.officetabla = QtWidgets.QMainWindow()
        self.ui_officetabla = OfficeTabla()
        self.ui_officetabla.setupUi(self.officetabla)
        self.ui_officetabla.updateTable(False)
        self.officetabla.show()
        self.officemenu.hide()
        self.ui_officetabla.pushButton_Fieldselector.clicked.connect(self.open_officefieldselector)
        self.ui_officetabla.pushButtonAplicar.clicked.connect(self.applyChanges_officetabla)
        #self.ui_officetabla.pushButtonActualizar.clicked.connect(self.ui_officetabla.loadData)
        self.ui_officetabla.pushButtonAtras.clicked.connect(self.back_officetabla)

    def open_trendmicrofieldselector(self):
        self.trendmicrofieldselector = QtWidgets.QMainWindow()
        self.ui_trendmicrofieldselector = TrendmicroFieldSelector()
        self.ui_trendmicrofieldselector.setupUi(self.trendmicrofieldselector)
        self.trendmicrofieldselector.show()
        self.ui_trendmicrofieldselector.pushButtonAplicar.clicked.connect(self.apply_trendmicrofieldselector)
        self.ui_trendmicrofieldselector.pushButtonSwitch.clicked.connect(self.ui_trendmicrofieldselector.switcher)

    def open_officefieldselector(self):
        self.officefieldselector = QtWidgets.QMainWindow()
        self.ui_officefieldselector = OfficeFieldSelector()
        self.ui_officefieldselector.setupUi(self.officefieldselector)
        self.officefieldselector.show()
        self.ui_officefieldselector.pushButtonAplicar.clicked.connect(self.apply_officefieldselector)
        self.ui_officefieldselector.pushButtonSwitch.clicked.connect(self.ui_officefieldselector.switcher)

        
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
        

    def apply_trendmicrofieldselector(self):
        self.ui_trendmicrotabla.updateTable(self.ui_trendmicrofieldselector.setFields())
        self.trendmicrofieldselector.hide()

    def apply_officefieldselector(self):
        self.ui_officetabla.updateTable(self.ui_officefieldselector.setFields())
        self.officefieldselector.hide()

    def applyChanges_trendmicrotabla(self):
        try:
            self.ui_trendmicrotabla.updateTable(self.ui_trendmicrofieldselector.setFields())
        except: 
            self.ui_trendmicrotabla.updateTable(False)

    def applyChanges_officetabla(self):
        try:
            self.ui_officetabla.updateTable(self.ui_officefieldselector.setFields())
        except: 
            self.ui_officetabla.updateTable(False)

    
    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.exec()



        

    #def switch_fieldselector(self):
        
        





    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

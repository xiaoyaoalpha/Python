# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from Testresult.Ui_butdis import Ui_Dialog
from PyQt4 import  QtGui
from Testresult.Ui_butdis import _translate

class buttondisa(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_Button1_clicked(self):
        # TODO: not implemented yet
        self.label.setText(_translate("Dialog", "请按下按钮1", None))
    
    @pyqtSignature("")
    def on_Button_2_clicked(self):
        # TODO: not implemented yet
        self.label.setText(_translate("Dialog", "请按下按钮2", None))
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = buttondisa()
    dlg.show()
    sys.exit(app.exec_())
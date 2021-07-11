import os

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


# This loads your .ui file so that PyQt can populate your plugin 
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'MorfoCuencas_dialog_base.ui'))


class MyPluginDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MyPluginDialog, self).__init__(parent)
       
        self.setupUi(self)
        
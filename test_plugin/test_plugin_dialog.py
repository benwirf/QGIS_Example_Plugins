"""
/****************************************************************************************
Copyright:  Ben Wirf
Date:       November 2019
Email:      ben.wirf@gmail.com
****************************************************************************************/
"""

from qgis.gui import QgsMapLayerComboBox, QgsFieldComboBox
from PyQt5.QtWidgets import QDialog, QGridLayout, QTabWidget, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont


class TestPluginDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.main_layout = QGridLayout(self)
        self.tabwidget = QTabWidget()
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        # Set up Tab_1 layout
        self.layout_1 = QGridLayout(self)
        self.main_lbl = QLabel('Select features by attribute value', self)
        self.main_lbl.setFont(QFont('Arial', 12))
        self.v_cb_lbl = QLabel('Select a vector layer:', self)
        self.vector_cb = QgsMapLayerComboBox()
        self.f_cb_lbl = QLabel('Select a field:', self)
        self.fld_cb = QgsFieldComboBox()
        self.edit_lbl = QLabel('Field value contains:', self)
        self.edit = QLineEdit(self)
        self.btn_ok_1 = QPushButton('Select Features', self)
        self.layout_1.addWidget(self.main_lbl, 0, 0, 1, 2)
        self.layout_1.addWidget(self.v_cb_lbl, 1, 0)  # item, row, column
        self.layout_1.addWidget(self.vector_cb, 1, 1)
        self.layout_1.addWidget(self.f_cb_lbl, 2, 0)
        self.layout_1.addWidget(self.fld_cb, 2, 1)
        self.layout_1.addWidget(self.edit_lbl, 3, 0)
        self.layout_1.addWidget(self.edit, 3, 1)
        self.layout_1.addWidget(self.btn_ok_1, 4, 1)
        self.layout_1.setSpacing(25)
        self.tab1.setLayout(self.layout_1)
        # Set up Tab_2 layout
        self.layout_2 = QGridLayout(self)
        self.r_cb_lbl = QLabel('Select a raster layer:', self)
        self.raster_cb = QgsMapLayerComboBox(self)
        self.md_edit = QTextEdit(self)
        self.btn_ok_2 = QPushButton('Get Metadata', self)
        self.layout_2.addWidget(self.r_cb_lbl, 0, 0)
        self.layout_2.addWidget(self.raster_cb, 0, 1)
        self.layout_2.addWidget(self.md_edit, 1, 0, 1, 2)
        self.layout_2.addWidget(self.btn_ok_2, 2, 1)
        self.tab2.setLayout(self.layout_2)
        ###
        self.tabwidget.addTab(self.tab1, "Vector")
        self.tabwidget.addTab(self.tab2, "Raster")
        self.main_layout.addWidget(self.tabwidget, 0, 0)
        
    def closeEvent(self, event):
        self.edit.clear()
        self.md_edit.clear()
            

"""
/****************************************************************************************
Copyright:  (C) Ben Wirf
Date:       November 2019
Email:      ben.wirf@gmail.com
****************************************************************************************/
"""

from qgis.core import QgsMapLayerProxyModel
from PyQt5.QtWidgets import QAction, QToolBar

from .test_plugin_dialog import TestPluginDialog


class TestPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.window = self.iface.mainWindow()
        self.dlg = TestPluginDialog()
        self.toolbar = [c for c in self.window.children() if isinstance(c, QToolBar) and c.objectName() == 'mPluginToolBar'][0]
        self.action = QAction('Go!', self.window)
        
    def initGui(self):
        """This method is where we add the plugin action to the plugin toolbar.
       We also do any setup of the gui widgets such as apply filters to Map Layer Combo Boxes
       and set layers to Field Combo Boxes. This is also where we connect any signals and slots
       such as Push Buttons to our class methods which contain our plugin logic."""
        self.action.setObjectName('btnGo')
        self.toolbar.addAction(self.action)
        # Vector Tab
        self.dlg.vector_cb.setFilters(QgsMapLayerProxyModel.VectorLayer | QgsMapLayerProxyModel.HasGeometry)
        self.dlg.fld_cb.setLayer(self.dlg.vector_cb.currentLayer())
        self.dlg.vector_cb.layerChanged.connect(lambda: self.dlg.fld_cb.setLayer(self.dlg.vector_cb.currentLayer()))
        self.dlg.btn_ok_1.setEnabled(False)
        self.dlg.edit.textChanged.connect(self.edit_text_changed)
        self.dlg.btn_ok_1.clicked.connect(self.vector_logic)
        # Raster Tab
        self.dlg.raster_cb.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.dlg.btn_ok_2.clicked.connect(self.raster_logic)
        # Show Plugin Dialog
        self.action.triggered.connect(lambda: self.dlg.show())
        
    def edit_text_changed(self):
        if self.dlg.edit.text() == '':
            self.dlg.btn_ok_1.setEnabled(False)
        else:
            self.dlg.btn_ok_1.setEnabled(True)
            
        
    def vector_logic(self):
        v_lyr = self.dlg.vector_cb.currentLayer()
        fld = self.dlg.fld_cb.currentField()
        val = self.dlg.edit.text()
        exp = """"{}" LIKE '%{}%'""".format(fld, val)
        v_lyr.selectByExpression(exp)
        
    def raster_logic(self):
        r_lyr = self.dlg.raster_cb.currentLayer()
        m_data = r_lyr.dataProvider().htmlMetadata()
        self.dlg.md_edit.setHtml(m_data)
            
    def unload(self):
        self.toolbar.removeAction(self.action)
        del self.action



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMessageBox
from qgis.gui import QgsMapToolEmitPoint

from .my_plugin_dialog import MyPluginDialog


class MyPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.pointTool = QgsMapToolEmitPoint(self.canvas)
        self.msg = QMessageBox()
        self.dlg = MyPluginDialog()

    def initGui(self):
        self.action = QAction('My Plugin', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        
        # Declare your signal-slot connections
        self.dlg.finished.connect(lambda: self.iface.actionPan().trigger())
        self.dlg.Boton.clicked.connect(self.Pbtn_clicked)
        self.dlg.Prueba.clicked.connect(self.Prueba_clic)
        self.dlg.pb_close.clicked.connect(lambda: self.dlg.close())
        self.pointTool.canvasClicked.connect(self.display_point)
        
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def Pbtn_clicked(self):
        #Fetch current layer in QgsMapLayerComboBox
        entrada = self.dlg.cbbCargarCapas.currentLayer()
#        directorioTrabajo=self.lneSalida.text()
#        self.Proceso(entrada,directorioTrabajo)
        self.iface.messageBar().pushMessage("la ruta de salida es: "+str(entrada.name()))

    def Prueba_clic(self):
        self.dlg.showMinimized()
        self.canvas.setMapTool(self.pointTool)

    def display_point(self,  pnt):
        puntox = str(pnt[0])
        puntoy = str(pnt[1])
        QMessageBox.information(self.iface.mainWindow(), "Capa Activa", 'El punto es ' +puntox+','+puntoy)

    def run(self):
        self.dlg.show()
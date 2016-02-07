# coding: latin-1
__author__ = 'waldo'

import sys

from ventanas import Ui_vtnPrincipal
from baseDatos import Conexion, CreacionTabla
from gestionClientes import *
from gestionProductos import *
from gestionVentas import *
from gui import MyMdi
from lgIngresar import Ingresar
from lgListados import Listar
from lgAyuda import Ayuda
from gui.signals import PoolOfWindows

class MainWindow(QtGui.QMainWindow, Ui_vtnPrincipal):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # ----- Mappea las tablas con la base y crea una sesion
        CreacionTabla()
        bdConexion = Conexion()
        self.sesion = bdConexion.crearSesion()
        # Cerrar ventana con la opcion del menu
        self.actionSalir_2.triggered.connect(self.close)

        self.config()

        #contenedor de ventanas internas
        self.setCentralWidget(QtGui.QMdiArea(self))
        self.centralWidget().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.centralWidget().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # ------ Instanciar ventanas MDI
        action_subwin = [
            (self.actionAltaCliente, Cliente.create),
            (self.actionBajaCliente, Cliente.delete),
            (self.actionModificarCliente, Cliente.update),
            (self.actionAltaMedicamento, Medicamento.create),
            (self.actionBajaMedicamento, Medicamento.delete),
            (self.actionModificarMedicamento, Medicamento.update),
            (self.actionAltaMonodroga, Monodroga.create),
            (self.actionBajaMonodroga, Monodroga.delete),
            (self.actionModificarMonodroga, Monodroga.update),
            (self.actionAltaPresentacion, Presentacion.create),
            (self.actionBajaPresentacion, Presentacion.delete),
            (self.actionModificarPresentacion, Presentacion.update),
            (self.actionAltaProducto, Producto.create),
            (self.actionBajaProducto, Producto.delete),
            (self.actionModificarProducto, Producto.update),
            (self.actionAltaLote, Lote.create),
            (self.actionModificarLote, Lote.update),
            (self.actionBajaRemito, Remito.delete),
            (self.actionModificarRemito, Remito.update),
            (self.actionDevolucionDeCliente, DevolucionDeCliente),
            (self.actionFraccionarProducto, FraccionarProducto),
            (self.actionIngresar, Ingresar),
            (self.actionListar, Listar),
            (self.actionRegistrarCobroRemito, RegistrarCobroRemito),
            (self.actionReintegroCliente, ReintegroCliente),
            (self.actionVentaContado, VentaContado),
            (self.actionVentaConRemito, VentaConRemito),
            (self.actionAjusteNegativoStock, AjusteNegativoStock),
            (self.actionAyuda, Ayuda)
        ]

        # ------ Lista de ventanas disponibles para el farmaceutico
        self.farmaceutico = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionModificarCliente),
            (self.menuVenta),
            (self.actionRegistrarCobroRemito),
            (self.actionReintegroCliente),
            (self.actionVentaContado),
            (self.actionVentaConRemito),
            (self.actionBajaRemito),
            (self.actionModificarRemito),
            (self.actionDevolucionDeCliente),
            (self.menuListar),
            (self.actionListar)
        ]
        # ----- Lista de ventanas disponibles para el administrador
        self.administrador = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionBajaCliente),
            (self.actionModificarCliente),
            (self.menuListar),
            (self.actionListar)
        ]
        # ----- Lista de ventanas disponibles para el tecnico farmaceutico
        self.tecnico_farmaceutico = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionBajaCliente),
            (self.actionModificarCliente),
            (self.menuProducto),
            (self.actionAltaMedicamento),
            (self.actionBajaMedicamento),
            (self.actionModificarMedicamento),
            (self.actionAltaMonodroga),
            (self.actionBajaMonodroga),
            (self.actionModificarMonodroga),
            (self.actionAltaPresentacion),
            (self.actionBajaPresentacion),
            (self.actionModificarPresentacion),
            (self.actionAltaProducto),
            (self.actionBajaProducto),
            (self.actionModificarProducto),
            (self.actionAltaLote),
            (self.actionModificarLote),
            (self.actionAjusteNegativoStock),
            (self.actionFraccionarProducto),
            (self.menuListar),
            (self.actionListar),
            (self.menuVenta),
            (self.actionRegistrarCobroRemito),
            (self.actionReintegroCliente),
            (self.actionVentaContado),
            (self.actionVentaConRemito),
            (self.actionBajaRemito),
            (self.actionModificarRemito),
            (self.actionDevolucionDeCliente)
        ]

        instances = []
        for action, subwin in action_subwin:
            mdi = MyMdi(self)
            temp = subwin(mdi)
            instances.append(temp)
            mdi.setWidget(temp)
            self.centralWidget().addSubWindow(mdi)
            if not (action == self.actionIngresar):
                mdi.hide()
            action.triggered.connect(mdi.show)
        self.deshabilitarMenu()

        nombres_ventanas = [
            "AltaCliente", "BajaCliente", "ModificarCliente",
            "AltaMedicamento", "BajaMedicamento", "ModificarMedicamento",
            "AltaMonodroga", "BajaMonodroga", "ModificarMonodroga",
            "AltaPresentacion","BajaPresentacion", "ModificarPresentacion",
            "AltaProducto", "BajaProducto", "ModificarProducto",
            "AltaLote","ModificarLote", "BajaRemito",
            "ModificarRemito", "DevolucionDeCliente", "FraccionarProducto",
            "Ingresar", "Listar", "RegistrarCobroRemito",
            "ReintegroCliente", "VentaContado", "VentaConRemito",
            "AjusteNegativoStock", "Ayuda"]

        dict = {}
        for nro, obj in enumerate(instances):
            dict[nombres_ventanas[nro]] = obj

        PoolOfWindows.addPool(dict)
        PoolOfWindows.setHandlers()

    # ----- muestra un mensaje en la barra de estado de la ventan principal
    def setBarraEstado(self, estado):
        self.statusBar().showMessage(estado)

    # ----- deshabilita los menu y actions cada vez que se llama a la ventana ingresar

    def deshabilitarMenu(self):
        for hab in self.tecnico_farmaceutico:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(False)
            else:
                hab.setVisible(False)

    # ----- Devuelve la sesion de la BD
    def getSesionBD(self):
        return self.sesion

    def config(self):
        from configparser import ConfigParser
        config = ConfigParser()
        config.read("Configuracion.cfg")
        sections = config.sections() #ve las secciones del archivo (hay una sola llamada FARMACIA)
        a = config.get("Farmacia", "CUIT") #Asi se obtiene cada item del archivo

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
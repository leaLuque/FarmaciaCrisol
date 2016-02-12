# coding: latin-1
__author__ = 'waldo'

import sys

from PyQt4.QtGui import QGroupBox

from ventanas import Ui_vtnPrincipal
from baseDatos import Conexion, CreacionTabla
from gestionClientes import *
from gestionProductos import *
from gestionVentas import *
from gui import MyMdi
from lgIngresar import Ingresar
from lgListados import Listar
from lgAyuda import Ayuda, AcercaDe
from gui.signals import PoolOfWindows

class MainWindow(QtGui.QMainWindow, Ui_vtnPrincipal):

    user = ""
    host = ""
    password = ""

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.config()
        # ----- Mappea las tablas con la base y crea una sesion
        CreacionTabla(user = self.user,host = self.host, password = self.password)
        bdConexion = Conexion(user = self.user,host = self.host, password = self.password)
        self.sesion = bdConexion.crearSesion()
        # Cerrar ventana con la opcion del menu
        self.actionSalir_2.triggered.connect(self.cerrar)



        self.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F1), self), QtCore.SIGNAL('activated()'),
                     self.ayuda)

        #contenedor de ventanas internas
        self.setCentralWidget(QtGui.QMdiArea(self))
        self.centralWidget().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.centralWidget().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # ------ Instanciar ventanas MDI
        action_subwin = [
            (self.actionAltaCliente, Cliente.create, "id_alta_clt"),
            (self.actionBajaCliente, Cliente.delete, "id_baja_clt"),
            (self.actionModificarCliente, Cliente.update, "id_mod_clt"),
            (self.actionAltaMedicamento, Medicamento.create, "id_alta_med"),
            (self.actionBajaMedicamento, Medicamento.delete, "id_baja_med"),
            (self.actionModificarMedicamento, Medicamento.update, "id_mod_med"),
            (self.actionAltaMonodroga, Monodroga.create, "id_alta_mon"),
            (self.actionBajaMonodroga, Monodroga.delete, "id_baja_mon"),
            (self.actionModificarMonodroga, Monodroga.update, "id_mod_mon"),
            (self.actionAltaPresentacion, Presentacion.create, "id_alta_pres"),
            (self.actionBajaPresentacion, Presentacion.delete, "id_baja_pres"),
            (self.actionModificarPresentacion, Presentacion.update, "id_mod_pres"),
            (self.actionAltaProducto, Producto.create, "id_alta_prod"),
            (self.actionBajaProducto, Producto.delete, "id_baja_prod"),
            (self.actionModificarProducto, Producto.update, "id_mod_prod"),
            (self.actionAltaLote, Lote.create, "id_alta_lote"),
            (self.actionModificarLote, Lote.update, "id_mod_lote"),
            (self.actionBajaRemito, Remito.delete, "id_baja_rem"),
            (self.actionModificarRemito, Remito.update, "id_mod_rem"),
            (self.actionDevolucionDeCliente, DevolucionDeCliente, "id_dev_clt"),
            (self.actionFraccionarProducto, FraccionarProducto, "id_fracc_prod"),
            (self.actionIngresar, Ingresar, "id_ing"),
            (self.actionListar, Listar, "id_gen_list"),
            (self.actionRegistrarCobroRemito, RegistrarCobroRemito, "id_reg_cob_rem"),
            (self.actionReintegroCliente, ReintegroCliente, "id_reint_clt"),
            (self.actionVentaContado, VentaContado, "id_vent_cont"),
            (self.actionVentaConRemito, VentaConRemito, "id_vent_rem"),
            (self.actionAjusteNegativoStock, AjusteNegativoStock, "id_ajuste_neg_stock"),
            (self.actionAyuda, Ayuda, "id_ayuda"),
            (self.actionAcercaDe, AcercaDe, "id_acerca" )
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
        for action, subwin, ventana in action_subwin:
            mdi = MyMdi(self)
            subwidget = subwin(mdi)
            subwidget.setVentana(ventana)
            instances.append(subwidget)
            if (type(subwidget) == Ayuda):
                self.ayuda = subwidget
            mdi.setWidget(subwidget)
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
            "AjusteNegativoStock", "Ayuda","AcercaDe"]

        dict = {}
        for nro, obj in enumerate(instances):
            dict[nombres_ventanas[nro]] = obj

        PoolOfWindows.addPool(dict)
        PoolOfWindows.setHandlers()

    def cerrar(self):
        signal = QtGui.QMessageBox.warning(self, 'Atención', 'Esta seguro que desea salir?',
                                  QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        if (signal == QtGui.QMessageBox.Ok):
            self.close()

    # ----- muestra un mensaje en la barra de estado de la ventan principal
    def setBarraEstado(self, estado):
        """
            Muestra mensajes en la barra de estado de
            la ventana principal
        :param estado Mensaje:
        :return:
        """
        self.statusBar().showMessage(estado)

    def ayuda(self):
        if(type(self.focusWidget().parent()) is QGroupBox):
            self.ayuda.ayudaVentana(self.focusWidget().parent().parent().getVentana())
        else:
            self.ayuda.ayudaVentana(self.focusWidget().parent().getVentana())
        self.ayuda.show()

    # ----- deshabilita los menu y actions cada vez que se llama a la ventana ingresar

    def deshabilitarMenu(self):
        """
            Deshabilita las opciones que no corresponden con
            el rol del usuario
        :return:
        """
        for hab in self.tecnico_farmaceutico:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(False)
            else:
                hab.setVisible(False)

    # ----- Devuelve la sesion de la BD
    def getSesionBD(self):
        """
            Retorno la Sesion actual con la Base de Datos
        :return Session:
        """
        return self.sesion

    def config(self):
        """
            Configuración del programa mediante archivo externo
        :return:
        """
        from configparser import ConfigParser
        config = ConfigParser()
        config.read("Configuracion.cfg")
        ##
        a = config.get("Excel", "path")
        Listar.path_excel_files = str(a)
        a = config.get("BaseDatos", "user")
        self.user = a
        a = config.get("BaseDatos", "host")
        self.host = a
        a = config.get("BaseDatos", "password")
        self.password = a
        a = config.get("PlazoDevolucion","plazo")
        DevolucionDeCliente.plazo = a
        a = config.get("PlazoReintegro","plazo")
        ReintegroCliente.plazo = a



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.showMaximized()
    sys.exit(app.exec_())

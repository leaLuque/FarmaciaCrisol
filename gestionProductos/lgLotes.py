# coding: latin-1

__author__ = 'waldo'

import re

from datetime import datetime, date
from PyQt4 import QtCore, QtGui

from gui import MdiWidget, CRUDWidget
from gui.signals import PoolOfWindows
from ventanas import Ui_vtnLote
from validarDatos import ValidarDatos
from baseDatos import Lote as LoteModel
from baseDatos import LoteProducto as LoteProductoModel
from baseDatos import Producto as ProductoModel

class Lote(CRUDWidget, Ui_vtnLote):
    """
    Lógica de Alta y Modificación de Lotes.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase Lote.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(LoteModel)
        self.setFecha()
        self.producto = None

    def cargarLotes(self):
        """
        Carga los datos de los lotes en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaLote,
            LoteModel.buscarTodos("codigo", self.sesion).all(),
            ("codigo", "fecha_vencimiento")
        )

    def crear(self):
        """
        Da de alta un lote nuevo y lo almacena en la base de datos.
        :return:
        """
        if self.producto == None:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ningun Producto de la tabla.',
                                      'Aceptar')
        else:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                if self.dateFechVenc.dateTime().toPyDateTime().date() > date.today():
                    lote = LoteModel(str(self.lineCodigo.text()), str(self.dateFechVenc.text()))
                    if lote.guardar(self.sesion):
                        QtGui.QMessageBox.information(self, 'Info', 'El Lote fue dado de alta.', 'Aceptar')
                        loteProducto = LoteProductoModel(lote.getCodigo(), self.producto,
                                                                 int(self.spinCantidad.value()))
                        if loteProducto.guardar(self.sesion):
                            QtGui.QMessageBox.information(self, 'Info', 'Lote/Producto fue dado de alta.', 'Aceptar')
                        else:
                            QtGui.QMessageBox.critical(self, 'Error', 'Lote/Producto ya existe.', 'Aceptar')
                        self.limpiarCampos()
                        self.objectCreated.emit()
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'El Lote ya existe.', 'Aceptar')
                else:
                    QtGui.QMessageBox.critical(self, 'Error',
                                               'La fehca de vencimiento debe ser mayor a la fecha actual.', 'Aceptar')
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                      'Aceptar')

    def modificar(self):
        """
        Modifica los datos del lote seleccionado.
        :return:
        """
        itemActual = self.tablaLote.currentItem()
        if itemActual != None:
            if self.dateFechVenc.dateTime().toPyDateTime().date() > date.today():
                row = itemActual.row()
                codigo = str(self.tablaLote.item(row, 0).text())
                self.lote = LoteModel.buscar(LoteModel.codigo, self.sesion, codigo).first()
                self.lote.setFechaVencimiento(str(self.dateFechVenc.text()))
                self.lote.modificar(self.sesion)
                QtGui.QMessageBox.information(self, 'Info', 'El Lote fue modificado.', 'Aceptar')
                self.objectModified.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error',
                                           'La fehca de vencimiento debe ser mayor a la fecha actual.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado un Lote de la tabla.', 'Aceptar')

    def buscarLote(self):
        """
        Busca y carga en la tabla los datos de un lote para un codigo ingresado.
        :return:
        """
        codigo = str(self.lineCodigo.text())
        data = self.getAllTabla(self.tablaLote)

        if codigo != "":
            dataLote = filter(lambda x: x[0].upper() == codigo.upper(), data.values())
        else:
            dataLote = data.values()

        for dato in data:
            self.tablaLote.setRowHidden(dato, False)

        for dato in data:
            if not data[dato] in dataLote:
                self.tablaLote.setRowHidden(dato, True)

    def buscarProducto(self):
        """
        Busca y carga en la tabla los datos de un producto para un codigo de barra ingresado.
        :return:
        """
        cod_barra = str(self.lineCod_Barra.text())
        data = self.getAllTabla(self.tablaProducto)

        if cod_barra != "":
            dataProd = filter(lambda x: x[0].upper() == cod_barra.upper(), data.values())
        else:
            dataProd = data.values()

        for dato in data:
            self.tablaProducto.setRowHidden(dato, False)

        for dato in data:
            if not data[dato] in dataProd:
                self.tablaProducto.setRowHidden(dato, True)

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tablaLote)
        self.cargarLotes()
        self.actualizarProd()

    def actualizarProd(self):
        """
        Actualiza la tabla que muestra los datos de los productos.
        :return:
        """
        self.limpiarTabla(self.tablaProducto)
        self.cargarProductos()

    def actualizarLote(self):
        """
        Actualiza la tabla que muestra los datos de los productos.
        :return:
        """
        self.limpiarTabla(self.tablaLote)
        self.cargarLotes()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineCodigo.clear()
        self.lineCodigo.setEnabled(True)
        self.lineCod_Barra.clear()
        self.spinCantidad.setValue(1)
        self.tablaProducto.setCurrentItem(None)
        self.producto = None
        self.setFecha()

    def cargarCampos(self):
        """
        Carga los campos con los datos del lote seleccionado.
        :return:
        """
        self.lineCodigo.setEnabled(False)
        row = self.tablaLote.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaLote.columnCount()):
            infoItem.append(self.tablaLote.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCodigo.setText(infoItem[0])
        formato = "%Y-%m-%d"
        fechaVenc = datetime.strptime(str(infoItem[1]), formato)
        formato = "%d/%m/%Y"
        f = fechaVenc.strftime(formato)
        formato = "dd/MM/yyyy"
        fecha = QtCore.QDate.fromString(str(f), formato)
        self.dateFechVenc.setDate(fecha)

    def setFecha(self):
        """
        Setea la fecha del Date Edit (campo de la fecha) con la fecha actual.
        :return:
        """
        formato = "%d/%m/%Y"  # Asigna un formato dia mes año
        fechaAct = date.today()
        fechaVenc = fechaAct.strftime(formato)
        formato = "dd/MM/yyyy"
        fecha = QtCore.QDate.fromString(fechaVenc, formato)
        self.dateFechVenc.setDate(fecha)

    def cargarProductos(self):
        """
        Carga la tabla de los productos con los datos de todos los productos disponibles.
        :return:
        """
        self.cargarObjetos(self.tablaProducto,
            ProductoModel.buscarTodos("codigo_barra", self.sesion).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "importe")
        )

    def setProducto(self):
        """
        Setea la referencia al producto con el producto seleccionado.
        :return:
        """
        row = self.tablaProducto.currentItem().row()
        self.producto = str(self.tablaProducto.item(row, 0).text())
        self.lineCod_Barra.setText(self.producto)

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Lote.
        :param mdi: referencia a la ventana Alta Lote.
        :return: gui
        """
        gui = super(Lote, cls).create(mdi)
        gui.tablaLote.hide()
        gui.btnBuscarLote.hide()
        gui.cargarProductos()
        gui.tablaProducto.itemClicked.connect(gui.setProducto)
        gui.lineCod_Barra.returnPressed.connect(gui.buscarProducto)
        gui.btnBuscarProd.pressed.connect(gui.buscarProducto)
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

    @classmethod
    def update(cls, mdi):
        """
        Configuración de la ventana Modificación Lote.
        :param mdi: referencia a la ventana Modificación Lote.
        :return: gui
        """
        gui = super(Lote, cls).update(mdi)
        gui.cargarLotes()
        gui.gbProducto.hide()
        gui.labelCantidad.hide()
        gui.spinCantidad.hide()
        gui.tablaLote.itemClicked.connect(gui.cargarCampos)
        gui.lineCodigo.returnPressed.connect(gui.buscarLote)
        gui.btnBuscarLote.pressed.connect(gui.buscarLote)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

    def addHandlerSignal(self):
        self.sender = PoolOfWindows.getVentana("AltaProducto")
        self.sender.objectCreated.connect(self.actualizar)
        self.sender1 = PoolOfWindows.getVentana("BajaProducto")
        self.sender1.objectDeleted.connect(self.actualizar)
        self.sender2 = PoolOfWindows.getVentana("ModificarProducto")
        self.sender2.objectModified.connect(self.actualizar)
# coding: latin-1
__author__ = 'waldo'

import re

from datetime import datetime, date, timedelta
from PyQt4 import QtCore, QtGui

from gui import MdiWidget, CRUDWidget
from gui.signals import PoolOfWindows
from ventanas import Ui_vtnProducto, Ui_vtnFraccionarProducto, Ui_vtnAjusteNegativoStock
from validarDatos import ValidarDatos
from baseDatos import Presentacion as PresentacionModel
from baseDatos import Lote as LoteModel
from baseDatos import LoteProducto as LoteProductoModel
from baseDatos import Producto as ProductoModel
from baseDatos import Medicamento as MedicamentoModel
from baseDatos import DetalleRemito as DetalleRemitoModel
from baseDatos import Remito as RemitoModel
from baseDatos import DetalleFactura as DetalleFacturaModel
from baseDatos import FacturaLiquidacion as FacturaLiquidacionModel
from baseDatos import Factura as FacturaModel
from baseDatos import CobroObraSocial  as CobroObraSocialModel

class Producto(CRUDWidget, Ui_vtnProducto):
    """
    Lógica del ABM de producto.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase Producto.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(ProductoModel)
        self.lote = None
        self.cantLoteProd = False

    def cargarProductos(self):
        """
        Carga los datos de los productos en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaProducto,
            ProductoModel.buscarTodos("codigo_barra", self.sesion).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "importe")
        )

    def crear(self):
        """
        Da de alta un producto nuevo y lo almacena en la base de datos.
        :return:
        """
        itemActualMed = self.tablaMedicamento.currentItem()
        if itemActualMed == None:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ningun Medicamento de la tabla.', 'Aceptar')
        else:
            row = itemActualMed.row()
            medicamento = str(self.tablaMedicamento.item(row, 0).text())
            itemActualPres = self.tablaPresentacion.currentItem()
            if itemActualPres == None:
                QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ninguna Presentación de la tabla.',
                                          'Aceptar')
            else:
                row = itemActualPres.row()
                presentacion = str(self.tablaPresentacion.item(row, 0).text())
                if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                    if self.cantLoteProd:
                        producto = ProductoModel(str(self.lineCodigo_Barra.text()), medicamento,
                                                 presentacion, str(self.lineImporte.text()))
                        if self.validarLote(producto):
                            if producto.guardar(self.sesion):
                                QtGui.QMessageBox.information(self, 'Info', 'El Producto fue dado de alta.', 'Aceptar')
                                if self.lote == None:
                                    self.lote = LoteModel(str(self.lineCod_Lote.text()),
                                                          str(self.dateFechVenc.text()))
                                    if self.lote.guardar(self.sesion):
                                        QtGui.QMessageBox.information(self, 'Info', 'El Lote fue dado de alta.', 'Aceptar')
                                    else:
                                        QtGui.QMessageBox.critical(self, 'Error', 'El Lote ya existe.', 'Aceptar')
                                loteProducto = LoteProductoModel(self.lote.getCodigo(),
                                                                 str(self.lineCodigo_Barra.text()),
                                                                 int(self.spinCantidad.value()))
                                if loteProducto.guardar(self.sesion):
                                    QtGui.QMessageBox.information(self, 'Info', 'Lote/Producto fue dado de alta.', 'Aceptar')
                                else:
                                    QtGui.QMessageBox.critical(self, 'Error', 'Lote/Producto ya existe.', 'Aceptar')
                                self.actualizar()
                                self.objectCreated.emit()
                            else:
                                QtGui.QMessageBox.critical(self, 'Error', 'El Producto ya existe.', 'Aceptar')
                        else:
                            QtGui.QMessageBox.critical(self, 'Error', 'El Producto no puedo asociarse a un lote asociado'
                                                                      ' a otro tipo de producto (distinto medicamento).'
                                                       , 'Aceptar')
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'El Lote ya fue asignado a dos productos.',
                                                  'Aceptar')
                else:
                    QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                              'Aceptar')

    def validarLote(self, producto):
        if self.lote != None:
            loteProd = LoteProductoModel.buscar(LoteProductoModel.id_lote, self.sesion, self.lote.getCodigo()).all()
            if loteProd.__len__() == 1:
                for lp in loteProd:
                    prod = ProductoModel.buscar(ProductoModel.codigo_barra, self.sesion, lp.getIdProducto()).first()
                    if prod.getIdMedicamento() != producto.getIdMedicamento():
                        return False
        return True

    def eliminar(self):
        """
        Da de baja el producto seleccionado.
        :return:
        """
        itemActual = self.tablaProducto.currentItem()
        if itemActual == None:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ningun Producto de la tabla.', 'Aceptar')
        else:
            row = itemActual.row()
            codigo_barra = str(self.tablaProducto.item(row, 0).text())
            if (self.stock(codigo_barra)):
                if self.bajaValida(codigo_barra):
                    self.producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra,
                                                             self.sesion, codigo_barra).first()
                    self.actualizarLoteProd(self.producto.getCodigoBarra())
                    self.producto.borrar(self.sesion)
                    QtGui.QMessageBox.information(self, 'Info', 'El Producto ha sido dado de baja.', 'Aceptar')
                    self.tablaProducto.removeRow(row)
                    self.objectDeleted.emit()
                    self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Existe stock para el Producto seleccionado. '
                                                          'No puede ser dado de baja', 'Aceptar')

    def stock(self, cod_barra):
        lote_producto = LoteProductoModel.buscar(LoteProductoModel.id_producto, self.sesion, cod_barra).all()
        for lp in lote_producto:
            if (lp.getCantidad() > 0):
                return False
        return True

    def actualizarLoteProd(self, producto):
        """
        Actualiza la cantidad de un producto para un lote determinado.
        :param producto: referencia del producto al cual se le actualiza la cantidad.
        :return:
        """
        lote_producto = LoteProductoModel.buscar(LoteProductoModel.id_producto,
                                                 self.sesion, producto).all()
        for lp in lote_producto:
            lp.setCantidad(0)
            lp.modificar(self.sesion)

    def modificar(self):
        """
        Modifica los datos del producto seleccionada.
        :return:
        """
        itemActual = self.tablaProducto.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios([self.lineImporte]):
                row = itemActual.row()
                codigo_barra = str(self.tablaProducto.item(row, 0).text())
                self.producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra,
                                                         self.sesion, codigo_barra).first()
                self.producto.setImporte(str(self.lineImporte.text()))
                self.producto.modificar(self.sesion)
                QtGui.QMessageBox.information(self, 'Info', 'El Producto fue modificado.', 'Aceptar')
                self.objectModified.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado un Producto de la tabla.', 'Aceptar')

    def bajaValida(self, codigo_barra):
        """
        Verifica que el producto no figure en remitos pendientes de pago, facturas liquidadas pendientes de pago o
        facturas pendientes de liquidación.
        :param codigo_barra:
        :return:
        """
        detalleRemito = DetalleRemitoModel.buscarAlta(DetalleRemitoModel.producto,
                                                      self.sesion, codigo_barra).all()
        for dr in detalleRemito:
            remito = RemitoModel.buscarAlta(RemitoModel.numero, self.sesion, dr.getIdRemito()).first()
            if not (remito.getAnulado()):
                if remito.getCobrado() == None:
                    QtGui.QMessageBox.critical(self, 'Error', 'Existen remitos pendientes de pago '
                                                              'en los que figura dicho Producto.', 'Aceptar')
                    return False
        detalleFactura = DetalleFacturaModel.buscar(DetalleFacturaModel.producto,
                                                      self.sesion, codigo_barra).all()
        for df in detalleFactura:
            factura = FacturaModel.buscar(FacturaModel.numero, self.sesion, df.getIdFactura()).first()
            if not (factura.getAnulado()):
                if df.getDescuento() > 0:
                    facturaLiquidacion = FacturaLiquidacionModel.buscar(FacturaLiquidacionModel.nro_factura,
                                                        self.sesion, df.getIdFactura()).first()
                    if facturaLiquidacion:
                        cobroObraSocial = CobroObraSocialModel.buscar(
                                                        CobroObraSocialModel.id_factura_liquidacion, self.sesion,
                                                        facturaLiquidacion.getNumero()).first()
                        if cobroObraSocial == None:
                            QtGui.QMessageBox.critical(self, 'Error', 'Existen facturas liquidadas pendientes'
                                                                ' de cobro a la obra social en las que figura '
                                                                'dicho Producto.', 'Aceptar')
                            return False
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'Existen facturas pendientes de liquidación'
                                                                ' en las que figura dicho Producto.', 'Aceptar')
                        return False
                elif factura.getFechaEmision() + timedelta(days=7) >= date.today():
                    QtGui.QMessageBox.critical(self, 'Error', 'El plazo de devolución de la factura no ha vencido.',
                                               'Aceptar')
                    return False
        return True

    def cargarCamposBaja(self):
        """
        Carga los campos con los datos del producto seleccionado.
        :return:
        """
        self.spinCantidad.setEnabled(False)
        self.lineNomb_Med.setEnabled(False)
        self.lineTipo_Pres.setEnabled(False)
        self.lineImporte.setEnabled(False)
        self.dateFechVenc.setEnabled(False)
        self.lineCod_Lote.setEnabled(False)
        self.cargarCamposMod()

    def buscarProducto(self):
        """
        Busca y carga en la tabla los datos de un producto para un código de barra ingresado.
        :return:
        """
        cod_barra = str(self.lineCodigo_Barra.text())
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

    def buscarPresentacion(self):
        """
        Busca y carga en la tabla los datos de una presentación para un tipo ingresado.
        :return:
        """
        tipo = str(self.lineTipo_Pres.text())
        data = self.getAllTabla(self.tablaPresentacion)

        if tipo != "":
            dataPres = filter(lambda x: x[0].upper() == tipo.upper(), data.values())
        else:
            dataPres = data.values()

        for dato in data:
            self.tablaPresentacion.setRowHidden(dato, False)

        for dato in data:
            if not data[dato] in dataPres:
                self.tablaPresentacion.setRowHidden(dato, True)

    def buscarMedicamento(self):
        """
        Busca y carga en la tabla los datos de un medicamento para un nombre comercial ingresado.
        :return:
        """
        nomb = str(self.lineNomb_Med.text())
        data = self.getAllTabla(self.tablaMedicamento)

        if nomb != "":
            dataMed = filter(lambda x: x[0].upper() == nomb.upper(), data.values())
        else:
            dataMed = data.values()

        for dato in data:
            self.tablaMedicamento.setRowHidden(dato, False)

        for dato in data:
            if not data[dato] in dataMed:
                self.tablaMedicamento.setRowHidden(dato, True)

    def buscarLote(self):
        """
        Busca y carga en la tabla los datos de un lote para un código ingresado.
        :return:
        """
        self.lote = LoteModel.buscar(LoteModel.codigo, self.sesion, str(self.lineCod_Lote.text())).first()
        if self.lote != None:
            loteProducto = LoteProductoModel.buscar(LoteProductoModel.id_lote, self.sesion,
                                                              str(self.lineCod_Lote.text())).all()
            if loteProducto.__len__() < 2:
                self.cantLoteProd = True
            else:
                self.cantLoteProd = False
            self.dateFechVenc.setEnabled(False)
            formato = "%Y-%m-%d"
            fechaVenc = datetime.strptime(str(self.lote.fecha_vencimiento), formato)
            formato = "%d/%m/%y"
            f = fechaVenc.strftime(formato)
            formato = "dd/MM/yy"
            fecha = QtCore.QDate.fromString(str(f), formato)
            self.dateFechVenc.setDate(fecha)
        else:
            self.cantLoteProd = True
            self.setFecha()
            self.dateFechVenc.setEnabled(True)

    def setFecha(self):
        """
        Setea la fecha del Date Edit (campo de la fecha) con la fecha actual.
        :return:
        """
        formato = "%d/%m/%y"  # Asigna un formato dia mes año
        fechaAct = datetime.today()
        fechaVenc = fechaAct.strftime(formato)
        formato = "dd/MM/yy"
        fecha = QtCore.QDate.fromString(fechaVenc, formato)
        self.dateFechVenc.setDate(fecha)

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tablaProducto)
        self.cargarProductos()
        self.actualizarInfoMed()
        self.actualizarInfoPres()

    def actualizarInfoPres(self):
        """
        Actualiza la tabla de las presentaciones con los datos modificados.
        :return:
        """
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarPresentaciones()

    def actualizarInfoMed(self):
        """
        Actualiza la tabla de los medicamentos con los datos modificados.
        :return:
        """
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarMedicamentos()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineCodigo_Barra.clear()
        self.lineCodigo_Barra.setEnabled(True)
        self.lineImporte.clear()
        self.lineNomb_Med.clear()
        self.lineTipo_Pres.clear()
        self.spinCantidad.setValue(1)
        self.setFecha()
        self.lineCod_Lote.clear()
        self.tablaMedicamento.setCurrentItem(None)
        self.tablaProducto.setCurrentItem(None)
        self.tablaPresentacion.setCurrentItem(None)
        self.lote = None
        self.cantLoteProd = False
        self.dateFechVenc.setEnabled(False)

    def cargarCamposMod(self):
        """
        Carga los campos con los datos del producto seleccionado.
        :return:
        """
        self.lineCodigo_Barra.setEnabled(False)
        row = self.tablaProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaProducto.columnCount()):
            infoItem.append(self.tablaProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCodigo_Barra.setText(infoItem[0])
        self.lineImporte.setText(infoItem[3])

    def cargarPresentaciones(self):
        """
        Carga la tabla de las presentaciones con los datos de todos las presentaciones disponibles.
        :return:
        """
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarTodos("tipo", self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion")
        )

    def cargarMedicamentos(self):
        """
        Carga la tabla de los medicamentos con los datos de todos los medicamentos disponibles.
        :return:
        """
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarTodos("nombre_comercial", self.sesion).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def setMedicamento(self):
        """
        Setea la referencia al medicamento con el medicamento seleccionado.
        :return:
        """
        row = self.tablaMedicamento.currentItem().row()
        self.medicamento = str(self.tablaMedicamento.item(row, 0).text())
        self.lineNomb_Med.setText(self.medicamento)

    def setPresentacion(self):
        """
        Setea la referencia a la presentación con la presentación seleccionada.
        :return:
        """
        row = self.tablaPresentacion.currentItem().row()
        self.presentacion = str(self.tablaPresentacion.item(row, 0).text())
        self.lineTipo_Pres.setText(self.presentacion)

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Producto.
        :param mdi: referencia a la ventana Alta Producto.
        :return: gui
        """
        gui = super(Producto, cls).create(mdi)
        gui.tablaProducto.hide()
        gui.btnBuscarProd.hide()
        gui.dateFechVenc.setEnabled(False)
        gui.cargarPresentaciones()
        gui.cargarMedicamentos()
        gui.setFecha()
        gui.lineCod_Lote.returnPressed.connect(gui.buscarLote)
        gui.btnBuscarLote.pressed.connect(gui.buscarLote)
        gui.lineNomb_Med.returnPressed.connect(gui.buscarMedicamento)
        gui.btnBuscarMed.pressed.connect(gui.buscarMedicamento)
        gui.lineTipo_Pres.returnPressed.connect(gui.buscarPresentacion)
        gui.btnBuscarPres.pressed.connect(gui.buscarPresentacion)
        gui.tablaMedicamento.itemClicked.connect(gui.setMedicamento)
        gui.tablaPresentacion.itemClicked.connect(gui.setPresentacion)
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

    @classmethod
    def delete(cls, mdi):
        """
        Configuración de la ventana Baja Producto.
        :param mdi: referencia a la ventana Baja Producto.
        :return: gui
        """
        gui = super(Producto, cls).delete(mdi)
        gui.lineImporte.setEnabled(False)
        gui.gbMedicamento.hide()
        gui.gbPresentacion.hide()
        gui.gbLote.hide()
        gui.linea1.hide()
        gui.linea2.hide()
        gui.linea3.hide()
        gui.lineCodigo_Barra.returnPressed.connect(gui.buscarProducto)
        gui.btnBuscarProd.pressed.connect(gui.buscarProducto)
        gui.cargarProductos()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tablaProducto.itemClicked.connect(gui.cargarCamposBaja)
        return gui

    @classmethod
    def update(cls, mdi):
        """
        Configuración de la ventana Modificación Producto.
        :param mdi: referencia a la ventana Modificación Producto.
        :return: gui
        """
        gui = super(Producto, cls).update(mdi)
        gui.cargarProductos()
        gui.tablaProducto.itemClicked.connect(gui.cargarCamposMod)
        gui.gbMedicamento.hide()
        gui.gbPresentacion.hide()
        gui.gbLote.hide()
        gui.linea1.hide()
        gui.linea2.hide()
        gui.linea3.hide()
        gui.lineCodigo_Barra.returnPressed.connect(gui.buscarProducto)
        gui.btnBuscarProd.pressed.connect(gui.buscarProducto)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

    def addHandlerSignal(self):

        self.sender = PoolOfWindows.getVentana("AltaMedicamento")
        self.sender.objectCreated.connect(self.actualizarInfoMed)
        self.sender1 = PoolOfWindows.getVentana("BajaMedicamento")
        self.sender1.objectDeleted.connect(self.actualizarInfoMed)
        self.sender2 = PoolOfWindows.getVentana("ModificarMedicamento")
        self.sender2.objectModified.connect(self.actualizarInfoMed)
        self.sender3 = PoolOfWindows.getVentana("AltaPresentacion")
        self.sender3.objectCreated.connect(self.actualizarInfoPres)
        self.sender4 = PoolOfWindows.getVentana("BajaPresentacion")
        self.sender4.objectDeleted.connect(self.actualizarInfoPres)
        self.sender5 = PoolOfWindows.getVentana("ModificarPresentacion")
        self.sender5.objectModified.connect(self.actualizarInfoPres)

class FraccionarProducto(CRUDWidget, Ui_vtnFraccionarProducto):
    """
    Lógica del Fraccionado de productos.
    """
    def __init__(self, mdi):
        """
        Cosntructor de la clase FraccionarProducto.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.lineCod_Barra.returnPressed.connect(self.buscarPorProducto)
        self.btnBuscar.pressed.connect(self.buscarPorProducto)
        self.cargarProductos()
        self.tablaProducto.itemClicked.connect(self.cargarFraccionables)
        #self.btnActualizar.pressed.connect(self.actualizarInfo)
        self.btnAceptar.pressed.connect(self.fraccionar)
        self.btnCancelar.pressed.connect(self.actualizar)

    def validadores(self):
        """
        Setea los campos obligatorios, junto con los validadores de cada campo.
        :return:
        """
        ##Esta parte analiza los campos requeridos para el cliente
        self.camposRequeridos = [self.lineCod_Barra]
        ValidarDatos.setValidador(self.camposRequeridos)

    def cargarProductos(self):
        """
        Carga la tabla de los productos con los datos de todos los productos disponibles,
        junto con el lote al que pertenecen.
        :return:
        """
        self.cargarObjetos(self.tablaProducto,
            LoteProductoModel.buscarTodosLoteProducto(self.sesion, ProductoModel, LoteModel).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def fraccionar(self):
        """
        Fracciona un producto. Da de alta y almacena un nuevo producto en la base de datos
        de acuerdo al producto seleccionado para fraccionar, o si ya existe actualiza la cantidad.
        :return:
        """
        itemActual = self.tablaProducto.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                if self.tablaFraccionable.rowCount() > 0:
                    itemFracc = self.tablaFraccionable.currentItem()
                    if itemFracc != None:
                        row = itemActual.row()
                        codigo_barra = str(self.tablaProducto.item(row, 0).text())
                        codigo_lote = str(self.tablaProducto.item(row, 3).text())
                        self.loteProducto = LoteProductoModel.buscarLoteProducto(self.sesion, codigo_barra,
                                                                                  codigo_lote).first()
                        if int(self.spinCantidad.value()) > int(self.loteProducto.getCantidad()):
                            QtGui.QMessageBox.warning(self, 'Atención', 'La cantidad ingresada no puede ser mayor a la '
                                                        'cantidad del Producto.', 'Aceptar')
                        else:
                            resto = int(self.loteProducto.getCantidad()) - int(self.spinCantidad.value())
                            self.loteProducto.setCantidad(resto)
                            self.loteProducto.modificar(self.sesion)
                            cantidadFracciones = self.cantidadFracciones(codigo_barra,
                                                                         int(self.spinCantidad.value()))
                            row = itemFracc.row()
                            codigo_barra = str(self.tablaFraccionable.item(row, 0).text())
                            self.loteProducto = LoteProductoModel.buscarLoteProducto(self.sesion,
                                                                                     codigo_barra,
                                                                                      codigo_lote).first()
                            if self.loteProducto:
                                suma = int(self.loteProducto.cantidad) + int(cantidadFracciones)
                                self.loteProducto.setCantidad(suma)
                                self.loteProducto.modificar(self.sesion)
                            else:
                                loteProducto = LoteProductoModel(codigo_lote, codigo_barra,
                                                                     int(cantidadFracciones))
                                if loteProducto.guardar(self.sesion):
                                    QtGui.QMessageBox.information(self, 'Info', 'Lote/Producto fue dado de alta.', 'Aceptar')
                                else:
                                    QtGui.QMessageBox.critical(self, 'Error', 'Lote/Producto ya existe.', 'Aceptar')
                            QtGui.QMessageBox.information(self, 'Info', 'La cantidad fue modificada.', 'Aceptar')
                            self.actualizar()
                            self.objectModified.emit()
                    else:
                        QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado un Fraccionable de la tabla.', 'Aceptar')
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'El Producto seleccionado no puede fraccionarse.', 'Aceptar')
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado un Producto de la tabla.', 'Aceptar')

    def cantidadFracciones(self, codigo, cantidad):
        """
        Calcula y devuelve la cantidad del poducto (subproducto, fracciones del producto fraccionable),
        número de fracciones * cantidad a fraccionar.
        :param codigo: Código del producto a fraccionar.
        :param cantidad: Cantidad a fraccionar.
        :return: resultado
        """
        producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra, self.sesion, codigo).first()
        presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo, self.sesion,
                                                    producto.id_presentacion).first()
        resultado = int(presentacion.getCantidadFracciones()) * cantidad
        return resultado

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.actualizarInfo()
        self.limpiarTabla(self.tablaFraccionable)

    def actualizarInfo(self):
        """
        Actualiza la tabla de los productos con los datos modificados.
        :return:
        """
        self.limpiarTabla(self.tablaProducto)
        self.cargarProductos()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineCod_Barra.clear()

    def cargarFraccionables(self):
        """
        Carga la tabla de los productos (subproducto, fracciones del producto fraccionable),
        con los datos de todos los productos (subproducto, fraacciones del producto fraccionable).
        :return:
        """
        #Recuperar la informacion de un item
        row = self.tablaProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaProducto.columnCount()):
            infoItem.append(self.tablaProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCod_Barra.setText(infoItem[0])
        self.limpiarTabla(self.tablaFraccionable)
        self.cargarObjetos(self.tablaFraccionable,
            LoteProductoModel.buscarFraccionable(self.sesion, ProductoModel, LoteModel, PresentacionModel,
                                                            str(self.lineCod_Barra.text())).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def buscarPorProducto(self):
        """
        Busca y carga en la tabla los datos de un producto y su/s lote/s para un código de barra ingresado.
        :return:
        """
        self.limpiarTabla(self.tablaProducto)
        self.cargarObjetos(self.tablaProducto,
            LoteProductoModel.buscarLoteProductoPorProducto(self.sesion, ProductoModel, LoteModel,
                                                            str(self.lineCod_Barra.text())).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def addHandlerSignal(self):

        self.sender = PoolOfWindows.getVentana("AltaProducto")
        self.sender.objectCreated.connect(self.actualizarInfo)
        self.sender1 = PoolOfWindows.getVentana("BajaProducto")
        self.sender1.objectDeleted.connect(self.actualizarInfo)
        self.sender2 = PoolOfWindows.getVentana("ModificarProducto")
        self.sender2.objectModified.connect(self.actualizarInfo)
        self.sender3 = PoolOfWindows.getVentana("AjusteNegativoStock")
        self.sender3.objectModified.connect(self.actualizarInfo)

class AjusteNegativoStock(CRUDWidget, Ui_vtnAjusteNegativoStock):
    """
    Lógica del ajuste negativo del stock de los productos.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase AjusteNegativoStock.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(LoteProductoModel)
        self.lineCod_Barra.returnPressed.connect(self.buscar)
        self.lineCod_Lote.returnPressed.connect(self.buscar)
        self.btnBuscar.pressed.connect(self.buscar)
        self.cargarLoteProducto()
        self.tablaLoteProducto.itemClicked.connect(self.cargarCampos)
        self.btnAceptar.pressed.connect(self.ajuste)
        self.btnCancelar.pressed.connect(self.actualizar)

    def cargarLoteProducto(self):
        """
        Carga los datos de los productos y su/s lote/s en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaLoteProducto,
            LoteProductoModel.buscarTodosLoteProducto(self.sesion, ProductoModel, LoteModel).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def buscar(self):
        """
        Busca y carga en la tabla los datos de un producto y su/s lote/s.
        :return:
        """
        producto = str(self.lineCod_Barra.text())
        lote = str(self.lineCod_Lote.text())
        data = self.getAllTabla(self.tablaLoteProducto)

        if producto != "":
            data_producto = filter(lambda x: x[0].upper() == producto.upper(), data.values())
        else:
            data_producto = data.values()
        if lote != "":
            data_lote = filter(lambda x: x[1].upper() == lote.upper(), data_producto)
        else:
            data_lote = data_producto

        for dato in data:
            self.tablaLoteProducto.setRowHidden(dato,False)

        for dato in data:
            if not data[dato] in data_lote:
                self.tablaLoteProducto.setRowHidden(dato,True)

    def ajuste(self):
        """
        Actualiza la cantidad del producto seleccionado para realizar el ajuste negativo de stock.
        :return:
        """
        itemActual = self.tablaLoteProducto.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                row = itemActual.row()
                codigo_barra = str(self.tablaLoteProducto.item(row, 0).text())
                codigo_lote = str(self.tablaLoteProducto.item(row, 3).text())
                self.loteProducto = LoteProductoModel.buscarLoteProducto(self.sesion, codigo_barra,
                                                                         codigo_lote).first()
                resto = int(self.loteProducto.getCantidad()) - int(self.spinCantidad.value())
                if resto < 0:
                    QtGui.QMessageBox.critical(self, 'Error', 'La cantidad ingresada no puede ser mayor '
                                                                'a la cantidad del Producto.', 'Aceptar')
                else:
                    self.loteProducto.setCantidad(resto)
                    self.loteProducto.modificar(self.sesion)
                    QtGui.QMessageBox.information(self, 'Info', 'La cantidad fue modificada.', 'Aceptar')
                    self.objectModified.emit()
                    self.actualizar()
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                          'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado un Lote/Producto de la tabla.', 'Aceptar')

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.actualizarInfo()

    def actualizarInfo(self):
        """
        Actualiza la tabla de los productos con los datos modificados.
        :return:
        """
        self.limpiarTabla(self.tablaLoteProducto)
        self.cargarLoteProducto()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineCod_Barra.clear()
        self.lineCod_Lote.clear()
        self.spinCantidad.setValue(1)

    def cargarCampos(self):
        """
        Carga los campos con los datos del producto seleccionado.
        :return:
        """
        #Recuperar la informacion de un item
        row = self.tablaLoteProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaLoteProducto.columnCount()):
            infoItem.append(self.tablaLoteProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCod_Barra.setText(infoItem[0])
        self.lineCod_Lote.setText(infoItem[3])

    def addHandlerSignal(self):

        self.sender = PoolOfWindows.getVentana("AltaProducto")
        self.sender.objectCreated.connect(self.actualizarInfo)
        self.sender1 = PoolOfWindows.getVentana("BajaProducto")
        self.sender1.objectDeleted.connect(self.actualizarInfo)
        self.sender2 = PoolOfWindows.getVentana("ModificarProducto")
        self.sender2.objectModified.connect(self.actualizarInfo)
        self.sender3 = PoolOfWindows.getVentana("FraccionarProducto")
        self.sender3.objectModified.connect(self.actualizarInfo)
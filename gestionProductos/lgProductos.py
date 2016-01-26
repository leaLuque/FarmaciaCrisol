__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnProducto, Ui_vtnFraccionarProducto, Ui_vtnAjusteNegativoStock
from validarDatos import ValidarDatos
from baseDatos import Presentacion as PresentacionModel
from baseDatos import Lote as LoteModel
from baseDatos import LoteProducto as LoteProductoModel
from baseDatos import Producto as ProductoModel
from baseDatos import Medicamento as MedicamentoModel
from baseDatos import DetalleRemito as DetalleRemitoModel
from baseDatos import Remito as RemitoModel
from baseDatos import Factura as FacturaModel
from baseDatos import DetalleFactura as DetalleFacturaModel
from baseDatos import FacturaLiquidacion as FacturaLiquidacionModel
from baseDatos import CobroObraSocial  as CobroObraSocialModel
from datetime import datetime
from PyQt4 import QtCore, QtGui
class Producto(CRUDWidget, Ui_vtnProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(ProductoModel)
        self.lote = None
        self.cantLoteProd = False

    def cargarProductos(self):
        self.cargarObjetos(self.tablaProducto,
            ProductoModel.buscarTodos("codigo_barra", self.sesion).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "importe")
        )

    def crear(self):
        itemActualMed = self.tablaMedicamento.currentItem()
        if itemActualMed == None:
            self.showMsjEstado("No se ha seleccionado ningun Medicamento de la tabla")
        else:
            row = itemActualMed.row()
            medicamento = str(self.tablaMedicamento.item(row, 0).text())
            itemActualPres = self.tablaPresentacion.currentItem()
            if itemActualPres == None:
                self.showMsjEstado("No se ha seleccionado ninguna Presentación de la tabla")
            else:
                row = itemActualPres.row()
                presentacion = str(self.tablaPresentacion.item(row, 0).text())
                if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                    if self.cantLoteProd:
                        producto = ProductoModel(str(self.lineCodigo_Barra.text()), medicamento,
                                                 presentacion, str(self.lineImporte.text()))
                        if producto.guardar(self.sesion):
                            self.showMsjEstado("El Producto fue dado de alta.")
                            if self.lote == None:
                                self.lote = LoteModel(str(self.lineCod_Lote.text()),
                                                      str(self.dateFechVenc.text()))
                                if self.lote.guardar(self.sesion):
                                    self.showMsjEstado("El Lote fue dado de alta.")
                                else:
                                    self.showMsjEstado("El Lote ya existe.")
                            loteProducto = LoteProductoModel(self.lote.getCodigo(),
                                                             str(self.lineCodigo_Barra.text()),
                                                             int(self.spinCantidad.value()))
                            if loteProducto.guardar(self.sesion):
                                self.showMsjEstado("Lote/Producto fue dado de alta.")
                            else:
                                self.showMsjEstado("Lote/Producto ya existe.")
                            self.actualizar()
                            self.objectCreated.emit()
                        else:
                            self.showMsjEstado("El Producto ya existe.")
                    else:
                        self.showMsjEstado("El Lote ya fue asignado a dos productos.")
                else:
                    self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def eliminar(self):
        itemActual = self.tablaProducto.currentItem()
        if itemActual == None:
            self.showMsjEstado("No se ha seleccionado ningun Producto de la tabla")
        else:
            row = itemActual.row()
            codigo_barra = str(self.tablaProducto.item(row, 0).text())
            if self.bajaValida(codigo_barra):
                self.producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra,
                                                         self.sesion, codigo_barra).first()
                self.producto.borrar(self.sesion)
                self.showMsjEstado("El Producto ha sido dado de baja")
                self.tablaProducto.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()

    def modificar(self):
        itemActual = self.tablaProducto.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios([self.lineImporte]):
                row = itemActual.row()
                codigo_barra = str(self.tablaProducto.item(row, 0).text())
                self.producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra,
                                                         self.sesion, codigo_barra).first()
                self.producto.setImporte(str(self.lineImporte.text()))
                self.producto.modificar(self.sesion)
                self.showMsjEstado("El Producto fue modificado")
                self.objectModified.emit()
                self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Producto de la tabla")

    def bajaValida(self, codigo_barra):
        detalleRemito = DetalleRemitoModel.buscarAlta(DetalleRemitoModel.producto,
                                                      self.sesion, codigo_barra).all()
        for dr in detalleRemito:
            remito = RemitoModel.buscarAlta(RemitoModel.numero, self.sesion, dr.getIdRemito()).first()
            if remito.getCobrado() == None:
                QtGui.QMessageBox.critical(self, 'Error', 'Existen remitos pendientes de pago '
                                                          'en los que figura dicho Producto.', 'Aceptar')
                return False
        detalleFactura = DetalleFacturaModel.buscar(DetalleFacturaModel.producto,
                                                      self.sesion, codigo_barra).all()
        for df in detalleFactura:
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
        return True

    def cargarCampos(self):
        #Deshabilitar los lines restantes
        self.lineCodigo_Barra.setEnabled(False)
        self.spinCantidad.setEnabled(False)
        self.lineNomb_Med.setEnabled(False)
        self.lineTipo_Pres.setEnabled(False)
        self.lineImporte.setEnabled(False)
        self.dateFechVenc.setEnabled(False)
        self.lineCod_Lote.setEnabled(False)
        #Recuperar la informacion de un item
        row = self.tablaProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaProducto.columnCount()):
            infoItem.append(self.tablaProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCodigo_Barra.setText(infoItem[0])
        self.lineImporte.setText(infoItem[3])

    def buscarProducto(self):
        self.limpiarTabla(self.tablaProducto)
        self.cargarObjetos(self.tablaProducto,
            ProductoModel.buscarAlta(ProductoModel.codigo_barra, self.sesion,
                                     str(self.lineCodigo_Barra.text())).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "importe")
        )


    def buscarPresentacion(self):
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarLike(PresentacionModel.tipo, self.sesion,
                                         str(self.lineTipo_Pres.text())).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion")
        )

    def buscarMedicamento(self):
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarLike(MedicamentoModel.nombre_comercial, self.sesion,
                                        str(self.lineNomb_Med.text())).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def buscarLote(self):
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
        formato = "%d/%m/%y"  # Asigna un formato dia mes año
        fechaAct = datetime.today()
        fechaVenc = fechaAct.strftime(formato)
        formato = "dd/MM/yy"
        fecha = QtCore.QDate.fromString(fechaVenc, formato)
        self.dateFechVenc.setDate(fecha)

    def actualizar(self):
        self.limpiarCampos()
        self.limpiarTabla(self.tablaProducto)
        self.cargarProductos()
        self.actualizarInfoMed()
        self.actualizarInfoPres()

    def actualizarInfoPres(self):
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarPresentaciones()

    def actualizarInfoMed(self):
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarMedicamentos()

    def limpiarCampos(self):
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

    def modificarItem(self):
        self.lineCodigo_Barra.setEnabled(False)
        row = self.tablaProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaProducto.columnCount()):
            infoItem.append(self.tablaProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCodigo_Barra.setText(infoItem[0])
        self.lineImporte.setText(infoItem[3])

    def cargarPresentaciones(self):
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarTodos("tipo", self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion")
        )

    def cargarMedicamentos(self):
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarTodos("nombre_comercial", self.sesion).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def setMedicamento(self):
        row = self.tablaMedicamento.currentItem().row()
        self.medicamento = str(self.tablaMedicamento.item(row, 0).text())
        self.lineNomb_Med.setText(self.medicamento)

    def setPresentacion(self):
        row = self.tablaPresentacion.currentItem().row()
        self.presentacion = str(self.tablaPresentacion.item(row, 0).text())
        self.lineTipo_Pres.setText(self.presentacion)

    @classmethod
    def create(cls, mdi):
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
        gui.btnActualizarMed.pressed.connect(gui.actualizarInfoMed)
        gui.btnActualizarPres.pressed.connect(gui.actualizarInfoPres)
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

    @classmethod
    def delete(cls, mdi):
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
        gui.tablaProducto.itemClicked.connect(gui.cargarCampos)
        return gui

    @classmethod
    def update(cls, mdi):
        gui = super(Producto, cls).update(mdi)
        gui.cargarProductos()
        gui.tablaProducto.itemClicked.connect(gui.modificarItem)
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

class FraccionarProducto(MdiWidget, Ui_vtnFraccionarProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.lineCod_Barra.returnPressed.connect(self.buscarPorProducto)
        self.btnBuscar.pressed.connect(self.buscarPorProducto)
        self.cargarProductos()
        self.tablaProducto.itemClicked.connect(self.cargarCampos)
        self.btnActualizar.pressed.connect(self.actualizarInfo)
        self.btnAceptar.pressed.connect(self.fraccionar)
        self.btnCancelar.pressed.connect(self.actualizar)

    def validadores(self):
        ##Esta parte analiza los campos requeridos para el cliente
        self.camposRequeridos = [self.lineCod_Barra]
        ValidarDatos.setValidador(self.camposRequeridos)

    def cargarProductos(self):
        self.cargarObjetos(self.tablaProducto,
            LoteProductoModel.buscarTodosLoteProducto(self.sesion, ProductoModel, LoteModel).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def fraccionar(self):
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
                            self.showMsjEstado("La cantidad ingresada no puede ser mayor a la "
                                               "cantidad del Producto.")
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
                                    self.showMsjEstado("Lote/Producto fue dado de alta.")
                                else:
                                    self.showMsjEstado("Lote/Producto ya existe.")
                            self.showMsjEstado("La cantidad fue modificada")
                            self.actualizar()
                    else:
                        self.showMsjEstado("No se ha seleccionado un Fraccionable de la tabla.")
                else:
                    self.showMsjEstado("El Producto seleccionado no puede fraccionarse.")
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Producto de la tabla")

    def cantidadFracciones(self, codigo, cantidad):
        producto = ProductoModel.buscarAlta(ProductoModel.codigo_barra, self.sesion, codigo).first()
        presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo, self.sesion,
                                                    producto.id_presentacion).first()
        resultado = int(presentacion.getCantidadFracciones()) * cantidad
        return resultado

    def actualizar(self):
        self.limpiarCampos()
        self.actualizarInfo()
        self.limpiarTabla(self.tablaFraccionable)

    def actualizarInfo(self):
        self.limpiarTabla(self.tablaProducto)
        self.cargarProductos()

    def limpiarCampos(self):
        self.lineCod_Barra.clear()

    def cargarCampos(self):
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
        self.limpiarTabla(self.tablaProducto)
        self.cargarObjetos(self.tablaProducto,
            LoteProductoModel.buscarLoteProductoPorProducto(self.sesion, ProductoModel, LoteModel,
                                                            str(self.lineCod_Barra.text())).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

class AjusteNegativoStock(MdiWidget, Ui_vtnAjusteNegativoStock):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(LoteProductoModel)
        self.lineCod_Barra.returnPressed.connect(self.buscar)
        self.lineCod_Lote.returnPressed.connect(self.buscar)
        self.btnBuscar.pressed.connect(self.buscar)
        self.cargarLoteProducto()
        self.tablaLoteProducto.itemClicked.connect(self.cargarCampos)
        self.btnActualizar.pressed.connect(self.actualizarInfo)
        self.btnAceptar.pressed.connect(self.ajuste)
        self.btnCancelar.pressed.connect(self.actualizar)

    def cargarLoteProducto(self):
        self.cargarObjetos(self.tablaLoteProducto,
            LoteProductoModel.buscarTodosLoteProducto(self.sesion, ProductoModel, LoteModel).all(),
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    def buscar(self):
        obj = self.sender().objectName()
        if obj == 'lineCod_Barra':
            loteProducto = LoteProductoModel.buscarLoteProductoPorProducto(self.sesion, ProductoModel, LoteModel,
                                                            str(self.lineCod_Barra.text())).all()
        elif obj == 'lineCod_Lote':
            loteProducto = LoteProductoModel.buscarLoteProductoPorLote(self.sesion, ProductoModel, LoteModel,
                                                        str(self.lineCod_Lote.text())).all()
        elif obj == 'btnBuscar':
            if str(self.lineCod_Barra.text()) != "":
                loteProducto = LoteProductoModel.buscarLoteProductoPorProducto(self.sesion, ProductoModel, LoteModel,
                                                            str(self.lineCod_Barra.text())).all()
            elif str(self.lineCod_Lote.text()) != "":
                loteProducto = LoteProductoModel.buscarLoteProductoPorLote(self.sesion, ProductoModel, LoteModel,
                                                        str(self.lineCod_Lote.text())).all()
            else:
                self.showMsjEstado("Ingrese Código de Barra del Producto o Código del Lote para realizar la"
                                   " busqueda.")
                return
        self.limpiarTabla(self.tablaLoteProducto)
        self.cargarObjetos(self.tablaLoteProducto, loteProducto,
            ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
        )

    # def buscarPorProducto(self):
    #     self.limpiarTabla(self.tablaLoteProducto)
    #     self.cargarObjetos(self.tablaLoteProducto,
    #         LoteProductoModel.buscarLoteProductoPorProducto(self.sesion, ProductoModel, LoteModel,
    #                                                         str(self.lineCod_Barra.text())).all(),
    #         ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
    #     )
    #
    # def buscarPorLote(self):
    #     self.limpiarTabla(self.tablaLoteProducto)
    #     self.cargarObjetos(self.tablaLoteProducto,
    #         LoteProductoModel.buscarLoteProductoPorLote(self.sesion, ProductoModel, LoteModel,
    #                                                     str(self.lineCod_Lote.text())).all(),
    #         ("codigo_barra", "id_medicamento", "id_presentacion", "codigo", "cantidad")
    #     )

    def ajuste(self):
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
                    self.showMsjEstado("La cantidad ingresada no puede ser mayor a la cantidad del Producto")
                else:
                    self.loteProducto.setCantidad(resto)
                    self.loteProducto.modificar(self.sesion)
                    self.showMsjEstado("La cantidad fue modificada")
                    self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Lote/Producto de la tabla")

    def actualizar(self):
        self.limpiarCampos()
        self.actualizarInfo()

    def actualizarInfo(self):
        self.limpiarTabla(self.tablaLoteProducto)
        self.cargarLoteProducto()

    def limpiarCampos(self):
        self.lineCod_Barra.clear()
        self.lineCod_Lote.clear()
        self.spinCantidad.setValue(1)

    def cargarCampos(self):
        #Recuperar la informacion de un item
        row = self.tablaLoteProducto.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaLoteProducto.columnCount()):
            infoItem.append(self.tablaLoteProducto.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineCod_Barra.setText(infoItem[0])
        self.lineCod_Lote.setText(infoItem[3])

#         self.campos = [self.lineNombMed, self.lineTipoPres, self.lineCodBarra, self.lineImp]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.btnBuscarMed.pressed.connect(self.buscarMedicamento)
#         self.btnBuscarPres.pressed.connect(self.buscarPresentacion)
#         self.lineNombMed.returnPressed.connect(self.buscarMedicamento)
#         self.lineTipoPres.returnPressed.connect(self.buscarPresentacion)
#         self.tablaMedicamento.itemClicked.connect(self.setMedicamento)
#         self.tablaPresentacion.itemClicked.connect(self.setPresentacion)
#         self.columnHeadersPres = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
#         self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
#         self.medicamento = None
#         self.presentacion = None
#
#     def buscarMedicamento(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
#         medicamentos = {}
#         query = Medicamento.buscarLike(Medicamento.nombreComercial, self.sesion, str(self.lineNombMed.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
#             medicamentos[i] = item
#             i += 1
#             self.medicamento = instance.nombreComercial
#         if len(medicamentos.items()) < 1:
#             self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
#         elif len(medicamentos.items()) > 1:
#             self.medicamento = None
#         else:
#             self.lineNombMed.setText(self.medicamento)
#         self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeadersMed)
#
#     def buscarPresentacion(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
#         presentaciones = {}
#         query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipoPres.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#             self.presentacion = instance.tipo
#         if len(presentaciones.items()) < 1:
#             self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
#         elif len(presentaciones.items()) > 1:
#             self.presentacion = None
#         else:
#             self.lineTipoPres.setText(self.presentacion)
#         self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeadersPres)
#
#     def setPresentacion(self):
#         self.presentacion = self.itemSeleccionado(self.tablaPresentacion)
#         self.lineTipoPres.setText(self.presentacion)
#
#     def setMedicamento(self):
#         self.medicamento = self.itemSeleccionado(self.tablaMedicamento)
#         self.lineNombMed.setText(self.medicamento)
#
#     def confirmarOperacion(self):
#         if self.tablaMedicamento.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
#         else:
#             if self.medicamento == None:
#                     self.showMsjEstado("Seleccione un Medicamento de la tabla.")
#             else:
#                 if self.tablaPresentacion.rowCount() < 1:
#                     self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
#                 else:
#                     if self.presentacion == None:
#                         self.showMsjEstado("Seleccione una Presentacion de la tabla.")
#                     else:
#                         if self.validarDatos.validarCamposVacios(self.campos):
#                             producto = Producto(str(self.lineCodBarra.text()),  str(self.lineNombMed.text()),
#                                     str(self.lineTipoPres.text()), str(self.lineImp.text()))
#                             if producto.guardar(self.sesion):
#                                 self.showMsjEstado("El Producto fue dado de alta.")
#                                 self.actualizarVentana()
#                                 self.presentacion = None
#                                 self.medicamento = None
#                             else:
#                                 self.showMsjEstado("El Producto ya existe.")
#                         else:
#                             self.showMsjEstado("Uno o más datos obligatorios no fueron completados.")
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
#         self.lineNombMed.setText("")
#         self.lineTipoPres.setText("")
#         self.lineCodBarra.setText("")
#         self.lineImp.setText("")
#
# class BajaProducto(MdiWidget, Ui_vtnBajaProducto):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.campos = [self.lineCodBarra]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.columnHeaders = ["Código de Barra", "Medicamento", "Presentación", "Importe"]
#         self.tablaProducto.itemClicked.connect(self.obtenerProducto)
#         self.btnBuscar.pressed.connect(self.buscarProductos)
#         self.lineCodBarra.returnPressed.connect(self.buscarProductos)
#         self.producto = None
#
#     def buscarProductos(self):
#         productos = {}
#         if self.validarDatos.validarCamposVacios(self.campos):
#             self.limpiarTabla(self.tablaProducto, self.columnHeaders)
#             query = Producto.buscar(Producto.codigoBarra, self.sesion, str(self.lineCodBarra.text()))
#             i = 0
#             for instance in query.all():
#                 item = [instance.codigoBarra, instance.id_medicamento, instance.id_presentacion, instance.importe]
#                 productos[i] = item
#                 i += 1
#                 self.producto = instance
#             if len(productos.items()) < 1:
#                 self.showMsjEstado("No existen Productos que coincidan con el código de barra ingresado en la busqueda.")
#         else:
#             self.showMsjEstado("Ingrese el código de barra del Producto para poder realizar la busqueda.")
#         self.cargarTabla(self.tablaProducto, productos, self.columnHeaders)
#
#     def obtenerProducto(self):
#         codBarra = self.itemSeleccionado(self.tablaProducto)
#         query = Producto.buscar(Producto.codigoBarra, self.sesion, codBarra)
#         for instance in query.all():
#              self.producto = instance
#
#     def confirmarOperacion(self):
#         if self.tablaProducto.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione un Producto de la tabla.")
#         else:
#             if self.producto == None:
#                 self.showMsjEstado("Seleccione un Producto de la tabla.")
#             else:
#                 self.producto.borrar(self.sesion)
#                 self.showMsjEstado("El Producto fue dado de baja.")
#                 self.actualizarVentana()
#                 self.producto = None
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaProducto, self.columnHeaders)
#         self.lineCodBarra.setText("")
#
# class ModificarProducto(MdiWidget, Ui_vtnModificarProducto):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.campos = [self.lineCodBarra, self.lineNombMed, self.lineTipoPres, self.lineImp]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.columnHeadersProd = ["Código de Barra", "Medicamento", "Presentación", "Importe"]
#         self.tablaProducto.itemClicked.connect(self.obtenerProducto)
#         self.btnBuscarProd.pressed.connect(self.buscarProductos)
#         self.lineCodBarra.returnPressed.connect(self.buscarProductos)
#         self.producto = None
#         self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
#         self.tablaMedicamento.itemClicked.connect(self.setMedicamento)
#         self.btnBuscarMed.pressed.connect(self.buscarMedicamento)
#         self.lineNombMed.returnPressed.connect(self.buscarMedicamento)
#         self.medicamento = None
#         self.columnHeadersPres = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
#         self.tablaPresentacion.itemClicked.connect(self.setPresentacion)
#         self.btnBuscarPres.pressed.connect(self.buscarPresentacion)
#         self.lineTipoPres.returnPressed.connect(self.buscarPresentacion)
#         self.presentacion = None
#
#     def buscarProductos(self):
#         cod = [self.lineCodBarra]
#         productos = {}
#         if self.validarDatos.validarCamposVacios(cod):
#             self.limpiarTabla(self.tablaProducto, self.columnHeadersProd)
#             query = Producto.buscar(Producto.codigoBarra, self.sesion, str(self.lineCodBarra.text()))
#             i = 0
#             for instance in query.all():
#                 item = [instance.codigoBarra, instance.id_medicamento, instance.id_presentacion, instance.importe]
#                 productos[i] = item
#                 i += 1
#                 self.producto = instance
#                 self.medicamento = self.producto.id_medicamento
#                 self.presentacion = self.producto.id_presentacion
#             if len(productos.items()) < 1:
#                 self.showMsjEstado("No existen Productos que coincidan con el código de barra ingresado en la busqueda.")
#             else:
#                 self.cargarCampos()
#         else:
#             self.showMsjEstado("Ingrese el código de barra del Producto para poder realizar la busqueda.")
#         self.cargarTabla(self.tablaProducto, productos, self.columnHeadersProd)
#
#     def obtenerProducto(self):
#         codBarra = self.itemSeleccionado(self.tablaProducto)
#         query = Producto.buscar(Producto.codigoBarra, self.sesion, codBarra)
#         for instance in query.all():
#             self.producto = instance
#             self.medicamento = self.producto.id_medicamento
#             self.presentacion = self.producto.id_presentacion
#             self.cargarCampos()
#
#     def cargarCampos(self):
#         self.lineCodBarra.setText(str(self.producto.codigoBarra))
#         self.lineImp.setText(str(self.producto.importe))
#         self.lineNombMed.setText(str(self.producto.id_medicamento))
#         self.lineTipoPres.setText(str(self.producto.id_presentacion))
#
#     def buscarMedicamento(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
#         medicamentos = {}
#         query = Medicamento.buscarLike(Medicamento.nombreComercial, self.sesion, str(self.lineNombMed.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
#             medicamentos[i] = item
#             i += 1
#             self.medicamento = instance.nombreComercial
#         if len(medicamentos.items()) < 1:
#             self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
#         elif len(medicamentos.items()) > 1:
#             self.medicamento = None
#         else:
#             self.lineNombMed.setText(self.medicamento)
#         self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeadersMed)
#
#     def buscarPresentacion(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
#         presentaciones = {}
#         query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipoPres.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#             self.presentacion = instance.tipo
#         if len(presentaciones.items()) < 1:
#             self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
#         elif len(presentaciones.items()) > 1:
#             self.presentacion = None
#         else:
#             self.lineTipoPres.setText(self.presentacion)
#         self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeadersPres)
#
#     def setPresentacion(self):
#         self.presentacion = self.itemSeleccionado(self.tablaPresentacion)
#         self.lineTipoPres.setText(self.presentacion)
#
#     def setMedicamento(self):
#         self.medicamento = self.itemSeleccionado(self.tablaMedicamento)
#         self.lineNombMed.setText(self.medicamento)
#
#
#     def confirmarOperacion(self):
#         if self.tablaProducto.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda de un Producto.")
#         else:
#             if self.validarDatos.validarCamposVacios(self.campos):
#                 if self.medicamento != None:
#                     if self.presentacion != None:
#                         self.producto.codigoBarra = str(self.lineCodBarra.text())
#                         self.producto.id_medicamento = self.medicamento
#                         self.producto.id_presentacion = self.presentacion
#                         self.producto.importe = str(self.lineImp.text())
#                         self.producto.modificar(self.sesion)
#                         self.showMsjEstado("Los datos del Producto fueron modificados.")
#                         self.actualizarVentana()
#                         self.medicamento = None
#                         self.producto = None
#                         self.presentacion = None
#                     else:
#                         self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación.")
#                 else:
#                     self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento.")
#             else:
#                 self.showMsjEstado("No pueden haber datos sin completar.")
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
#         self.limpiarTabla(self.tablaProducto, self.columnHeadersProd)
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
#         self.lineImp.setText("")
#         self.lineNombMed.setText("")
#         self.lineTipoPres.setText("")
#         self.lineCodBarra.setText("")
#         producto = {}
#         producto[0] = [self.producto.codigoBarra, self.producto.id_medicamento,
#                          self.producto.id_presentacion, self.producto.importe]
#         self.cargarTabla(self.tablaProducto, producto, self.columnHeadersProd)
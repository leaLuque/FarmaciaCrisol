__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnPresentacion
from validarDatos import ValidarDatos
from baseDatos import Presentacion as PresentacionModel
from baseDatos import Producto as ProductoModel
from PyQt4 import QtGui
class Presentacion(CRUDWidget, Ui_vtnPresentacion):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(PresentacionModel)
        self.subPresentacion = None
        self.superPresentacion = None
        self.subPresentacionOld = None

    def cargarFraccionables(self):
        self.cargarObjetos(self.tablaFraccionable,
            PresentacionModel.listarFraccionables(self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones")
        )

    def cargarPresentaciones(self):
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarTodos("tipo", self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion", "super_presentacion")
        )

    def crear(self):
        if ValidarDatos.validarCamposVacios(self.camposRequeridos):
            if self.validarFracciones():
                presentacion = PresentacionModel(str(self.lineTipo.text()), str(self.lineUnidad_Medida.text()),
                                str(self.spinCantidad.value()), self.subPresentacion, self.superPresentacion)
                if presentacion.guardar(self.sesion):
                    self.showMsjEstado("La Presentación fue dada de alta.")
                    if self.subPresentacion != None:
                        self.setSuperPresentacion(str(self.lineTipo.text()))
                    self.objectCreated.emit()
                    self.actualizar()
                else:
                    presentacion = PresentacionModel.buscar(PresentacionModel.tipo, self.sesion,
                                                      str(self.lineTipo.text())).first()
                    if presentacion.getBaja():
                        if presentacion.getCantidadFracciones() > 1:
                            item = self.tablaFraccionable.currentItem()
                            if item:
                                self.subPresentacion = str(self.tablaFraccionable.item(item.row(), 0).text())
                                presentacion.setBaja(False)
                                presentacion.setSubPresentacion(self.subPresentacion)
                                presentacion.modificar(self.sesion)
                                superPres = presentacion.getTipo()
                                presentacion = PresentacionModel.buscar(PresentacionModel.tipo, self.sesion,
                                                      self.subPresentacion).first()
                                presentacion.setSuperPresentacion(superPres)
                                presentacion.modificar(self.sesion)
                                self.showMsjEstado("La Presentación fue dada de alta.")
                                self.limpiarCampos()
                                self.objectCreated.emit()
                            else:
                                self.showMsjEstado("Seleccione la Presentación en la cual puede "
                                               "fraccionarse la Presentación actual.")
                        else:
                            presentacion.setBaja(False)
                            presentacion.modificar(self.sesion)
                            self.showMsjEstado("La Presentación fue dada de alta.")
                            self.limpiarCampos()
                            self.objectCreated.emit()
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'La Presentación ya existe.', 'Aceptar')
            else:
                self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
        else:
            self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    #TODO tener en cuenta si un producto figura en un remito,
    # al dar de baja la presentencion sse da de baja el producto idem para medicamento
    def eliminar(self):
        itemActual = self.tablaPresentacion.currentItem()
        if itemActual == None:
            self.showMsjEstado("No se ha seleccionado ninguna Presentación de la tabla")
        else:
            row = itemActual.row()
            tipo = str(self.tablaPresentacion.item(row, 0).text())
            if self.bajaValida(ProductoModel, ProductoModel.id_presentacion, tipo):
                self.presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo,
                                                                 self.sesion, tipo).first()
                self.presentacion.borrar(self.sesion)
                self.showMsjEstado("La Presentación ha sido eliminada")
                tipo = self.presentacion.getSubPresentacion()
                if tipo:
                    self.presentacion.setSubPresentacion(None)
                    self.presentacion.modificar(self.sesion)
                    self.presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo,
                                                                 self.sesion, tipo).first()
                    self.presentacion.setSuperPresentacion(None)
                    self.presentacion.modificar(self.sesion)
                tipo = self.presentacion.getSuperPresentacion()
                if tipo:
                    self.presentacion.setSuperPresentacion(None)
                    self.presentacion.modificar(self.sesion)
                    self.presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo,
                                                                 self.sesion, tipo).first()
                    self.presentacion.setSubPresentacion(None)
                    self.presentacion.modificar(self.sesion)
                self.tablaPresentacion.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'La Presentación no puede ser dada de baja, '
                                                          'esta asignada a 1 ó más productos', 'Aceptar')

    def modificar(self):
        presActual = self.tablaPresentacion.currentItem()
        if presActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                if self.validarFracciones():
                    row = presActual.row()
                    tipo = str(self.tablaPresentacion.item(row, 0).text())
                    self.presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo,
                                                                     self.sesion, tipo).first()
                    self.presentacion.setUnidadMedida(str(self.lineUnidad_Medida.text()))
                    self.presentacion.setCantidadFracciones(str(self.spinCantidad.value()))
                    self.presentacion.setSubPresentacion(self.subPresentacion)
                    if self.subPresentacion != None:
                        self.setSuperPresentacion(str(self.lineTipo.text()))
                    if self.subPresentacionOld != None:
                        self.subPresentacion = self.subPresentacionOld
                        self.setSuperPresentacion(None)
                    self.presentacion.modificar(self.sesion)
                    self.showMsjEstado("La Presentación fue modificada")
                    self.objectModified.emit()
                    self.actualizar()
                else:
                    self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado una Presentación de la tabla")


    def cargarCampos(self):
        #Deshabilitar los lines restantes
        self.lineTipo.setEnabled(False)
        self.spinCantidad.setEnabled(False)
        self.lineUnidad_Medida.setEnabled(False)
        #Recuperar la informacion de un item
        row = self.tablaPresentacion.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaPresentacion.columnCount()):
            infoItem.append(self.tablaPresentacion.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineTipo.setText(infoItem[0])
        self.lineUnidad_Medida.setText(infoItem[1])
        self.spinCantidad.setValue(int(infoItem[2]))

    def buscar(self):
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarLike(PresentacionModel.tipo, self.sesion,
                                         str(self.lineTipo.text())).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion", "super_presentacion")
        )

    def actualizar(self):
        self.limpiarCampos()
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarPresentaciones()

    def limpiarCampos(self):
        self.lineTipo.clear()
        self.lineTipo.setEnabled(True)
        self.spinCantidad.setValue(1)
        self.lineUnidad_Medida.clear()
        self.tablaPresentacion.setCurrentItem(None)
        self.tablaFraccionable.setCurrentItem(None)
        self.subPresentacion = None
        self.superPresentacion = None
        self.subPresentacionOld = None
        self.limpiarTabla(self.tablaFraccionable)
        self.cargarFraccionables()

    def modificarItem(self):
        self.lineTipo.setEnabled(False)
        row = self.tablaPresentacion.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaPresentacion.columnCount()):
            infoItem.append(self.tablaPresentacion.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineTipo.setText(infoItem[0])
        self.lineUnidad_Medida.setText(infoItem[1])
        self.spinCantidad.setValue(int(infoItem[2]))
        if str(infoItem[3]) == 'None':
            self.subPresentacion = None
            self.subPresentacionOld = None
        else:
            self.subPresentacion = str(infoItem[3])
            self.subPresentacionOld = str(infoItem[3])
        if str(infoItem[4]) == 'None':
            self.superPresentacion = None
            self.spinCantidad.setEnabled(True)
            self.tablaFraccionable.setEnabled(True)
        else:
            self.spinCantidad.setEnabled(False)
            self.tablaFraccionable.setEnabled(False)

    def setFraccionable(self):
        row = self.tablaFraccionable.currentItem().row()
        self.subPresentacion = str(self.tablaFraccionable.item(row, 0).text())

    def validarFracciones(self):
        if self.spinCantidad.value() > 1:
            if self.subPresentacion != None:
                return True
            else:
                return False
        else:
            if self.subPresentacion != None:
                self.setSuperPresentacion(None)
            self.subPresentacion = None
            return True

    def setSuperPresentacion(self, superPresentacion):
        presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo, self.sesion,
                                             self.subPresentacion).first()
        presentacion.setSuperPresentacion(superPresentacion)
        presentacion.modificar(self.sesion)
        self.objectModified.emit()

    @classmethod
    def create(cls, mdi):
        gui = super(Presentacion, cls).create(mdi)
        gui.groupPresentacion.hide()
        gui.btnBuscar.hide()
        gui.cargarFraccionables()
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.limpiarCampos)
        gui.tablaFraccionable.itemClicked.connect(gui.setFraccionable)
        return gui

    @classmethod
    def delete(cls, mdi):
        gui = super(Presentacion, cls).delete(mdi)
        gui.lineUnidad_Medida.setEnabled(False)
        gui.spinCantidad.setEnabled(False)
        gui.groupFraccionable.hide()
        gui.lineTipo.returnPressed.connect(gui.buscar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        gui.cargarPresentaciones()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tablaPresentacion.itemClicked.connect(gui.cargarCampos)
        return gui

    @classmethod
    def update(cls, mdi):
        gui = super(Presentacion, cls).update(mdi)
        gui.cargarPresentaciones()
        gui.cargarFraccionables()
        gui.tablaPresentacion.itemClicked.connect(gui.modificarItem)
        gui.lineTipo.returnPressed.connect(gui.buscar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tablaFraccionable.itemClicked.connect(gui.setFraccionable)
        return gui
#
# class AltaPresentacion(MdiWidget, Ui_vtnAltaPresentacion):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
#         self.campos = [self.lineTipo, self.lineUnidadMedida, self.lineCantFracc]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.tablaPresentacion.itemClicked.connect(self.setSubPresentacion)
#         self.inicializarTabla()
#         self.subPresentacion = None
#         self.superPresentacion = None
#
#     def inicializarTabla(self):
#         presentaciones = self.buscarPresentaciones()
#         self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)
#
#     def buscarPresentaciones(self):
#         presentaciones = {}
#         i = 0
#         query = Presentacion.buscarTodos(Presentacion.tipo, self.sesion)
#         for instance in query:
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#         return presentaciones
#
#     def setSubPresentacion(self):
#         self.subPresentacion = self.itemSeleccionado(self.tablaPresentacion)
#         self.superPresentacion = str(self.lineTipo.text())
#
#     def confirmarOperacion(self):
#         if self.validarDatos.validarCamposVacios(self.campos):
#             if self.validarFracciones():
#                 presentacion = Presentacion(str(self.lineTipo.text()),  str(self.lineUnidadMedida.text()),
#                                     str(self.lineCantFracc.text()), self.subPresentacion, None)
#                 if presentacion.guardar(self.sesion):
#                     self.showMsjEstado("La Presentación fue dada de alta.")
#                     self.actualizarFraccionable()
#                     self.actualizarVentana()
#                     self.subPresentacion = None
#                     self.superPresentacion = None
#                 else:
#                     self.showMsjEstado("La Presentación ya existe.")
#             else:
#                 self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
#         else:
#             self.showMsjEstado("Unos o más datos obligatorios no fueron completados.")
#
#     def validarFracciones(self):
#         if int(self.lineCantFracc.text()) > 1:
#             if self.subPresentacion != None:
#                 return True
#             else:
#                 return False
#         else:
#             self.subPresentacion = None
#             self.superPresentacion = None
#             return True
#
#     def actualizarFraccionable(self):
#         if self.superPresentacion != None:
#             tipo = self.itemSeleccionado(self.tablaPresentacion)
#             query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
#             for instance in query.all():
#                  presentacion = instance
#             presentacion.superPresentacion = self.superPresentacion
#             self.sesion.commit()
#
#     def actualizarVentana(self):
#         self.lineTipo.setText("")
#         self.lineUnidadMedida.setText("")
#         self.lineCantFracc.setText("")
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
#         self.inicializarTabla()
#
# class BajaPresentacion(MdiWidget, Ui_vtnBajaPresentacion):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
#         self.campos = [self.lineTipo]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.tablaPresentacion.itemClicked.connect(self.obtenerPresentacion)
#         self.presentacion = None
#         self.btnBuscar.pressed.connect(self.buscarPresentacion)
#         self.lineTipo.returnPressed.connect(self.buscarPresentacion)
#
#     def buscarPresentacion(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
#         presentaciones = {}
#         query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipo.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#             self.presentacion = instance
#         if len(presentaciones.items()) < 1:
#             self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
#         elif len(presentaciones.items()) > 1:
#             self.presentacion = None
#         self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)
#
#     def obtenerPresentacion(self):
#         tipo = self.itemSeleccionado(self.tablaPresentacion)
#         query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
#         for instance in query.all():
#              self.presentacion = instance
#
#     def confirmarOperacion(self):
#         if self.tablaPresentacion.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
#         else:
#             if self.presentacion == None:
#                 self.showMsjEstado("Seleccione una Presentación de la tabla.")
#             else:
#                 self.presentacion.borrar(self.sesion)
#                 self.showMsjEstado("La Presentación fue dada de baja.")
#                 self.actualizarVentana()
#                 self.monodroga = None
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
#         self.lineTipo.setText("")
#
# class ModificarPresentacion(MdiWidget, Ui_vtnModificarPresentacion):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
#         self.campos = [self.lineTipo, self.lineUnidadMedida, self.lineCantFracc]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.tablaPresentacion.itemClicked.connect(self.obtenerPresentacion)
#         self.tablaPresFracc.itemClicked.connect(self.setSubPresentacion)
#         self.presentacion = None
#         self.subPresentacion = None
#         self.btnBuscar.pressed.connect(self.buscarPresentacion)
#         self.lineTipo.returnPressed.connect(self.buscarPresentacion)
#         self.inicializarTabla()
#
#     def inicializarTabla(self):
#         presentaciones = self.buscarPresentaciones()
#         self.limpiarTabla(self.tablaPresFracc, self.columnHeaders)
#         self.cargarTabla(self.tablaPresFracc, presentaciones, self.columnHeaders)
#
#     def buscarPresentaciones(self):
#         presentaciones = {}
#         i = 0
#         query = Presentacion.buscarTodos(Presentacion.tipo, self.sesion)
#         for instance in query:
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#         return presentaciones
#
#     def buscarPresentacion(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
#         presentaciones = {}
#         query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipo.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
#             presentaciones[i] = item
#             i += 1
#             self.presentacion = instance
#             self.subPresentacion = instance.subPresentacion
#         self.limpiarCampos()
#         if len(presentaciones.items()) < 1:
#             self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
#         elif len(presentaciones.items()) > 1:
#             self.presentacion = None
#             self.subPresentacion = None
#         else:
#             self.cargarCampos()
#         self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)
#
#     def obtenerPresentacion(self):
#         tipo = self.itemSeleccionado(self.tablaPresentacion)
#         query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
#         for instance in query.all():
#             self.presentacion = instance
#             self.subPresentacion = instance.subPresentacion
#         self.cargarCampos()
#
#     def cargarCampos(self):
#         self.lineTipo.setText(self.presentacion.tipo)
#         self.lineUnidadMedida.setText(self.presentacion.unidadMedida)
#         self.lineCantFracc.setText(str(self.presentacion.cantidadFracciones))
#
#     def limpiarCampos(self):
#         self.lineTipo.setText("")
#         self.lineUnidadMedida.setText("")
#         self.lineCantFracc.setText("")
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
#         self.limpiarCampos()
#         presentacion = {}
#         presentacion[0] = [self.presentacion.tipo, self.presentacion.unidadMedida,
#                          self.presentacion.cantidadFracciones, self.presentacion.subPresentacion]
#         self.cargarTabla(self.tablaPresentacion, presentacion, self.columnHeaders)
#         self.inicializarTabla()
#
#     def setSubPresentacion(self):
#         self.subPresentacion = self.itemSeleccionado(self.tablaPresFracc)
#
#     def confirmarOperacion(self):
#         if self.tablaPresentacion.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
#         else:
#             if self.presentacion == None:
#                 self.showMsjEstado("Seleccione una Presentacion de la tabla.")
#             else:
#                 if self.validarDatos.validarCamposVacios(self.campos):
#                     if self.validarFracciones():
#                         self.presentacion.tipo = str(self.lineTipo.text())
#                         self.presentacion.unidadMedida = str(self.lineUnidadMedida.text())
#                         self.presentacion.cantidadFracciones = str(self.lineCantFracc.text())
#                         self.presentacion.subPresentacion = self.subPresentacion
#                         self.presentacion.modificar(self.sesion)
#                         self.showMsjEstado("Los datos de la Presentación fueron modificados.")
#                         self.actualizarVentana()
#                         self.presentacion = None
#                         self.subPresentacion = None
#                     else:
#                         self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
#                 else:
#                     self.showMsjEstado("No pueden haber datos sin completar.")
#
#     def validarFracciones(self):
#         if int(self.lineCantFracc.text()) > 1:
#             if self.subPresentacion != None:
#                 return True
#             else:
#                 return False
#         else:
#             self.subPresentacion = None
#             return True
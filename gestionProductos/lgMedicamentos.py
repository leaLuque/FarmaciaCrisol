__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnMedicamento
from baseDatos import Medicamento as MedicamentoModel
from baseDatos import Monodroga as MonodrogaModel
from validarDatos import ValidarDatos
from baseDatos import Producto as ProductoModel
from PyQt4 import QtGui
class Medicamento(CRUDWidget, Ui_vtnMedicamento):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(MedicamentoModel)
        self.monodroga = None

    def cargarMedicamentos(self):
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarTodos("nombre_comercial", self.sesion).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def crear(self):
        if self.monodroga == None:
            self.showMsjEstado("No se ha seleccionado ninguna Monodroga de la tabla")
        else:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                medicamento = MedicamentoModel(str(self.lineNombre_Med.text()), self.monodroga,
                                               str(self.spinCantidad.value()))
                if medicamento.guardar(self.sesion):
                    self.showMsjEstado("El Medicamento fue dado de alta.")
                    self.limpiarCampos()
                    self.objectCreated.emit()
                else:
                    medicamento = MedicamentoModel.buscar(MedicamentoModel.nombre_comercial, self.sesion,
                                                      str(self.lineNombre_Med.text())).first()
                    if medicamento.getBaja():
                        medicamento.setBaja(False)
                        medicamento.modificar(self.sesion)
                        self.showMsjEstado("El Medicamento fue dado de alta.")
                        self.limpiarCampos()
                        self.objectCreated.emit()
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'El Medicamento ya existe.', 'Aceptar')
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def eliminar(self):
        itemActual = self.tablaMedicamento.currentItem()
        if itemActual == None:
            self.showMsjEstado("No se ha seleccionado ningun Medicamento de la tabla")
        else:
            row = itemActual.row()
            nombre_comercial = str(self.tablaMedicamento.item(row, 0).text())
            if self.bajaValida(ProductoModel, ProductoModel.id_medicamento, nombre_comercial):
                self.medicamento = MedicamentoModel.buscarAlta(MedicamentoModel.nombre_comercial,
                                                               self.sesion, nombre_comercial).first()
                self.medicamento.borrar(self.sesion)
                self.showMsjEstado("El Medicamento ha sido dado de baja.")
                self.tablaMedicamento.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'El Medicamento no puede ser dado de baja, '
                                                          'esta asignado a 1 ó más productos', 'Aceptar')

    def modificar(self):
        itemActual = self.tablaMedicamento.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                row = itemActual.row()
                nombre_comercial = str(self.tablaMedicamento.item(row, 0).text())
                self.medicamento = MedicamentoModel.buscarAlta(MedicamentoModel.nombre_comercial,
                                                    self.sesion, nombre_comercial).first()
                self.medicamento.setCantidadMonodroga(str(self.spinCantidad.value()))
                self.medicamento.setIdMonodroga(self.monodroga)
                self.medicamento.modificar(self.sesion)
                self.showMsjEstado("El Medicamento fue modificado")
                self.objectModified.emit()
                self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Medicamento de la tabla")

    def cargarCampos(self):
        #Deshabilitar los lines restantes
        self.lineNombre_Med.setEnabled(False)
        self.spinCantidad.setEnabled(False)
        self.lineNombre_Mon.setEnabled(False)
        #Recuperar la informacion de un item
        row = self.tablaMedicamento.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaMedicamento.columnCount()):
            infoItem.append(self.tablaMedicamento.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineNombre_Med.setText(infoItem[0])
        self.lineNombre_Mon.setText(infoItem[1])
        self.spinCantidad.setValue(int(infoItem[2]))

    def buscarMonodroga(self):
        self.limpiarTabla(self.tablaMonodroga)
        self.cargarObjetos(self.tablaMonodroga,
            MonodrogaModel.buscarLike(MonodrogaModel.nombre, self.sesion,
                                      str(self.lineNombre_Mon.text())).all(),
            ("nombre", "tipo_venta", "descripcion")
        )

    def buscarMedicamento(self):
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarLike(MedicamentoModel.nombre_comercial, self.sesion,
                                        str(self.lineNombre_Med.text())).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def actualizar(self):
        self.limpiarCampos()
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarMedicamentos()

    def actualizarInfo(self):
        self.limpiarTabla(self.tablaMonodroga)
        self.cargarMonodrogas()

    def limpiarCampos(self):
        self.lineNombre_Med.clear()
        self.lineNombre_Med.setEnabled(True)
        self.lineNombre_Mon.clear()
        self.spinCantidad.setValue(1)
        self.tablaMonodroga.setCurrentItem(None)
        self.monodroga = None
        self.actualizarInfo()

    def modificarItem(self):
        self.lineNombre_Med.setEnabled(False)
        row = self.tablaMedicamento.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaMedicamento.columnCount()):
            infoItem.append(self.tablaMedicamento.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineNombre_Med.setText(infoItem[0])
        self.lineNombre_Mon.setText(infoItem[1])
        self.monodroga = infoItem[1]
        self.spinCantidad.setValue(int(infoItem[2]))

    def cargarMonodrogas(self):
        self.cargarObjetos(self.tablaMonodroga,
            MonodrogaModel.buscarTodos("nombre", self.sesion).all(),
            ("nombre", "tipo_venta", "descripcion")
        )

    def setMonodroga(self):
        row = self.tablaMonodroga.currentItem().row()
        self.monodroga = str(self.tablaMonodroga.item(row, 0).text())
        self.lineNombre_Mon.setText(self.monodroga)

    @classmethod
    def create(cls, mdi):
        gui = super(Medicamento, cls).create(mdi)
        gui.tablaMedicamento.hide()
        gui.btnBuscarMed.hide()
        gui.cargarMonodrogas()
        gui.lineNombre_Mon.returnPressed.connect(gui.buscarMonodroga)
        gui.btnBuscarMon.pressed.connect(gui.buscarMonodroga)
        gui.btnActualizar.pressed.connect(gui.actualizarInfo)
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.limpiarCampos)
        gui.tablaMonodroga.itemClicked.connect(gui.setMonodroga)
        return gui

    @classmethod
    def delete(cls, mdi):
        gui = super(Medicamento, cls).delete(mdi)
        gui.gbMonodroga.hide()
        gui.lineNombre_Med.returnPressed.connect(gui.buscarMedicamento)
        gui.btnBuscarMed.pressed.connect(gui.buscarMedicamento)
        gui.cargarMedicamentos()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tablaMedicamento.itemClicked.connect(gui.cargarCampos)
        return gui

    @classmethod
    def update(cls, mdi):
        gui = super(Medicamento, cls).update(mdi)
        gui.cargarMedicamentos()
        gui.cargarMonodrogas()
        gui.lineNombre_Mon.returnPressed.connect(gui.buscarMonodroga)
        gui.lineNombre_Med.returnPressed.connect(gui.buscarMedicamento)
        gui.tablaMedicamento.itemClicked.connect(gui.modificarItem)
        gui.btnActualizar.pressed.connect(gui.actualizarInfo)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.btnBuscarMon.pressed.connect(gui.buscarMonodroga)
        gui.btnBuscarMed.pressed.connect(gui.buscarMedicamento)
        gui.tablaMonodroga.itemClicked.connect(gui.setMonodroga)
        return gui

# class AltaMedicamento(MdiWidget, Ui_vtnAltaMedicamento):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.campos = [self.lineNomb, self.lineCantidad]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.columnHeaders = ["Nombre", "Tipo de Venta", "Descripción"]
#         self.tablaMonodroga.itemClicked.connect(self.obtenerMonodroga)
#         self.monodroga = None
#         self.inicializarTabla()
#         self.btnActMon.pressed.connect(self.inicializarTabla)
#
#     def inicializarTabla(self):
#         self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
#         monodrogas = {}
#         i = 0
#         query = Monodroga.buscarTodos(Monodroga.nombre, self.sesion)
#         for instance in query.all():
#             item = [instance.nombre, instance.tipoVta, instance.descripcion]
#             monodrogas[i] = item
#             i += 1
#         self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeaders)
#
#     def obtenerMonodroga(self):
#         nombre = self.itemSeleccionado(self.tablaMonodroga)
#         query = Monodroga.buscar(Monodroga.nombre, self.sesion, nombre)
#         for instance in query.all():
#             self.monodroga = instance
#
#     def confirmarOperacion(self):
#         if self.validarDatos.validarCamposVacios(self.campos):
#             if self.monodroga != None:
#                 medicamento = Medicamento(str(self.lineNomb.text()),  str(self.monodroga.nombre),
#                                     str(self.lineCantidad.text()))
#                 if medicamento.guardar(self.sesion):
#                     self.showMsjEstado("El Medicamento fue dado de alta.")
#                     self.actualizarVentana()
#                     self.monodroga = None
#                 else:
#                     self.showMsjEstado("El Medicamento ya existe.")
#             else:
#                 self.showMsjEstado("Seleccione una Monodroga de la tabla")
#         else:
#             self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
#
#     def actualizarVentana(self):
#         self.lineCantidad.setText("")
#         self.lineNomb.setText("")
#
# class BajaMedicamento(MdiWidget, Ui_vtnBajaMedicamento):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.campos = [self.lineNomb]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.columnHeaders = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
#         self.tablaMedicamento.itemClicked.connect(self.obtenerMedicamento)
#         self.btnBuscar.pressed.connect(self.buscarMedicamentos)
#         self.lineNomb.returnPressed.connect(self.buscarMedicamentos)
#         self.medicamento = None
#
#     def buscarMedicamentos(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeaders)
#         medicamentos = {}
#         query = Medicamento.buscarLike(Medicamento.nombreComercial, self.sesion, str(self.lineNomb.text()))
#         i = 0
#         for instance in query.all():
#             item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
#             medicamentos[i] = item
#             i += 1
#             self.medicamento = instance
#         if len(medicamentos.items()) < 1:
#             self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
#         elif len(medicamentos.items()) > 1:
#             self.medicamento = None
#         self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeaders)
#
#     def obtenerMedicamento(self):
#         nombre = self.itemSeleccionado(self.tablaMedicamento)
#         query = Medicamento.buscar(Medicamento.nombreComercial, self.sesion, nombre)
#         for instance in query.all():
#              self.medicamento = instance
#
#     def confirmarOperacion(self):
#         if self.tablaMedicamento.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
#         else:
#             if self.medicamento == None:
#                 self.showMsjEstado("Seleccione un Medicamento de la tabla.")
#             else:
#                 self.medicamento.borrar(self.sesion)
#                 self.showMsjEstado("El Medicamento fue dado de baja.")
#                 self.actualizarVentana()
#                 self.medicamento = None
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeaders)
#         self.lineNomb.setText("")
# 1
# class ModificarMedicamento(MdiWidget, Ui_vtnModificarMedicamento):
#     def __init__(self, mdi):
#         MdiWidget.__init__(self, mdi)
#         self.sesion = self.mdi().window().getSesionBD()
#         self.btnBuscarMon.pressed.connect(self.buscarMonodroga)
#         self.lineNombMon.returnPressed.connect(self.buscarMonodroga)
#         self.btnBuscarMed.pressed.connect(self.buscarMedicamento)
#         self.lineNombMed.returnPressed.connect(self.buscarMedicamento)
#         self.tablaMonodroga.itemClicked.connect(self.setMonodroga)
#         self.tablaMedicamento.itemClicked.connect(self.obtenerMedicamento)
#         self.campos = [self.lineNombMed, self.lineNombMon, self.lineCantidad]
#         self.validarDatos = ValidarDatos()
#         self.validarDatos.setValidator(self.campos)
#         self.columnHeadersMon = ["Nombre", "Tipo de Venta", "Descripci�n"]
#         self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
#         self.medicamento = None
#         self.monodroga = None
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
#             self.medicamento = instance
#             self.monodroga = instance.id_monodroga
#         if len(medicamentos.items()) < 1:
#             self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
#         elif len(medicamentos.items()) > 1:
#             self.medicamento = None
#             self.monodroga = None
#         else:
#             self.cargarCampos()
#         self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeadersMed)
#
#     def obtenerMedicamento(self):
#         nombre = self.itemSeleccionado(self.tablaMedicamento)
#         query = Medicamento.buscar(Medicamento.nombreComercial, self.sesion, nombre)
#         for instance in query.all():
#             self.medicamento = instance
#             self.monodroga = instance.id_monodroga
#         self.cargarCampos()
#
#     def buscarMonodroga(self):
#         self.limpiarTabla(self.tablaMonodroga, self.columnHeadersMon)
#         monodrogas = {}
#         i = 0
#         query = Monodroga.buscarLike(Monodroga.nombre, self.sesion, str(self.lineNombMon.text()))
#         for instance in query.all():
#             item = [instance.nombre, instance.tipoVta, instance.descripcion]
#             monodrogas[i] = item
#             i += 1
#             self.monodroga = instance.nombre
#         if len(monodrogas.items()) < 1:
#             self.showMsjEstado("No existen Monodrogas que coincidan con el nombre ingresado en la busqueda.")
#         elif len(monodrogas.items()) > 1:
#             self.monodroga = None
#         else:
#             self.lineNombMon.setText(self.monodroga)
#         self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeadersMon)
#
#     def setMonodroga(self):
#         self.monodroga = self.itemSeleccionado(self.tablaMonodroga)
#         self.lineNombMon.setText(self.monodroga)
#
#     def cargarCampos(self):
#         self.lineNombMed.setText(self.medicamento.nombreComercial)
#         self.lineNombMon.setText(self.medicamento.id_monodroga)
#         self.lineCantidad.setText(str(self.medicamento.cantidadMonodroga))
#
#     def limpiarCampos(self):
#         self.lineNombMon.setText("")
#         self.lineNombMed.setText("")
#         self.lineCantidad.setText("")
#
#     def confirmarOperacion(self):
#         if self.tablaMedicamento.rowCount() < 1:
#             self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
#         else:
#             if self.medicamento == None:
#                 self.showMsjEstado("Seleccione un Medicamento de la tabla.")
#             else:
#                 if self.validarDatos.validarCamposVacios(self.campos):
#                     if self.monodroga != None:
#                         self.medicamento.nombreComercial = str(self.lineNombMed.text())
#                         self.medicamento.id_monodroga = self.monodroga
#                         self.medicamento.cantidadMonodroga = str(self.lineCantidad.text())
#                         self.medicamento.modificar(self.sesion)
#                         self.showMsjEstado("Los datos del Medicamento fueron modificados.")
#                         self.actualizarVentana()
#                         self.medicamento = None
#                         self.monodroga = None
#                     else:
#                         self.showMsjEstado("Seleccione una Monodroga de la tabla.")
#                 else:
#                     self.showMsjEstado("No pueden haber datos sin completar.")
#
#     def actualizarVentana(self):
#         self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
#         self.limpiarTabla(self.tablaMonodroga, self.columnHeadersMon)
#         self.limpiarCampos()
#         medicamento = {}
#         medicamento[0] = [self.medicamento.nombreComercial, self.medicamento.id_monodroga,
#                          self.medicamento.cantidadMonodroga]
#         self.cargarTabla(self.tablaMedicamento, medicamento, self.columnHeadersMed)
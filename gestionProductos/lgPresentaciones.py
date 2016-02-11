# coding: latin-1
__author__ = 'waldo'
from PyQt4 import QtGui

from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnPresentacion
from validarDatos import ValidarDatos
from baseDatos import Presentacion as PresentacionModel
from baseDatos import Producto as ProductoModel

class Presentacion(CRUDWidget, Ui_vtnPresentacion):
    """
    Lógica del ABM de presentación.
    """
    def __init__(self, mdi):
        """
        Coonstructor de la clase Presentación.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(PresentacionModel)
        self.subPresentacion = None
        self.superPresentacion = None
        self.subPresentacionOld = None

    def cargarFraccionables(self):
        """
        Carga los datos de las presentaciones que pueden fraccionarse en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaFraccionable,
            PresentacionModel.listarFraccionables(self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones")
        )

    def cargarPresentaciones(self):
        """
        Carga los datos de las presentaciones en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaPresentacion,
            PresentacionModel.buscarTodos("tipo", self.sesion).all(),
            ("tipo", "unidad_medida", "cantidad_fracciones", "sub_presentacion", "super_presentacion")
        )

    def crear(self):
        """
        Da de alta una presentación nueva y la almacena en la base de datos.
        :return:
        """
        if ValidarDatos.validarCamposVacios(self.camposRequeridos):
            if self.validarFracciones():
                presentacion = PresentacionModel(str(self.lineTipo.text()),
                                                 str(self.lineUnidad_Medida.text()),
                                                 str(self.spinCantidad.value()),
                                                 self.subPresentacion, self.superPresentacion)
                if presentacion.guardar(self.sesion):
                    QtGui.QMessageBox.information(self, 'Info',
                                                  'La Presentación fue dada de alta.', 'Aceptar')
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
                                QtGui.QMessageBox.information(self, 'Info',
                                                              'La Presentación fue dada de alta.', 'Aceptar')
                                self.limpiarCampos()
                                self.objectCreated.emit()
                            else:
                                QtGui.QMessageBox.warning(self, 'Atención',
                                                          'Seleccione la Presentación en la cual puede'
                                                          'fraccionarse la Presentación actual.', 'Aceptar')
                        else:
                            presentacion.setBaja(False)
                            presentacion.modificar(self.sesion)
                            QtGui.QMessageBox.information(self, 'Info',
                                                          'La Presentación fue dada de alta.', 'Aceptar')
                            self.limpiarCampos()
                            self.objectCreated.emit()
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'La Presentación ya existe.', 'Aceptar')
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Seleccione la Presentación en la cual puede'
                                          'fraccionarse la Presentación actual.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                      'Aceptar')

    def eliminar(self):
        """
        Da de baja la presentación seleccionada.
        :return:
        """
        itemActual = self.tablaPresentacion.currentItem()
        if itemActual == None:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ninguna Presentación de la tabla.',
                                      'Aceptar')
        else:
            row = itemActual.row()
            tipo = str(self.tablaPresentacion.item(row, 0).text())
            if self.bajaValida(ProductoModel, ProductoModel.id_presentacion, tipo):
                self.presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo,
                                                                 self.sesion, tipo).first()
                self.presentacion.borrar(self.sesion)
                QtGui.QMessageBox.information(self, 'Info', 'La Presentación ha sido eliminada.', 'Aceptar')
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
        """
        Modifica los datos de la presentación seleccionada.
        :return:
        """
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
                    QtGui.QMessageBox.information(self, 'Info', 'La Presentación fue modificada.', 'Aceptar')
                    self.objectModified.emit()
                    self.actualizar()
                else:
                    QtGui.QMessageBox.warning(self, 'Atención', 'Seleccione la Presentación en la '
                                              'cual puede fraccionarse la Presentación actual.', 'Aceptar')
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no '
                                          'fueron completados.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado una Presentación de la tabla',
                                      'Aceptar')


    def cargarCampos(self):
        """
        Carga los campos con los datos de la presentación seleccionada.
        :return:
        """
        #Deshabilitar los lines restantes
        self.lineTipo.setEnabled(False)
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
        """
        Busca y carga en la tabla los datos de una presentación para un tipo ingresado.
        :return:
        """
        tipo = str(self.lineTipo.text())
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

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tablaPresentacion)
        self.cargarPresentaciones()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
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

    def actualizarTablaFraccionable(self,id_presentacion):
        """
            Actualiza la tabla de fraccionable
        :param id_presentacion Identificacion de presetacion:
        :return:
        """

        data = self.getAllTabla(self.tablaFraccionable)
        data_new = filter(lambda x: x[0] != id_presentacion, data.values())

        for dato in data:
            self.tablaFraccionable.setRowHidden(dato,False)

        for dato in data:
            if not data[dato] in data_new:
               self.tablaFraccionable.setRowHidden(dato,True)

    def modificarItem(self):
        """
        Carga los campos con los datos de la presentación seleccionada.
        :return:
        """
        self.lineTipo.setEnabled(False)
        row = self.tablaPresentacion.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaPresentacion.columnCount()):
            infoItem.append(self.tablaPresentacion.item(row, col).text())
        self.actualizarTablaFraccionable(infoItem[0])
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
        """
        Setea la referencia a la presentación con la presentación seleccionado.
        :return:
        """
        row = self.tablaFraccionable.currentItem().row()
        self.subPresentacion = str(self.tablaFraccionable.item(row, 0).text())

    def validarFracciones(self):
        """
        Verifica que la presentación sea fraccionable.
        :return:
        """
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
        """
        Setea la referencia a la presentación fraccionable.
        :param superPresentacion: referencia a la presentación fraccionable.
        :return:
        """
        presentacion = PresentacionModel.buscarAlta(PresentacionModel.tipo, self.sesion,
                                             self.subPresentacion).first()
        presentacion.setSuperPresentacion(superPresentacion)
        presentacion.modificar(self.sesion)
        self.objectModified.emit()

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Presentación.
        :param mdi: referencia a la ventana Alta Presentación.
        :return: gui
        """
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
        """
        Configuración de la ventana Baja Presentación.
        :param mdi: referencia a la ventana Baja Presentación.
        :return: gui
        """
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
        """
        Configuración de la ventana Modificación Presentación.
        :param mdi: referencia a la ventana Modificación Presentación.
        :return: gui
        """
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
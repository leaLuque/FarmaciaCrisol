# coding: latin-1
__author__ = 'waldo'

from PyQt4 import QtGui

from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnMonodroga
from baseDatos import Monodroga as MonodrogaModel
from baseDatos import Medicamento as MedicamentoModel
from validarDatos import ValidarDatos

class Monodroga(CRUDWidget, Ui_vtnMonodroga):
    """
    Lógica del ABM de monodrogas.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase Monodroga.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(MonodrogaModel)

    def cargarMonodrogas(self):
        """
        Carga los datos de las monodrogas en la tabla de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaMonodroga,
            MonodrogaModel.buscarTodos("nombre", self.sesion).all(),
            ("nombre", "tipo_venta", "descripcion")
        )

    def crear(self):
        """
        Da de alta una monodroga nueva y la almacena en la base de datos.
        :return:
        """
        if ValidarDatos.validarCamposVacios(self.camposRequeridos):
            monodroga = MonodrogaModel(str(self.lineNombre.text()),  str(self.cmbTipoVenta.currentText()),
                                str(self.txtDescripcion.toPlainText()))
            if monodroga.guardar(self.sesion):
                QtGui.QMessageBox.information(self, 'Info', 'La Monodroga fue dada de alta.', 'Aceptar')
                self.limpiarCampos()
                self.objectCreated.emit()
            else:
                monodroga = MonodrogaModel.buscar(MonodrogaModel.nombre, self.sesion,
                                                      str(self.lineNombre.text())).first()
                if monodroga.getBaja():
                    monodroga.setBaja(False)
                    monodroga.modificar(self.sesion)
                    QtGui.QMessageBox.information(self, 'Info', 'La Monodroga fue dada de alta.', 'Aceptar')
                    self.limpiarCampos()
                    self.objectCreated.emit()
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'La Monodroga ya existe.', 'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                      'Aceptar')

    def eliminar(self):
        """
        Da de baja la monodroga seleccionada.
        :return:
        """
        itemActual = self.tablaMonodroga.currentItem()
        if itemActual == None:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado ninguna Monodroga de la tabla.',
                                      'Aceptar')
        else:
            row = itemActual.row()
            nombre = str(self.tablaMonodroga.item(row, 0).text())
            if self.bajaValida(MedicamentoModel, MedicamentoModel.id_monodroga, nombre):
                self.monodroga = MonodrogaModel.buscarAlta(MonodrogaModel.nombre, self.sesion, nombre).first()
                self.monodroga.borrar(self.sesion)
                QtGui.QMessageBox.information(self, 'Info', 'La Monodroga ha sido dada de baja.', 'Aceptar')
                self.tablaMonodroga.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'La Monodroga no puede ser dada de baja, esta'
                                                          ' asignada a 1 ó más medicamentos', 'Aceptar')

    def modificar(self):
        """
        Modifica los datos de la monodroga seleccionada.
        :return:
        """
        itemActual = self.tablaMonodroga.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                row = itemActual.row()
                nombre = str(self.tablaMonodroga.item(row, 0).text())
                self.monodroga = MonodrogaModel.buscarAlta(MonodrogaModel.nombre, self.sesion, nombre).first()
                self.monodroga.setTipoVenta(str(self.cmbTipoVenta.currentText()))
                self.monodroga.setDescripcion(str(self.txtDescripcion.toPlainText()))
                self.monodroga.modificar(self.sesion)
                QtGui.QMessageBox.information(self, 'Info', 'La Monodroga fue modificada.', 'Aceptar')
                self.objectModified.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.warning(self, 'Atención', 'Hay datos obligatorios que no fueron completados.',
                                          'Aceptar')
        else:
            QtGui.QMessageBox.warning(self, 'Atención', 'No se ha seleccionado una Monodroga de la tabla.',
                                          'Aceptar')

    def buscar(self):
        """
        Busca y carga en la tabla los datos de una monodroga para un nombre ingresado.
        :return:
        """
        nomb = str(self.lineNombre.text())
        data = self.getAllTabla(self.tablaMonodroga)

        if nomb != "":
            dataMon = filter(lambda x: x[0].upper() == nomb.upper(), data.values())
        else:
            dataMon = data.values()

        for dato in data:
            self.tablaMonodroga.setRowHidden(dato, False)

        for dato in data:
            if not data[dato] in dataMon:
                self.tablaMonodroga.setRowHidden(dato, True)

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tablaMonodroga)
        self.cargarMonodrogas()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineNombre.clear()
        self.lineNombre.setEnabled(True)
        self.txtDescripcion.clear()
        self.tablaMonodroga.setCurrentItem(None)

    def cargarCampos(self):
        """
        Carga los campos con los datos de la monodroga seleccionada.
        :return:
        """
        self.lineNombre.setEnabled(False)
        row = self.tablaMonodroga.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaMonodroga.columnCount()):
            infoItem.append(str(self.tablaMonodroga.item(row, col).text()))
        #Cargar la info del item en los lines
        self.lineNombre.setText(infoItem[0])
        if infoItem[1] == "Libre":
            self.cmbTipoVenta.setCurrentIndex(0)
        elif infoItem[1] == "Receta":
            self.cmbTipoVenta.setCurrentIndex(1)
        else:
            self.cmbTipoVenta.setCurrentIndex(2)
        self.txtDescripcion.setText(infoItem[2])

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Monodroga.
        :param mdi: referencia a la ventana Alta Monodroga.
        :return: gui
        """
        gui = super(Monodroga, cls).create(mdi)
        gui.groupMonodroga.hide()
        gui.btnBuscar.hide()
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.cancelar)
        return gui

    @classmethod
    def delete(cls, mdi):
        """
        Configuración de la ventana Baja Monodroga.
        :param mdi: referencia a la ventana Baja Monodroga.
        :return: gui
        """
        gui = super(Monodroga, cls).delete(mdi)
        gui.txtDescripcion.setHidden(True)
        gui.cmbTipoVenta.setHidden(True)
        gui.label_tv.setHidden(True)
        gui.label_desc.setHidden(True)
        gui.lineNombre.returnPressed.connect(gui.buscar)
        gui.cargarMonodrogas()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.cancelar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        gui.tablaMonodroga.itemClicked.connect(gui.cargarCampos)
        return gui

    @classmethod
    def update(cls, mdi):
        """
        Configuración de la ventana Modificación Monodroga.
        :param mdi: referencia a la ventana Modificación Monodroga.
        :return: gui
        """
        gui = super(Monodroga, cls).update(mdi)
        gui.cargarMonodrogas()
        gui.lineNombre.returnPressed.connect(gui.buscar)
        gui.tablaMonodroga.itemClicked.connect(gui.cargarCampos)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.cancelar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        return gui

    def cancelarVentana(self):
        self.actualizar()
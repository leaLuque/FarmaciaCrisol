# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnVentaConRemito.ui'
#
# Created: Tue Jan 26 19:47:45 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vtnVentaConRemito(object):
    def setupUi(self, vtnVentaConRemito):
        vtnVentaConRemito.setObjectName(_fromUtf8("vtnVentaConRemito"))
        vtnVentaConRemito.resize(906, 731)
        self.verticalLayout = QtGui.QVBoxLayout(vtnVentaConRemito)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbCliente = QtGui.QGroupBox(vtnVentaConRemito)
        self.gbCliente.setFlat(False)
        self.gbCliente.setCheckable(False)
        self.gbCliente.setObjectName(_fromUtf8("gbCliente"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbCliente)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblNombre = QtGui.QLabel(self.gbCliente)
        self.lblNombre.setObjectName(_fromUtf8("lblNombre"))
        self.horizontalLayout_2.addWidget(self.lblNombre)
        self.lineNombre = QtGui.QLineEdit(self.gbCliente)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.horizontalLayout_2.addWidget(self.lineNombre)
        self.lblApellido = QtGui.QLabel(self.gbCliente)
        self.lblApellido.setObjectName(_fromUtf8("lblApellido"))
        self.horizontalLayout_2.addWidget(self.lblApellido)
        self.lineApellido = QtGui.QLineEdit(self.gbCliente)
        self.lineApellido.setObjectName(_fromUtf8("lineApellido"))
        self.horizontalLayout_2.addWidget(self.lineApellido)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblDni = QtGui.QLabel(self.gbCliente)
        self.lblDni.setObjectName(_fromUtf8("lblDni"))
        self.horizontalLayout_3.addWidget(self.lblDni)
        self.lineDni = QtGui.QLineEdit(self.gbCliente)
        self.lineDni.setObjectName(_fromUtf8("lineDni"))
        self.horizontalLayout_3.addWidget(self.lineDni)
        self.btnBuscarCliente = QtGui.QPushButton(self.gbCliente)
        self.btnBuscarCliente.setObjectName(_fromUtf8("btnBuscarCliente"))
        self.horizontalLayout_3.addWidget(self.btnBuscarCliente)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.tableClientes = QtGui.QTableWidget(self.gbCliente)
        self.tableClientes.setAutoFillBackground(False)
        self.tableClientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableClientes.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableClientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableClientes.setObjectName(_fromUtf8("tableClientes"))
        self.tableClientes.setColumnCount(3)
        self.tableClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(2, item)
        self.tableClientes.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_10.addWidget(self.tableClientes)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout.addWidget(self.gbCliente)
        self.gbProducto = QtGui.QGroupBox(vtnVentaConRemito)
        self.gbProducto.setObjectName(_fromUtf8("gbProducto"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbProducto)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.gbProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineMedicamento = QtGui.QLineEdit(self.gbProducto)
        self.lineMedicamento.setObjectName(_fromUtf8("lineMedicamento"))
        self.horizontalLayout_6.addWidget(self.lineMedicamento)
        self.label = QtGui.QLabel(self.gbProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.lineMonodroga = QtGui.QLineEdit(self.gbProducto)
        self.lineMonodroga.setObjectName(_fromUtf8("lineMonodroga"))
        self.horizontalLayout_6.addWidget(self.lineMonodroga)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.tableProductos = QtGui.QTableWidget(self.gbProducto)
        self.tableProductos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableProductos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableProductos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableProductos.setObjectName(_fromUtf8("tableProductos"))
        self.tableProductos.setColumnCount(6)
        self.tableProductos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(5, item)
        self.tableProductos.horizontalHeader().setDefaultSectionSize(120)
        self.tableProductos.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_7.addWidget(self.tableProductos, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnActualizar = QtGui.QPushButton(self.gbProducto)
        self.btnActualizar.setObjectName(_fromUtf8("btnActualizar"))
        self.horizontalLayout_4.addWidget(self.btnActualizar)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.verticalLayout.addWidget(self.gbProducto)
        self.gbRemito = QtGui.QGroupBox(vtnVentaConRemito)
        self.gbRemito.setObjectName(_fromUtf8("gbRemito"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.gbRemito)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableRemito = QtGui.QTableWidget(self.gbRemito)
        self.tableRemito.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableRemito.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableRemito.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableRemito.setObjectName(_fromUtf8("tableRemito"))
        self.tableRemito.setColumnCount(3)
        self.tableRemito.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableRemito.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableRemito.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableRemito.setHorizontalHeaderItem(2, item)
        self.tableRemito.horizontalHeader().setDefaultSectionSize(120)
        self.tableRemito.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableRemito, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnEliminar = QtGui.QPushButton(self.gbRemito)
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.horizontalLayout.addWidget(self.btnEliminar)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.gbRemito)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btnAceptar = QtGui.QPushButton(vtnVentaConRemito)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnVentaConRemito)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_5.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(vtnVentaConRemito)
        QtCore.QMetaObject.connectSlotsByName(vtnVentaConRemito)
        vtnVentaConRemito.setTabOrder(self.lineNombre, self.lineApellido)
        vtnVentaConRemito.setTabOrder(self.lineApellido, self.lineDni)
        vtnVentaConRemito.setTabOrder(self.lineDni, self.btnBuscarCliente)
        vtnVentaConRemito.setTabOrder(self.btnBuscarCliente, self.tableClientes)
        vtnVentaConRemito.setTabOrder(self.tableClientes, self.lineMedicamento)
        vtnVentaConRemito.setTabOrder(self.lineMedicamento, self.lineMonodroga)
        vtnVentaConRemito.setTabOrder(self.lineMonodroga, self.tableProductos)
        vtnVentaConRemito.setTabOrder(self.tableProductos, self.btnActualizar)
        vtnVentaConRemito.setTabOrder(self.btnActualizar, self.tableRemito)
        vtnVentaConRemito.setTabOrder(self.tableRemito, self.btnEliminar)
        vtnVentaConRemito.setTabOrder(self.btnEliminar, self.btnAceptar)
        vtnVentaConRemito.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnVentaConRemito):
        vtnVentaConRemito.setWindowTitle(_translate("vtnVentaConRemito", "Venta con Remito", None))
        self.gbCliente.setTitle(_translate("vtnVentaConRemito", "Cliente", None))
        self.lblNombre.setText(_translate("vtnVentaConRemito", "Nombre", None))
        self.lineNombre.setStatusTip(_translate("vtnVentaConRemito", "Ingrese Nombre del cliente (solo letras)", None))
        self.lineNombre.setAccessibleDescription(_translate("vtnVentaConRemito", "nya", None))
        self.lblApellido.setText(_translate("vtnVentaConRemito", "Apellido", None))
        self.lineApellido.setStatusTip(_translate("vtnVentaConRemito", "Ingrese Apellido del cliente (solo letras)", None))
        self.lineApellido.setAccessibleDescription(_translate("vtnVentaConRemito", "nya", None))
        self.lblDni.setText(_translate("vtnVentaConRemito", "DNI", None))
        self.lineDni.setStatusTip(_translate("vtnVentaConRemito", "Ingrese DNI del cliente (exactamente 8 números)", None))
        self.lineDni.setAccessibleDescription(_translate("vtnVentaConRemito", "dni", None))
        self.btnBuscarCliente.setText(_translate("vtnVentaConRemito", "Buscar", None))
        self.tableClientes.setSortingEnabled(False)
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaConRemito", "Dni", None))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaConRemito", "Nombre", None))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaConRemito", "Apellido", None))
        self.gbProducto.setTitle(_translate("vtnVentaConRemito", "Producto", None))
        self.label_2.setText(_translate("vtnVentaConRemito", "Medicamento", None))
        self.lineMedicamento.setStatusTip(_translate("vtnVentaConRemito", "Ingrese nombre del medicamento (solo letras y números)", None))
        self.lineMedicamento.setAccessibleDescription(_translate("vtnVentaConRemito", "fMedicamento", None))
        self.label.setText(_translate("vtnVentaConRemito", "Monodroga", None))
        self.lineMonodroga.setStatusTip(_translate("vtnVentaConRemito", "Ingrese nombre de la monodroga", None))
        self.lineMonodroga.setAccessibleDescription(_translate("vtnVentaConRemito", "fmonodroga", None))
        item = self.tableProductos.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaConRemito", "Codigo", None))
        item = self.tableProductos.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaConRemito", "Medicamento", None))
        item = self.tableProductos.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaConRemito", "Presentacion", None))
        item = self.tableProductos.horizontalHeaderItem(3)
        item.setText(_translate("vtnVentaConRemito", "Monodroga", None))
        item = self.tableProductos.horizontalHeaderItem(4)
        item.setText(_translate("vtnVentaConRemito", "Cantidad", None))
        item = self.tableProductos.horizontalHeaderItem(5)
        item.setText(_translate("vtnVentaConRemito", "Importe", None))
        self.btnActualizar.setText(_translate("vtnVentaConRemito", "Actualizar", None))
        self.gbRemito.setTitle(_translate("vtnVentaConRemito", "Remito", None))
        item = self.tableRemito.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaConRemito", "Codigo", None))
        item = self.tableRemito.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaConRemito", "Cantidad", None))
        item = self.tableRemito.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaConRemito", "Importe", None))
        self.btnEliminar.setText(_translate("vtnVentaConRemito", "Eliminar", None))
        self.btnAceptar.setText(_translate("vtnVentaConRemito", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnVentaConRemito", "Cancelar", None))


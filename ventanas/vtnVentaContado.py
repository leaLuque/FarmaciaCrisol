# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnVentaContado.ui'
#
# Created: Tue Feb  9 15:41:24 2016
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

class Ui_vtnVentaContado(object):
    def setupUi(self, vtnVentaContado):
        vtnVentaContado.setObjectName(_fromUtf8("vtnVentaContado"))
        vtnVentaContado.resize(831, 678)
        self.verticalLayout = QtGui.QVBoxLayout(vtnVentaContado)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbObraSocial = QtGui.QGroupBox(vtnVentaContado)
        self.gbObraSocial.setObjectName(_fromUtf8("gbObraSocial"))
        self.formLayout = QtGui.QFormLayout(self.gbObraSocial)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.rbtnObra = QtGui.QRadioButton(self.gbObraSocial)
        self.rbtnObra.setChecked(False)
        self.rbtnObra.setObjectName(_fromUtf8("rbtnObra"))
        self.horizontalLayout_3.addWidget(self.rbtnObra)
        self.lineObra = QtGui.QLineEdit(self.gbObraSocial)
        self.lineObra.setObjectName(_fromUtf8("lineObra"))
        self.horizontalLayout_3.addWidget(self.lineObra)
        self.label_2 = QtGui.QLabel(self.gbObraSocial)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineCuit = QtGui.QLineEdit(self.gbObraSocial)
        self.lineCuit.setObjectName(_fromUtf8("lineCuit"))
        self.horizontalLayout_3.addWidget(self.lineCuit)
        self.btnBuscar = QtGui.QPushButton(self.gbObraSocial)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout_3.addWidget(self.btnBuscar)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.tableObra = QtGui.QTableWidget(self.gbObraSocial)
        self.tableObra.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableObra.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableObra.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableObra.setObjectName(_fromUtf8("tableObra"))
        self.tableObra.setColumnCount(3)
        self.tableObra.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableObra.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableObra.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableObra.setHorizontalHeaderItem(2, item)
        self.tableObra.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.tableObra)
        self.verticalLayout.addWidget(self.gbObraSocial)
        self.gbProducto = QtGui.QGroupBox(vtnVentaContado)
        self.gbProducto.setObjectName(_fromUtf8("gbProducto"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbProducto)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gbProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineMedicamento = QtGui.QLineEdit(self.gbProducto)
        self.lineMedicamento.setObjectName(_fromUtf8("lineMedicamento"))
        self.horizontalLayout.addWidget(self.lineMedicamento)
        self.label_3 = QtGui.QLabel(self.gbProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineMonodroga = QtGui.QLineEdit(self.gbProducto)
        self.lineMonodroga.setObjectName(_fromUtf8("lineMonodroga"))
        self.horizontalLayout.addWidget(self.lineMonodroga)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableProductos = QtGui.QTableWidget(self.gbProducto)
        self.tableProductos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableProductos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableProductos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableProductos.setObjectName(_fromUtf8("tableProductos"))
        self.tableProductos.setColumnCount(7)
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
        item = QtGui.QTableWidgetItem()
        self.tableProductos.setHorizontalHeaderItem(6, item)
        self.tableProductos.horizontalHeader().setDefaultSectionSize(120)
        self.tableProductos.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableProductos, 0, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbProducto)
        self.gbFactura = QtGui.QGroupBox(vtnVentaContado)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.gbFactura)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableFactura = QtGui.QTableWidget(self.gbFactura)
        self.tableFactura.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableFactura.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableFactura.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableFactura.setObjectName(_fromUtf8("tableFactura"))
        self.tableFactura.setColumnCount(3)
        self.tableFactura.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(2, item)
        self.tableFactura.horizontalHeader().setDefaultSectionSize(120)
        self.tableFactura.horizontalHeader().setMinimumSectionSize(80)
        self.tableFactura.horizontalHeader().setSortIndicatorShown(False)
        self.tableFactura.horizontalHeader().setStretchLastSection(True)
        self.tableFactura.verticalHeader().setCascadingSectionResizes(False)
        self.tableFactura.verticalHeader().setSortIndicatorShown(False)
        self.tableFactura.verticalHeader().setStretchLastSection(False)
        self.gridLayout_6.addWidget(self.tableFactura, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.btnEliminar = QtGui.QPushButton(self.gbFactura)
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.gridLayout_6.addWidget(self.btnEliminar, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.verticalLayout.addWidget(self.gbFactura)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(vtnVentaContado)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_2.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnVentaContado)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_2.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(vtnVentaContado)
        QtCore.QMetaObject.connectSlotsByName(vtnVentaContado)

    def retranslateUi(self, vtnVentaContado):
        vtnVentaContado.setWindowTitle(_translate("vtnVentaContado", "Venta Contado", None))
        self.gbObraSocial.setTitle(_translate("vtnVentaContado", "Obra Social", None))
        self.rbtnObra.setText(_translate("vtnVentaContado", "Razón Social", None))
        self.label_2.setText(_translate("vtnVentaContado", "CUIT", None))
        self.btnBuscar.setText(_translate("vtnVentaContado", "Buscar", None))
        item = self.tableObra.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaContado", "Razón Social", None))
        item = self.tableObra.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaContado", "CUIT", None))
        item = self.tableObra.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaContado", "Direccion", None))
        self.gbProducto.setTitle(_translate("vtnVentaContado", "Producto", None))
        self.label.setText(_translate("vtnVentaContado", "Medicamento", None))
        self.lineMedicamento.setStatusTip(_translate("vtnVentaContado", "Ingrese nombre del medicamento (solo letras y números)", None))
        self.lineMedicamento.setAccessibleDescription(_translate("vtnVentaContado", "fmedicamento", None))
        self.label_3.setText(_translate("vtnVentaContado", "Monodroga", None))
        self.lineMonodroga.setStatusTip(_translate("vtnVentaContado", "Ingrese nombre de la monodroga", None))
        self.lineMonodroga.setAccessibleDescription(_translate("vtnVentaContado", "fmonodroga", None))
        item = self.tableProductos.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaContado", "Codigo de Barra", None))
        item = self.tableProductos.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaContado", "Medicamento", None))
        item = self.tableProductos.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaContado", "Presentación", None))
        item = self.tableProductos.horizontalHeaderItem(3)
        item.setText(_translate("vtnVentaContado", "Monodroga", None))
        item = self.tableProductos.horizontalHeaderItem(4)
        item.setText(_translate("vtnVentaContado", "Descuento OS", None))
        item = self.tableProductos.horizontalHeaderItem(5)
        item.setText(_translate("vtnVentaContado", "Importe", None))
        item = self.tableProductos.horizontalHeaderItem(6)
        item.setText(_translate("vtnVentaContado", "Cantidad", None))
        self.gbFactura.setTitle(_translate("vtnVentaContado", "Factura", None))
        item = self.tableFactura.horizontalHeaderItem(0)
        item.setText(_translate("vtnVentaContado", "Código de Barra", None))
        item = self.tableFactura.horizontalHeaderItem(1)
        item.setText(_translate("vtnVentaContado", "Cantidad", None))
        item = self.tableFactura.horizontalHeaderItem(2)
        item.setText(_translate("vtnVentaContado", "Importe", None))
        self.btnEliminar.setText(_translate("vtnVentaContado", "Eliminar", None))
        self.btnAceptar.setText(_translate("vtnVentaContado", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnVentaContado", "Cancelar", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnRegistrarCobroRemito.ui'
#
# Created: Tue Jan 26 20:09:44 2016
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

class Ui_vtnRegistrarCobroRemito(object):
    def setupUi(self, vtnRegistrarCobroRemito):
        vtnRegistrarCobroRemito.setObjectName(_fromUtf8("vtnRegistrarCobroRemito"))
        vtnRegistrarCobroRemito.resize(653, 717)
        self.formLayout = QtGui.QFormLayout(vtnRegistrarCobroRemito)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gbObraSocial = QtGui.QGroupBox(vtnRegistrarCobroRemito)
        self.gbObraSocial.setObjectName(_fromUtf8("gbObraSocial"))
        self.formLayout_2 = QtGui.QFormLayout(self.gbObraSocial)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbtnRazonSocial = QtGui.QRadioButton(self.gbObraSocial)
        self.rbtnRazonSocial.setObjectName(_fromUtf8("rbtnRazonSocial"))
        self.horizontalLayout.addWidget(self.rbtnRazonSocial)
        self.lineRazonSocial = QtGui.QLineEdit(self.gbObraSocial)
        self.lineRazonSocial.setObjectName(_fromUtf8("lineRazonSocial"))
        self.horizontalLayout.addWidget(self.lineRazonSocial)
        self.btnBuscarOs = QtGui.QPushButton(self.gbObraSocial)
        self.btnBuscarOs.setObjectName(_fromUtf8("btnBuscarOs"))
        self.horizontalLayout.addWidget(self.btnBuscarOs)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.tableObras = QtGui.QTableWidget(self.gbObraSocial)
        self.tableObras.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableObras.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableObras.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableObras.setObjectName(_fromUtf8("tableObras"))
        self.tableObras.setColumnCount(3)
        self.tableObras.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableObras.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableObras.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableObras.setHorizontalHeaderItem(2, item)
        self.tableObras.horizontalHeader().setStretchLastSection(True)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.tableObras)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.gbObraSocial)
        self.gbRemitos = QtGui.QGroupBox(vtnRegistrarCobroRemito)
        self.gbRemitos.setObjectName(_fromUtf8("gbRemitos"))
        self.formLayout_3 = QtGui.QFormLayout(self.gbRemitos)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.gbRemitos)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineNumero = QtGui.QLineEdit(self.gbRemitos)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.horizontalLayout_2.addWidget(self.lineNumero)
        self.btnBuscarRemito = QtGui.QPushButton(self.gbRemitos)
        self.btnBuscarRemito.setObjectName(_fromUtf8("btnBuscarRemito"))
        self.horizontalLayout_2.addWidget(self.btnBuscarRemito)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.tableRemitos = QtGui.QTableWidget(self.gbRemitos)
        self.tableRemitos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableRemitos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableRemitos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableRemitos.setObjectName(_fromUtf8("tableRemitos"))
        self.tableRemitos.setColumnCount(3)
        self.tableRemitos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableRemitos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableRemitos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableRemitos.setHorizontalHeaderItem(2, item)
        self.tableRemitos.horizontalHeader().setStretchLastSection(True)
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.tableRemitos)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnAgregar = QtGui.QPushButton(self.gbRemitos)
        self.btnAgregar.setObjectName(_fromUtf8("btnAgregar"))
        self.horizontalLayout_3.addWidget(self.btnAgregar)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.gbRemitos)
        self.gbFactura = QtGui.QGroupBox(vtnRegistrarCobroRemito)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.formLayout_4 = QtGui.QFormLayout(self.gbFactura)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.tableFactura = QtGui.QTableWidget(self.gbFactura)
        self.tableFactura.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableFactura.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableFactura.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableFactura.setObjectName(_fromUtf8("tableFactura"))
        self.tableFactura.setColumnCount(4)
        self.tableFactura.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(3, item)
        self.tableFactura.horizontalHeader().setStretchLastSection(True)
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.SpanningRole, self.tableFactura)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lblImporteTotal = QtGui.QLabel(self.gbFactura)
        self.lblImporteTotal.setObjectName(_fromUtf8("lblImporteTotal"))
        self.horizontalLayout_5.addWidget(self.lblImporteTotal)
        self.formLayout_4.setLayout(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_5)
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.gbFactura)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnAceptar = QtGui.QPushButton(vtnRegistrarCobroRemito)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_4.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnRegistrarCobroRemito)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        self.formLayout.setLayout(5, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_4)

        self.retranslateUi(vtnRegistrarCobroRemito)
        QtCore.QMetaObject.connectSlotsByName(vtnRegistrarCobroRemito)

    def retranslateUi(self, vtnRegistrarCobroRemito):
        vtnRegistrarCobroRemito.setWindowTitle(_translate("vtnRegistrarCobroRemito", "Registrar Cobro Remito", None))
        self.gbObraSocial.setTitle(_translate("vtnRegistrarCobroRemito", "Obra Social", None))
        self.rbtnRazonSocial.setText(_translate("vtnRegistrarCobroRemito", "Razón Social", None))
        self.lineRazonSocial.setAccessibleDescription(_translate("vtnRegistrarCobroRemito", "frazonsocial", None))
        self.btnBuscarOs.setText(_translate("vtnRegistrarCobroRemito", "Buscar", None))
        item = self.tableObras.horizontalHeaderItem(0)
        item.setText(_translate("vtnRegistrarCobroRemito", "Razón Social", None))
        item = self.tableObras.horizontalHeaderItem(1)
        item.setText(_translate("vtnRegistrarCobroRemito", "CUIT", None))
        item = self.tableObras.horizontalHeaderItem(2)
        item.setText(_translate("vtnRegistrarCobroRemito", "Dirección", None))
        self.gbRemitos.setTitle(_translate("vtnRegistrarCobroRemito", "Remito", None))
        self.label.setText(_translate("vtnRegistrarCobroRemito", "Numero", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnRegistrarCobroRemito", "fnroremito", None))
        self.btnBuscarRemito.setText(_translate("vtnRegistrarCobroRemito", "Buscar", None))
        item = self.tableRemitos.horizontalHeaderItem(0)
        item.setText(_translate("vtnRegistrarCobroRemito", "Producto", None))
        item = self.tableRemitos.horizontalHeaderItem(1)
        item.setText(_translate("vtnRegistrarCobroRemito", "Cantidad", None))
        item = self.tableRemitos.horizontalHeaderItem(2)
        item.setText(_translate("vtnRegistrarCobroRemito", "Subtotal", None))
        self.btnAgregar.setText(_translate("vtnRegistrarCobroRemito", "Agregar", None))
        self.gbFactura.setTitle(_translate("vtnRegistrarCobroRemito", "Factura", None))
        item = self.tableFactura.horizontalHeaderItem(0)
        item.setText(_translate("vtnRegistrarCobroRemito", "Codigo", None))
        item = self.tableFactura.horizontalHeaderItem(1)
        item.setText(_translate("vtnRegistrarCobroRemito", "Cantidad", None))
        item = self.tableFactura.horizontalHeaderItem(2)
        item.setText(_translate("vtnRegistrarCobroRemito", "Subtotal", None))
        item = self.tableFactura.horizontalHeaderItem(3)
        item.setText(_translate("vtnRegistrarCobroRemito", "Descuento OS", None))
        self.lblImporteTotal.setText(_translate("vtnRegistrarCobroRemito", "Importe Total: $0,00", None))
        self.btnAceptar.setText(_translate("vtnRegistrarCobroRemito", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnRegistrarCobroRemito", "Cancelar", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnDevolucionDeCliente.ui'
#
# Created: Wed Jan 27 12:23:34 2016
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

class Ui_vtnDevolucionDeCliente(object):
    def setupUi(self, vtnDevolucionDeCliente):
        vtnDevolucionDeCliente.setObjectName(_fromUtf8("vtnDevolucionDeCliente"))
        vtnDevolucionDeCliente.resize(640, 480)
        self.formLayout = QtGui.QFormLayout(vtnDevolucionDeCliente)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gbFactura = QtGui.QGroupBox(vtnDevolucionDeCliente)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.formLayout_3 = QtGui.QFormLayout(self.gbFactura)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineNumero = QtGui.QLineEdit(self.gbFactura)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.gridLayout_2.addWidget(self.lineNumero, 0, 1, 1, 1)
        self.btnBuscar = QtGui.QPushButton(self.gbFactura)
        self.btnBuscar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout_2.addWidget(self.btnBuscar, 0, 2, 1, 1)
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
        self.tableFactura.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableFactura, 1, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.gbFactura)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.SpanningRole, self.gridLayout_2)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.gbFactura)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(vtnDevolucionDeCliente)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnDevolucionDeCliente)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.formLayout.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.gbNotaCredito = QtGui.QGroupBox(vtnDevolucionDeCliente)
        self.gbNotaCredito.setObjectName(_fromUtf8("gbNotaCredito"))
        self.formLayout_2 = QtGui.QFormLayout(self.gbNotaCredito)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.tableNC = QtGui.QTableWidget(self.gbNotaCredito)
        self.tableNC.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableNC.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableNC.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableNC.setObjectName(_fromUtf8("tableNC"))
        self.tableNC.setColumnCount(3)
        self.tableNC.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableNC.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableNC.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableNC.setHorizontalHeaderItem(2, item)
        self.tableNC.horizontalHeader().setStretchLastSection(True)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.tableNC)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.gbNotaCredito)

        self.retranslateUi(vtnDevolucionDeCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnDevolucionDeCliente)

    def retranslateUi(self, vtnDevolucionDeCliente):
        vtnDevolucionDeCliente.setWindowTitle(_translate("vtnDevolucionDeCliente", "Devolución de Cliente", None))
        self.gbFactura.setTitle(_translate("vtnDevolucionDeCliente", "Factura", None))
        self.lineNumero.setStatusTip(_translate("vtnDevolucionDeCliente", "Ingrese número de factura", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnDevolucionDeCliente", "fnroremito", None))
        self.btnBuscar.setText(_translate("vtnDevolucionDeCliente", "Buscar", None))
        item = self.tableFactura.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Código Barra", None))
        item = self.tableFactura.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableFactura.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))
        self.label_2.setText(_translate("vtnDevolucionDeCliente", "Número", None))
        self.btnAceptar.setText(_translate("vtnDevolucionDeCliente", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnDevolucionDeCliente", "Cancelar", None))
        self.gbNotaCredito.setTitle(_translate("vtnDevolucionDeCliente", "Nota de Crédito", None))
        item = self.tableNC.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Codigo Barra", None))
        item = self.tableNC.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableNC.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))


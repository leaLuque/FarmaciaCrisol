# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnReintegroCliente.ui'
#
# Created: Thu Feb 11 12:39:15 2016
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

class Ui_vtnReintegroCliente(object):
    def setupUi(self, vtnReintegroCliente):
        vtnReintegroCliente.setObjectName(_fromUtf8("vtnReintegroCliente"))
        vtnReintegroCliente.resize(640, 512)
        self.verticalLayout = QtGui.QVBoxLayout(vtnReintegroCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbObraSocial = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbObraSocial.setObjectName(_fromUtf8("gbObraSocial"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbObraSocial)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineRazon = QtGui.QLineEdit(self.gbObraSocial)
        self.lineRazon.setObjectName(_fromUtf8("lineRazon"))
        self.gridLayout_2.addWidget(self.lineRazon, 0, 1, 1, 1)
        self.btnBuscarOs = QtGui.QPushButton(self.gbObraSocial)
        self.btnBuscarOs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarOs.setObjectName(_fromUtf8("btnBuscarOs"))
        self.gridLayout_2.addWidget(self.btnBuscarOs, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gbObraSocial)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gbObraSocial)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineCuit = QtGui.QLineEdit(self.gbObraSocial)
        self.lineCuit.setObjectName(_fromUtf8("lineCuit"))
        self.gridLayout_2.addWidget(self.lineCuit, 1, 1, 1, 1)
        self.tableOs = QtGui.QTableWidget(self.gbObraSocial)
        self.tableOs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableOs.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableOs.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableOs.setObjectName(_fromUtf8("tableOs"))
        self.tableOs.setColumnCount(3)
        self.tableOs.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableOs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableOs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableOs.setHorizontalHeaderItem(2, item)
        self.tableOs.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableOs, 2, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbObraSocial)
        self.gbFactura = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbFactura)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineNumeroFac = QtGui.QLineEdit(self.gbFactura)
        self.lineNumeroFac.setObjectName(_fromUtf8("lineNumeroFac"))
        self.gridLayout_3.addWidget(self.lineNumeroFac, 0, 1, 1, 1)
        self.btnBuscarFac = QtGui.QPushButton(self.gbFactura)
        self.btnBuscarFac.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarFac.setObjectName(_fromUtf8("btnBuscarFac"))
        self.gridLayout_3.addWidget(self.btnBuscarFac, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gbFactura)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.tableFactura, 1, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbFactura)
        self.gbNotaCredito = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbNotaCredito.setObjectName(_fromUtf8("gbNotaCredito"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gbNotaCredito)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
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
        self.gridLayout_4.addWidget(self.tableNC, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.gbNotaCredito)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(vtnReintegroCliente)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnReintegroCliente)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(vtnReintegroCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnReintegroCliente)

    def retranslateUi(self, vtnReintegroCliente):
        vtnReintegroCliente.setWindowTitle(_translate("vtnReintegroCliente", "Reintegro Cliente", None))
        self.gbObraSocial.setTitle(_translate("vtnReintegroCliente", "Obra Social", None))
        self.lineRazon.setStatusTip(_translate("vtnReintegroCliente", "Ingrese nombre de Obra Social", None))
        self.lineRazon.setAccessibleDescription(_translate("vtnReintegroCliente", "frazonsocial", None))
        self.btnBuscarOs.setText(_translate("vtnReintegroCliente", "Buscar", None))
        self.label_2.setText(_translate("vtnReintegroCliente", "CUIT", None))
        self.label_3.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        self.lineCuit.setStatusTip(_translate("vtnReintegroCliente", "Ingrese CUIT de la Obra Social", None))
        self.lineCuit.setAccessibleDescription(_translate("vtnReintegroCliente", "fcuit", None))
        item = self.tableOs.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        item = self.tableOs.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "CUIT", None))
        item = self.tableOs.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Dirección", None))
        self.gbFactura.setTitle(_translate("vtnReintegroCliente", "Factura", None))
        self.lineNumeroFac.setStatusTip(_translate("vtnReintegroCliente", "Ingrese número de factura", None))
        self.lineNumeroFac.setAccessibleDescription(_translate("vtnReintegroCliente", "fnroremito", None))
        self.btnBuscarFac.setText(_translate("vtnReintegroCliente", "Buscar", None))
        self.label_4.setText(_translate("vtnReintegroCliente", "Número", None))
        item = self.tableFactura.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableFactura.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableFactura.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))
        self.gbNotaCredito.setTitle(_translate("vtnReintegroCliente", "Nota de Crédito", None))
        item = self.tableNC.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableNC.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableNC.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))
        self.btnAceptar.setText(_translate("vtnReintegroCliente", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnReintegroCliente", "Cancelar", None))


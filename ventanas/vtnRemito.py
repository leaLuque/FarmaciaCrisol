# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnRemito.ui'
#
# Created: Tue Jan 26 20:22:03 2016
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

class Ui_vtnRemito(object):
    def setupUi(self, vtnRemito):
        vtnRemito.setObjectName(_fromUtf8("vtnRemito"))
        vtnRemito.resize(692, 525)
        self.formLayout = QtGui.QFormLayout(vtnRemito)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(vtnRemito)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineNumero = QtGui.QLineEdit(vtnRemito)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.horizontalLayout.addWidget(self.lineNumero)
        self.btnBuscar = QtGui.QPushButton(vtnRemito)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.tableRemito = QtGui.QTableWidget(vtnRemito)
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
        self.tableRemito.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.tableRemito)
        self.line = QtGui.QFrame(vtnRemito)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.line)
        self.tableDetalles = QtGui.QTableWidget(vtnRemito)
        self.tableDetalles.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableDetalles.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableDetalles.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableDetalles.setObjectName(_fromUtf8("tableDetalles"))
        self.tableDetalles.setColumnCount(4)
        self.tableDetalles.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableDetalles.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableDetalles.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableDetalles.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableDetalles.setHorizontalHeaderItem(3, item)
        self.tableDetalles.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.tableDetalles)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnActualizar = QtGui.QPushButton(vtnRemito)
        self.btnActualizar.setObjectName(_fromUtf8("btnActualizar"))
        self.horizontalLayout_2.addWidget(self.btnActualizar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(vtnRemito)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_2.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnRemito)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_2.addWidget(self.btnCancelar)
        self.formLayout.setLayout(11, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblDetalles = QtGui.QLabel(vtnRemito)
        self.lblDetalles.setObjectName(_fromUtf8("lblDetalles"))
        self.horizontalLayout_3.addWidget(self.lblDetalles)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(8, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(vtnRemito)
        QtCore.QMetaObject.connectSlotsByName(vtnRemito)

    def retranslateUi(self, vtnRemito):
        self.label.setText(_translate("vtnRemito", "Numero", None))
        self.lineNumero.setStatusTip(_translate("vtnRemito", "Ingrese número de remito", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnRemito", "fnroremito", None))
        self.btnBuscar.setText(_translate("vtnRemito", "Buscar", None))
        item = self.tableRemito.horizontalHeaderItem(0)
        item.setText(_translate("vtnRemito", "Numero", None))
        item = self.tableRemito.horizontalHeaderItem(1)
        item.setText(_translate("vtnRemito", "DNI Cliente", None))
        item = self.tableRemito.horizontalHeaderItem(2)
        item.setText(_translate("vtnRemito", "Fecha Emision", None))
        item = self.tableDetalles.horizontalHeaderItem(0)
        item.setText(_translate("vtnRemito", "Linea", None))
        item = self.tableDetalles.horizontalHeaderItem(1)
        item.setText(_translate("vtnRemito", "Producto", None))
        item = self.tableDetalles.horizontalHeaderItem(2)
        item.setText(_translate("vtnRemito", "Cantidad", None))
        item = self.tableDetalles.horizontalHeaderItem(3)
        item.setText(_translate("vtnRemito", "Subtotal", None))
        self.btnActualizar.setText(_translate("vtnRemito", "Actualizar", None))
        self.btnAceptar.setText(_translate("vtnRemito", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnRemito", "Cancelar", None))
        self.lblDetalles.setText(_translate("vtnRemito", "Detalles de Remito", None))


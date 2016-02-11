# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnTiposCobro.ui'
#
# Created: Thu Feb 11 12:39:24 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(631, 380)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbtnTC = QtGui.QRadioButton(Dialog)
        self.rbtnTC.setObjectName(_fromUtf8("rbtnTC"))
        self.horizontalLayout.addWidget(self.rbtnTC)
        self.rbtnTD = QtGui.QRadioButton(Dialog)
        self.rbtnTD.setObjectName(_fromUtf8("rbtnTD"))
        self.horizontalLayout.addWidget(self.rbtnTD)
        self.rbtnNC = QtGui.QRadioButton(Dialog)
        self.rbtnNC.setCheckable(True)
        self.rbtnNC.setChecked(False)
        self.rbtnNC.setObjectName(_fromUtf8("rbtnNC"))
        self.horizontalLayout.addWidget(self.rbtnNC)
        self.rbtnEfectivo = QtGui.QRadioButton(Dialog)
        self.rbtnEfectivo.setCheckable(True)
        self.rbtnEfectivo.setChecked(False)
        self.rbtnEfectivo.setObjectName(_fromUtf8("rbtnEfectivo"))
        self.horizontalLayout.addWidget(self.rbtnEfectivo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblImporte = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblImporte.setFont(font)
        self.lblImporte.setObjectName(_fromUtf8("lblImporte"))
        self.horizontalLayout_3.addWidget(self.lblImporte)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tablePagos = QtGui.QTableWidget(Dialog)
        self.tablePagos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablePagos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablePagos.setObjectName(_fromUtf8("tablePagos"))
        self.tablePagos.setColumnCount(2)
        self.tablePagos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablePagos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePagos.setHorizontalHeaderItem(1, item)
        self.tablePagos.horizontalHeader().setStretchLastSection(True)
        self.tablePagos.verticalHeader().setSortIndicatorShown(False)
        self.tablePagos.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tablePagos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnEliminar = QtGui.QPushButton(Dialog)
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.horizontalLayout_2.addWidget(self.btnEliminar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(Dialog)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_4.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(Dialog)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.rbtnTC.setText(_translate("Dialog", "Tarjeta de Crédito", None))
        self.rbtnTD.setText(_translate("Dialog", "Tarjeta de Débito", None))
        self.rbtnNC.setText(_translate("Dialog", "Nota de Crédito", None))
        self.rbtnEfectivo.setText(_translate("Dialog", "Efectivo", None))
        self.lblImporte.setText(_translate("Dialog", "Importe a Pagar: $0.00", None))
        item = self.tablePagos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Tipo de Pago", None))
        item = self.tablePagos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Importe", None))
        self.btnEliminar.setText(_translate("Dialog", "Eliminar", None))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar", None))


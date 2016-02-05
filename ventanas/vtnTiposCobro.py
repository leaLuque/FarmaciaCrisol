# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnTiposCobro.ui'
#
# Created: Thu Feb  4 14:29:42 2016
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
        Dialog.resize(645, 380)
        self.tablePagos = QtGui.QTableWidget(Dialog)
        self.tablePagos.setGeometry(QtCore.QRect(10, 100, 621, 192))
        self.tablePagos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablePagos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablePagos.setObjectName(_fromUtf8("tablePagos"))
        self.tablePagos.setColumnCount(3)
        self.tablePagos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablePagos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePagos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablePagos.setHorizontalHeaderItem(2, item)
        self.tablePagos.horizontalHeader().setStretchLastSection(True)
        self.tablePagos.verticalHeader().setSortIndicatorShown(False)
        self.tablePagos.verticalHeader().setStretchLastSection(False)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbtnTC = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnTC.setObjectName(_fromUtf8("rbtnTC"))
        self.horizontalLayout.addWidget(self.rbtnTC)
        self.rbtnTD = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnTD.setObjectName(_fromUtf8("rbtnTD"))
        self.horizontalLayout.addWidget(self.rbtnTD)
        self.rbtnNC = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnNC.setObjectName(_fromUtf8("rbtnNC"))
        self.horizontalLayout.addWidget(self.rbtnNC)
        self.rbtnEfectivo = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.rbtnEfectivo.setChecked(True)
        self.rbtnEfectivo.setObjectName(_fromUtf8("rbtnEfectivo"))
        self.horizontalLayout.addWidget(self.rbtnEfectivo)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 69, 621, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblImporte = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblImporte.setFont(font)
        self.lblImporte.setObjectName(_fromUtf8("lblImporte"))
        self.horizontalLayout_3.addWidget(self.lblImporte)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 340, 621, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_4.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        self.btnEliminar = QtGui.QPushButton(Dialog)
        self.btnEliminar.setGeometry(QtCore.QRect(530, 300, 98, 27))
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.tablePagos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Número", None))
        item = self.tablePagos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tipo de Pago", None))
        item = self.tablePagos.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Importe", None))
        self.rbtnTC.setText(_translate("Dialog", "Tarjeta de Crédito", None))
        self.rbtnTD.setText(_translate("Dialog", "Tarjeta de Débito", None))
        self.rbtnNC.setText(_translate("Dialog", "Nota de Crédito", None))
        self.rbtnEfectivo.setText(_translate("Dialog", "Efectivo", None))
        self.lblImporte.setText(_translate("Dialog", "Importe a Pagar: $0.00", None))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar", None))
        self.btnEliminar.setText(_translate("Dialog", "Eliminar", None))


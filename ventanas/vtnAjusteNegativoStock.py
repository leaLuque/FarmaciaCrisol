# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAjusteNegativoStock.ui'
#
# Created: Thu Feb 11 12:40:56 2016
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

class Ui_vtnAjusteNegativoStock(object):
    def setupUi(self, vtnAjusteNegativoStock):
        vtnAjusteNegativoStock.setObjectName(_fromUtf8("vtnAjusteNegativoStock"))
        vtnAjusteNegativoStock.resize(658, 395)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAjusteNegativoStock)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbProducto = QtGui.QGroupBox(vtnAjusteNegativoStock)
        self.gbProducto.setObjectName(_fromUtf8("gbProducto"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbProducto)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gbProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineCod_Barra = QtGui.QLineEdit(self.gbProducto)
        self.lineCod_Barra.setObjectName(_fromUtf8("lineCod_Barra"))
        self.horizontalLayout.addWidget(self.lineCod_Barra)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gbLote = QtGui.QGroupBox(self.gbProducto)
        self.gbLote.setObjectName(_fromUtf8("gbLote"))
        self.formLayout_2 = QtGui.QFormLayout(self.gbLote)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.gbLote)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineCod_Lote = QtGui.QLineEdit(self.gbLote)
        self.lineCod_Lote.setObjectName(_fromUtf8("lineCod_Lote"))
        self.horizontalLayout_2.addWidget(self.lineCod_Lote)
        self.btnBuscar = QtGui.QPushButton(self.gbLote)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout_2.addWidget(self.btnBuscar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.gbLote)
        self.tablaLoteProducto = QtGui.QTableWidget(self.gbProducto)
        self.tablaLoteProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaLoteProducto.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaLoteProducto.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaLoteProducto.setObjectName(_fromUtf8("tablaLoteProducto"))
        self.tablaLoteProducto.setColumnCount(5)
        self.tablaLoteProducto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaLoteProducto.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaLoteProducto.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaLoteProducto.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaLoteProducto.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaLoteProducto.setHorizontalHeaderItem(4, item)
        self.tablaLoteProducto.horizontalHeader().setDefaultSectionSize(120)
        self.tablaLoteProducto.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tablaLoteProducto)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.gbProducto)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.spinCantidad = QtGui.QSpinBox(self.gbProducto)
        self.spinCantidad.setMinimum(1)
        self.spinCantidad.setMaximum(500)
        self.spinCantidad.setSingleStep(10)
        self.spinCantidad.setObjectName(_fromUtf8("spinCantidad"))
        self.horizontalLayout_8.addWidget(self.spinCantidad)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.gbProducto)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btnAceptar = QtGui.QPushButton(vtnAjusteNegativoStock)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnAjusteNegativoStock)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_5.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(vtnAjusteNegativoStock)
        QtCore.QMetaObject.connectSlotsByName(vtnAjusteNegativoStock)
        vtnAjusteNegativoStock.setTabOrder(self.lineCod_Barra, self.lineCod_Lote)
        vtnAjusteNegativoStock.setTabOrder(self.lineCod_Lote, self.btnBuscar)
        vtnAjusteNegativoStock.setTabOrder(self.btnBuscar, self.tablaLoteProducto)
        vtnAjusteNegativoStock.setTabOrder(self.tablaLoteProducto, self.spinCantidad)
        vtnAjusteNegativoStock.setTabOrder(self.spinCantidad, self.btnAceptar)
        vtnAjusteNegativoStock.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnAjusteNegativoStock):
        vtnAjusteNegativoStock.setWindowTitle(_translate("vtnAjusteNegativoStock", "Ajuste Negativo Stock", None))
        self.gbProducto.setTitle(_translate("vtnAjusteNegativoStock", "Producto", None))
        self.label.setText(_translate("vtnAjusteNegativoStock", "Código de Barra", None))
        self.lineCod_Barra.setStatusTip(_translate("vtnAjusteNegativoStock", "Ingrese código de barra del producto (exactamente 9 números)", None))
        self.lineCod_Barra.setAccessibleDescription(_translate("vtnAjusteNegativoStock", "codigo", None))
        self.gbLote.setTitle(_translate("vtnAjusteNegativoStock", "Lote", None))
        self.label_3.setText(_translate("vtnAjusteNegativoStock", "Código", None))
        self.lineCod_Lote.setStatusTip(_translate("vtnAjusteNegativoStock", "Ingrese código del lote (solo letras y números sin espacios)", None))
        self.lineCod_Lote.setAccessibleDescription(_translate("vtnAjusteNegativoStock", "codLote", None))
        self.btnBuscar.setText(_translate("vtnAjusteNegativoStock", "Buscar", None))
        item = self.tablaLoteProducto.horizontalHeaderItem(0)
        item.setText(_translate("vtnAjusteNegativoStock", "Código de Barra", None))
        item = self.tablaLoteProducto.horizontalHeaderItem(1)
        item.setText(_translate("vtnAjusteNegativoStock", "Medicamento", None))
        item = self.tablaLoteProducto.horizontalHeaderItem(2)
        item.setText(_translate("vtnAjusteNegativoStock", "Presentacion", None))
        item = self.tablaLoteProducto.horizontalHeaderItem(3)
        item.setText(_translate("vtnAjusteNegativoStock", "Código Lote", None))
        item = self.tablaLoteProducto.horizontalHeaderItem(4)
        item.setText(_translate("vtnAjusteNegativoStock", "Cantidad", None))
        self.label_2.setText(_translate("vtnAjusteNegativoStock", "* Cantidad", None))
        self.spinCantidad.setStatusTip(_translate("vtnAjusteNegativoStock", "Ingrese la cantidad del Producto para dicho lote", None))
        self.btnAceptar.setText(_translate("vtnAjusteNegativoStock", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnAjusteNegativoStock", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAjusteNegativoStock = QtGui.QWidget()
    ui = Ui_vtnAjusteNegativoStock()
    ui.setupUi(vtnAjusteNegativoStock)
    vtnAjusteNegativoStock.show()
    sys.exit(app.exec_())


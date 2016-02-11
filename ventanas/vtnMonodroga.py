# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnMonodroga.ui'
#
# Created: Thu Feb 11 12:41:22 2016
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

class Ui_vtnMonodroga(object):
    def setupUi(self, vtnMonodroga):
        vtnMonodroga.setObjectName(_fromUtf8("vtnMonodroga"))
        vtnMonodroga.resize(568, 483)
        self.verticalLayout = QtGui.QVBoxLayout(vtnMonodroga)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(vtnMonodroga)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineNombre = QtGui.QLineEdit(vtnMonodroga)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.horizontalLayout.addWidget(self.lineNombre)
        self.btnBuscar = QtGui.QPushButton(vtnMonodroga)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label = QtGui.QLabel(vtnMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtGui.QLabel(vtnMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmbTipoVenta = QtGui.QComboBox(vtnMonodroga)
        self.cmbTipoVenta.setObjectName(_fromUtf8("cmbTipoVenta"))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbTipoVenta)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.txtDescripcion = QtGui.QTextEdit(vtnMonodroga)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.gridLayout.addWidget(self.txtDescripcion, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupMonodroga = QtGui.QGroupBox(vtnMonodroga)
        self.groupMonodroga.setObjectName(_fromUtf8("groupMonodroga"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupMonodroga)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tablaMonodroga = QtGui.QTableWidget(self.groupMonodroga)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setTabKeyNavigation(True)
        self.tablaMonodroga.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaMonodroga.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(3)
        self.tablaMonodroga.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(2, item)
        self.tablaMonodroga.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tablaMonodroga)
        self.verticalLayout.addWidget(self.groupMonodroga)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(vtnMonodroga)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_3.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnMonodroga)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_3.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(vtnMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnMonodroga)
        vtnMonodroga.setTabOrder(self.lineNombre, self.btnBuscar)
        vtnMonodroga.setTabOrder(self.btnBuscar, self.cmbTipoVenta)
        vtnMonodroga.setTabOrder(self.cmbTipoVenta, self.txtDescripcion)
        vtnMonodroga.setTabOrder(self.txtDescripcion, self.tablaMonodroga)
        vtnMonodroga.setTabOrder(self.tablaMonodroga, self.btnAceptar)
        vtnMonodroga.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnMonodroga):
        vtnMonodroga.setWindowTitle(_translate("vtnMonodroga", "Alta Monodroga", None))
        self.label_4.setText(_translate("vtnMonodroga", "* Tipo de Venta", None))
        self.lineNombre.setStatusTip(_translate("vtnMonodroga", "Ingrese el nombre de la monodroga", None))
        self.lineNombre.setAccessibleDescription(_translate("vtnMonodroga", "monodroga", None))
        self.btnBuscar.setText(_translate("vtnMonodroga", "Buscar", None))
        self.label.setText(_translate("vtnMonodroga", "* Nombre", None))
        self.label_2.setText(_translate("vtnMonodroga", "Descripción", None))
        self.cmbTipoVenta.setStatusTip(_translate("vtnMonodroga", "Seleccione el tipo de venta que la monodroga exige", None))
        self.cmbTipoVenta.setItemText(0, _translate("vtnMonodroga", "Libre", None))
        self.cmbTipoVenta.setItemText(1, _translate("vtnMonodroga", "Receta", None))
        self.cmbTipoVenta.setItemText(2, _translate("vtnMonodroga", "Receta Archivada", None))
        self.txtDescripcion.setStatusTip(_translate("vtnMonodroga", "Ingrese la descripción de la monodroga (opcional)", None))
        self.groupMonodroga.setTitle(_translate("vtnMonodroga", "Monodroga", None))
        item = self.tablaMonodroga.horizontalHeaderItem(0)
        item.setText(_translate("vtnMonodroga", "Nombre", None))
        item = self.tablaMonodroga.horizontalHeaderItem(1)
        item.setText(_translate("vtnMonodroga", "Tipo de Venta", None))
        item = self.tablaMonodroga.horizontalHeaderItem(2)
        item.setText(_translate("vtnMonodroga", "Descripción", None))
        self.btnAceptar.setText(_translate("vtnMonodroga", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnMonodroga", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnMonodroga = QtGui.QWidget()
    ui = Ui_vtnMonodroga()
    ui.setupUi(vtnMonodroga)
    vtnMonodroga.show()
    sys.exit(app.exec_())


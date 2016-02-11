# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnCliente.ui'
#
# Created: Thu Feb 11 12:42:12 2016
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

class Ui_vtnCliente(object):
    def setupUi(self, vtnCliente):
        vtnCliente.setObjectName(_fromUtf8("vtnCliente"))
        vtnCliente.resize(720, 466)
        self.verticalLayout_2 = QtGui.QVBoxLayout(vtnCliente)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(vtnCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtGui.QLabel(vtnCliente)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineApellido = QtGui.QLineEdit(vtnCliente)
        self.lineApellido.setObjectName(_fromUtf8("lineApellido"))
        self.gridLayout.addWidget(self.lineApellido, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(vtnCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineTelefono = QtGui.QLineEdit(vtnCliente)
        self.lineTelefono.setEnabled(True)
        self.lineTelefono.setObjectName(_fromUtf8("lineTelefono"))
        self.gridLayout.addWidget(self.lineTelefono, 5, 1, 1, 1)
        self.lineNombre = QtGui.QLineEdit(vtnCliente)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.gridLayout.addWidget(self.lineNombre, 1, 1, 1, 1)
        self.lineDni = QtGui.QLineEdit(vtnCliente)
        self.lineDni.setObjectName(_fromUtf8("lineDni"))
        self.gridLayout.addWidget(self.lineDni, 0, 1, 1, 1)
        self.label = QtGui.QLabel(vtnCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtGui.QLabel(vtnCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineDireccion = QtGui.QLineEdit(vtnCliente)
        self.lineDireccion.setObjectName(_fromUtf8("lineDireccion"))
        self.gridLayout.addWidget(self.lineDireccion, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnBuscar = QtGui.QPushButton(vtnCliente)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout_2.addWidget(self.btnBuscar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBuscar = QtGui.QGroupBox(vtnCliente)
        self.groupBuscar.setObjectName(_fromUtf8("groupBuscar"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBuscar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableClientes = QtGui.QTableWidget(self.groupBuscar)
        self.tableClientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableClientes.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableClientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableClientes.setObjectName(_fromUtf8("tableClientes"))
        self.tableClientes.setColumnCount(5)
        self.tableClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(4, item)
        self.tableClientes.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableClientes)
        self.verticalLayout_2.addWidget(self.groupBuscar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(vtnCliente)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnCliente)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(vtnCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnCliente)
        vtnCliente.setTabOrder(self.lineDni, self.lineNombre)
        vtnCliente.setTabOrder(self.lineNombre, self.lineApellido)
        vtnCliente.setTabOrder(self.lineApellido, self.btnBuscar)
        vtnCliente.setTabOrder(self.btnBuscar, self.lineDireccion)
        vtnCliente.setTabOrder(self.lineDireccion, self.lineTelefono)
        vtnCliente.setTabOrder(self.lineTelefono, self.tableClientes)
        vtnCliente.setTabOrder(self.tableClientes, self.btnAceptar)
        vtnCliente.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnCliente):
        vtnCliente.setWindowTitle(_translate("vtnCliente", "Form", None))
        self.label_2.setText(_translate("vtnCliente", "* DNI", None))
        self.label_5.setText(_translate("vtnCliente", "* Nombre", None))
        self.lineApellido.setStatusTip(_translate("vtnCliente", "Ingrese Apellido del cliente (solo letras)", None))
        self.lineApellido.setAccessibleDescription(_translate("vtnCliente", "nya", None))
        self.label_3.setText(_translate("vtnCliente", "* Dirección", None))
        self.lineTelefono.setStatusTip(_translate("vtnCliente", "Ingrese Teléfono del cliente (solo números, máximo 20 números)", None))
        self.lineTelefono.setAccessibleDescription(_translate("vtnCliente", "telefono", None))
        self.lineNombre.setStatusTip(_translate("vtnCliente", "Ingrese Nombre del cliente (solo letras)", None))
        self.lineNombre.setAccessibleDescription(_translate("vtnCliente", "nya", None))
        self.lineDni.setStatusTip(_translate("vtnCliente", "Ingrese DNI del cliente (exactamente 8 números)", None))
        self.lineDni.setAccessibleDescription(_translate("vtnCliente", "dni", None))
        self.label.setText(_translate("vtnCliente", "* Apellido", None))
        self.label_4.setText(_translate("vtnCliente", "Teléfono", None))
        self.lineDireccion.setStatusTip(_translate("vtnCliente", "Ingrese Dirección del cliente", None))
        self.lineDireccion.setAccessibleDescription(_translate("vtnCliente", "direccion", None))
        self.btnBuscar.setText(_translate("vtnCliente", "Buscar", None))
        self.groupBuscar.setTitle(_translate("vtnCliente", "Clientes", None))
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("vtnCliente", "DNI", None))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("vtnCliente", "Nombre", None))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("vtnCliente", "Apellido", None))
        item = self.tableClientes.horizontalHeaderItem(3)
        item.setText(_translate("vtnCliente", "Dirección", None))
        item = self.tableClientes.horizontalHeaderItem(4)
        item.setText(_translate("vtnCliente", "Teléfono", None))
        self.btnAceptar.setText(_translate("vtnCliente", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnCliente", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnCliente = QtGui.QWidget()
    ui = Ui_vtnCliente()
    ui.setupUi(vtnCliente)
    vtnCliente.show()
    sys.exit(app.exec_())


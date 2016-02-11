# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnListar.ui'
#
# Created: Thu Feb 11 12:41:43 2016
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

class Ui_vtnListar(object):
    def setupUi(self, vtnListar):
        vtnListar.setObjectName(_fromUtf8("vtnListar"))
        vtnListar.resize(412, 220)
        self.verticalLayout_2 = QtGui.QVBoxLayout(vtnListar)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.cbTipoListado = QtGui.QComboBox(vtnListar)
        self.cbTipoListado.setObjectName(_fromUtf8("cbTipoListado"))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.cbTipoListado)
        self.gbOption = QtGui.QGroupBox(vtnListar)
        self.gbOption.setTitle(_fromUtf8(""))
        self.gbOption.setObjectName(_fromUtf8("gbOption"))
        self.rbtnPDF = QtGui.QRadioButton(self.gbOption)
        self.rbtnPDF.setGeometry(QtCore.QRect(0, 0, 116, 22))
        self.rbtnPDF.setChecked(True)
        self.rbtnPDF.setObjectName(_fromUtf8("rbtnPDF"))
        self.rbtnExcel = QtGui.QRadioButton(self.gbOption)
        self.rbtnExcel.setGeometry(QtCore.QRect(160, 0, 116, 22))
        self.rbtnExcel.setObjectName(_fromUtf8("rbtnExcel"))
        self.verticalLayout_2.addWidget(self.gbOption)
        self.gbFechas = QtGui.QGroupBox(vtnListar)
        self.gbFechas.setEnabled(False)
        self.gbFechas.setTitle(_fromUtf8(""))
        self.gbFechas.setObjectName(_fromUtf8("gbFechas"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gbFechas)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gbFechas)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.deFechaDesde = QtGui.QDateEdit(self.gbFechas)
        self.deFechaDesde.setObjectName(_fromUtf8("deFechaDesde"))
        self.horizontalLayout.addWidget(self.deFechaDesde)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.gbFechas)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.deFechaHasta = QtGui.QDateEdit(self.gbFechas)
        self.deFechaHasta.setObjectName(_fromUtf8("deFechaHasta"))
        self.horizontalLayout_2.addWidget(self.deFechaHasta)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.gbFechas)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnListar = QtGui.QPushButton(vtnListar)
        self.btnListar.setObjectName(_fromUtf8("btnListar"))
        self.horizontalLayout_3.addWidget(self.btnListar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(vtnListar)
        QtCore.QMetaObject.connectSlotsByName(vtnListar)

    def retranslateUi(self, vtnListar):
        vtnListar.setWindowTitle(_translate("vtnListar", "Listar", None))
        self.cbTipoListado.setItemText(0, _translate("vtnListar", "Productos en Stock", None))
        self.cbTipoListado.setItemText(1, _translate("vtnListar", "Clientes", None))
        self.cbTipoListado.setItemText(2, _translate("vtnListar", "Ventas Realizadas", None))
        self.rbtnPDF.setText(_translate("vtnListar", "PDF", None))
        self.rbtnExcel.setText(_translate("vtnListar", "Planilla Excel", None))
        self.label.setText(_translate("vtnListar", "Fecha Desde", None))
        self.label_2.setText(_translate("vtnListar", "Fecha Hasta", None))
        self.btnListar.setText(_translate("vtnListar", "Listar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnListar = QtGui.QWidget()
    ui = Ui_vtnListar()
    ui.setupUi(vtnListar)
    vtnListar.show()
    sys.exit(app.exec_())


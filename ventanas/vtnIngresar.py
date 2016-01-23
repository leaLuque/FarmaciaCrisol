# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnIngresar.ui'
#
# Created: Wed Apr  1 14:28:26 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_vtnIngresar(object):
    def setupUi(self, vtnIngresar):
        vtnIngresar.setObjectName(_fromUtf8("vtnIngresar"))
        vtnIngresar.resize(484, 113)
        self.formLayout = QtGui.QFormLayout(vtnIngresar)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(vtnIngresar)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineUsuario = QtGui.QLineEdit(vtnIngresar)
        self.lineUsuario.setObjectName(_fromUtf8("lineUsuario"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineUsuario)
        self.label_2 = QtGui.QLabel(vtnIngresar)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineContrasenia = QtGui.QLineEdit(vtnIngresar)
        self.lineContrasenia.setEchoMode(QtGui.QLineEdit.Password)
        self.lineContrasenia.setObjectName(_fromUtf8("lineContrasenia"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineContrasenia)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(vtnIngresar)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnIngresar)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_5.addWidget(self.btnCancelar)
        self.formLayout.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_5)

        self.retranslateUi(vtnIngresar)
        QtCore.QMetaObject.connectSlotsByName(vtnIngresar)

    def retranslateUi(self, vtnIngresar):
        vtnIngresar.setWindowTitle(_translate("vtnIngresar", "Ingresar", None))
        self.label.setText(_translate("vtnIngresar", "Usuario", None))
        self.label_2.setText(_translate("vtnIngresar", "Contraseña", None))
        self.btnAceptar.setText(_translate("vtnIngresar", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnIngresar", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnIngresar = QtGui.QWidget()
    ui = Ui_vtnIngresar()
    ui.setupUi(vtnIngresar)
    vtnIngresar.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAyuda.ui'
#
# Created: Mon Jan 18 17:27:42 2016
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

class Ui_vtnAyuda(object):
    def setupUi(self, vtnAyuda):
        vtnAyuda.setObjectName(_fromUtf8("vtnAyuda"))
        vtnAyuda.resize(713, 545)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAyuda)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(vtnAyuda)
        QtCore.QMetaObject.connectSlotsByName(vtnAyuda)

    def retranslateUi(self, vtnAyuda):
        vtnAyuda.setWindowTitle(_translate("vtnAyuda", "Ayuda", None))


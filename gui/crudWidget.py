# coding=utf-8
__author__ = 'waldo'

from PyQt4 import QtCore

from gui import MdiWidget

class CRUDWidget(MdiWidget):
    objectCreated = QtCore.pyqtSignal()
    objectModified = QtCore.pyqtSignal()
    objectDeleted = QtCore.pyqtSignal()
    instances = {
        'C': None,
        'R': None,
        'U': None,
        'D': None,
    }

    def actualizar(self):
        pass

    @classmethod
    def actionWidget(cls, tipo):
        return cls.instances[tipo]

    @classmethod
    def create(cls, mdi):
        cls.instances['C'] = gui = cls(mdi)
        gui.setWindowTitle("Alta %s" % cls.__name__)
        modificar = cls.actionWidget('U')
        if modificar:
            gui.objectCreated.connect(modificar.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            gui.objectCreated.connect(borrar.actualizar)
        leer = cls.actionWidget('R')
        if leer:
            gui.objectCreated.connect(leer.actualizar)
        return gui

    @classmethod
    def read(cls, mdi):
        cls.instances['R'] = gui = cls(mdi)
        gui.setWindowTitle("Alta %s" % cls.__name__)
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
        modificar = cls.actionWidget('U')
        if modificar:
            modificar.objectModified.connect(gui.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            borrar.objectDeleted.connect(gui.actualizar)
        return gui

    @classmethod
    def update(cls, mdi):
        cls.instances['U'] = gui = cls(mdi)
        gui.setWindowTitle(QtCore.QString.fromUtf8("Modificación %s" % cls.__name__))
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
            gui.objectModified.connect(alta.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            borrar.objectDeleted.connect(gui.actualizar)
            gui.objectModified.connect(borrar.actualizar)
        return gui

    @classmethod
    def delete(cls, mdi):
        cls.instances['D'] = gui = cls(mdi)
        gui.setWindowTitle("Baja %s" % cls.__name__)
        gui.objectModified.connect(gui.actualizar)
        modificar = cls.actionWidget('U')
        if modificar:
            modificar.objectModified.connect(gui.actualizar)
            gui.objectModified.connect(modificar.actualizar)
        leer = cls.actionWidget('R')
        if leer:
            gui.objectDeleted.connect(leer.actualizar)
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
            gui.objectDeleted.connect(alta.actualizar)
        return gui

    def bajaValida(self, model, campo, var):
        resultado = model.buscarAlta(campo, self.sesion, var).all()
        if resultado.__len__() > 0:
            return False
        return True
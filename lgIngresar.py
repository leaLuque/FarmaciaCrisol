# -*- coding: utf-8 -*-
__author__ = 'waldo'

from PyQt4 import QtGui

from ventanas import Ui_vtnIngresar
from gui import MdiWidget
from login import Login

class Ingresar(MdiWidget, Ui_vtnIngresar):
    """
        Clase que modela el comportamiento de Ingresar
    """
    def __init__(self, mdi):
        """
            Constructor de la clase Ingresar
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.btnAceptar.pressed.connect(self.validarUsuario)
        self.btnCancelar.pressed.connect(self.limpiarCampos)
        self.lineUsuario.returnPressed.connect(self.validarUsuario)
        self.lineContrasenia.returnPressed.connect(self.validarUsuario)

    def limpiarCampos(self):
        """
            Limpia los campos de la ventana
        :return:
        """
        self.lineUsuario.clear()
        self.lineContrasenia.clear()

    def validarUsuario(self):
        """
            Valida al usuario ingresada
        :return:
        """
        log=Login(str(self.lineUsuario.text()), str(self.lineContrasenia.text()),
                  self.mdi().window().getSesionBD())
        rol=log.loginValido()
        if (rol):
            self.mdi().hide()
            self.habilitarPermisos(rol)
            self.limpiarCampos()
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'Usuario o Contraseña incorrecta.', 'Aceptar')

    def habilitarPermisos(self, rol):
        """
            Setea los permisos a las ventanas,
            de acuerdo al rol del usuario
        :param rol Rol del usuario:
        :return:
        """
        self.mdi().window().deshabilitarMenu()
        permisos={'far': self.mdi().window().farmaceutico, 'tec': self.mdi().window().tecnico_farmaceutico,
                  'adm': self.mdi().window().administrador}
        hab_vtn=permisos[rol]
        for hab in hab_vtn:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(True)
            else:
                hab.setVisible(True)
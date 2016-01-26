# -*- coding: utf-8 -*-
__author__ = 'waldo'

from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtCore import QRegExp

class ValidarDatos():
    """
    Lógica de la validación de los datos ingresados.
    """
    @classmethod
    def setValidador(cls, campos):
        """
        Setea el tipo de validación para cada campo recibido en el arreglo "campos".
        :param campos: arreglo con los campos a validar.
        :return:
        """
        regexp = None
        for campo in campos:
            c = campo.accessibleDescription()
            if c == "palabra":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+")
            elif c == "texto":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+[a-zA-Zéáúóíñ ]*")
            elif c == "numeros":
                regexp = QRegExp("[1-9]\d{1,4}")
            elif c == "textoNumeros":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9]+[a-zA-Zéáúóíñ0-9 ]*")
            elif c == "codigo":
                regexp = QRegExp("\d{9}")
            elif c == "importe":
                regexp = QRegExp("[1-9]\d*\.\d{2}")
            elif c == "codLote":
                regexp = QRegExp("[0-9A-Za-z]{2,10}")
            elif c == "cantidad":
                regexp = QRegExp("[1-9]\d{1,6}")
            elif c == "dni":
                regexp = QRegExp("\d{8}")
            elif c == "telefono":
                regexp = QRegExp("\d{0,20}")
            elif c == "direccion":
                regexp = QRegExp(".+\d{0,5}")
            elif c == "nya":
                regexp = QRegExp("[a-zA-Zéáúóíñ]{2,15}(\s[a-zA-Zéáúóíñ]{2,15})*")
            elif c == "fmonodroga":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9\-\, ]*")
            elif c == "fmedicamento":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9 ]*")
            elif c == "frazonsocial":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9 ]*")
            elif c == "fnroremito":
                regexp = QRegExp("[0-9]*")

            validator = QRegExpValidator(regexp)
            campo.setValidator(validator)

    @classmethod
    def validarCamposVacios(cls, campos):
        """
        Verifica que los campos del arreglo "campos" no esten vacios.
        :param campos:
        :return:
        """
        for campo in campos:
            if campo.text() == "":
                return False
        return True
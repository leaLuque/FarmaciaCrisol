# -*- coding:utf-8 -*-

from baseDatos.objetoBase import ObjetoBase

class Cliente (ObjetoBase):
    """
    Objeto Cliente a almacenar en la base de datos.
    """
    requeridos = ("dni", "nombre", "apellido", "direccion")
    noRequeridos = ("telefono", )

    def __init__(self, dni, nombre, apellido, direccion, telefono):
        """
        Constructor de la clase Cliente.
        :param dni:
        :param nombre:
        :param apellido:
        :param direccion:
        :param telefono:
        :return:
        """
        ObjetoBase.__init__(self)
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def getDni(self):
        """
        Devuelve el dni del cliente.
        :return: dni
        """
        return self.dni

    def getNombre(self):
        """
        Decuelve el nombre del cliente.
        :return: nombre
        """
        return self.nombre

    def getApellido(self):
        """
        Devuelve el apellido del cliente.
        :return: apellido
        """
        return self.apellido

    def getDireccion(self):
        """
        Devuelve la dirección del cliente.
        :return: dirección
        """
        return self.direccion

    def getTelefono(self):
        """
        Devuelve el teléfono del cliente.
        :return:
        """
        return self.telefono

    def setDni(self, dni):
        """
        Setea el dni del cliente.
        :param dni:
        :return:
        """
        self.dni = dni

    def setNombre(self, nombre):
        """
        Setea el nombre del cliente.
        :param nombre:
        :return:
        """
        self.nombre = nombre

    def setApellido(self, apellido):
        """
        Setea el apellido del cliente.
        :param apellido:
        :return:
        """
        self.apellido = apellido

    def setDireccion(self,direccion):
        """
        Setea la dirección del cliente.
        :param direccion:
        :return:
        """
        self.direccion=direccion

    def setTelefono(self, telefono):
        """
        Setea el telefono del cliente.
        :param telefono:
        :return:
        """
        self.telefono=telefono

    @classmethod
    def getDatosCliente(cls,session,dni):
        """
            Devuelve los datos de un cliente determinado
        :param dni:
        :param session:
        :return Diccionario con datos del cliente:
        """
        temp = {}
        cliente = session.query(cls).filter(cls.dni == dni).first()
        temp["nombre"] = str(cliente.nombre)
        temp["apellido"] =str(cliente.apellido)
        temp["direccion"] = str(cliente.direccion)
        temp["telefono"] = str(cliente.telefono)
        return temp
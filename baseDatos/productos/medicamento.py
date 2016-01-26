#coding=utf-8
__author__ = 'waldo'

from baseDatos.objetoBase import ObjetoBase

class Monodroga(ObjetoBase):
    """
    Objeto Monodroga a almacenar en la base de datos.
    """
    requeridos = ("nombre",)
    noRequeridos = ()

    def __init__(self, nombre, tipo_venta, descripcion):
        """
        Constructor de la clase Monodroga.
        :param nombre:
        :param tipo_venta:
        :param descripcion:
        :return:
        """
        ObjetoBase.__init__(self)
        self.nombre=nombre
        self.tipo_venta=tipo_venta
        self.descripcion=descripcion

    def getNombre(self):
        """
        Devuelve el nombre de la monodroga.
        :return: nombre
        """
        return self.nombre

    def getTipoVenta(self):
        """
        Devuelve el tipo de venta de la monodroga.
        :return: tipo_venta
        """
        return self.tipo_venta

    def getDescripcion(self):
        """
        Devuelve la descripción de la monodroga.
        :return: descripcion
        """
        return self.descripcion

    def setTipoVenta(self, tipo_venta):
        """
        Setea el tipo de venta de la monodroga.
        :param tipo_venta:
        :return:
        """
        self.tipo_venta = tipo_venta

    def setDescripcion(self,descripcion):
        """
        Setea la descripción de la monodroga.
        :param descripcion:
        :return:
        """
        self.descripcion = descripcion

    def setNombre(self, nombre):
        """
        Setea el nombre de la monodroga.
        :param nombre:
        :return:
        """
        self.nombre = nombre

class Medicamento(ObjetoBase):
    """
    Objeto Medicamento a alamacenar en la base de datos.
    """
    requeridos = ("nombre_med", "nombre_mon")
    noRequeridos = ()

    def __init__(self, nombre_comercial, id_monodroga, cantidad_monodroga):
        """
        Constructor de la clase Medicamento.
        :param nombre_comercial:
        :param id_monodroga:
        :param cantidad_monodroga:
        :return:
        """
        ObjetoBase.__init__(self)
        self.nombre_comercial=nombre_comercial
        self.id_monodroga=id_monodroga
        self.cantidad_monodroga=cantidad_monodroga

    def getNombreComercial(self):
        """
        Devuelve el nombre comercial del medicamento.
        :return: nombre_comercial
        """
        return self.nombre_comercial

    def getIdMonodroga(self):
        """
        Devuelve el id de la monodroga de la cual se compone el medicamento.
        :return: id_monodroga
        """
        return self.id_monodroga

    def getCantidadMonodroga(self):
        """
        Devuelve la cantidad de la monodroga de la cual se compone el medicamento.
        :return: cantidad_monodroga
        """
        return self.cantidad_monodroga

    def setNombreComercial(self, nombre_comercial):
        """
        Setea el nombre comercial del medicamento.
        :param nombre_comercial:
        :return:
        """
        self.nombre_comercial = nombre_comercial

    def setIdMonodroga(self, id_monodroga):
        """
        Setea el id de la monodroga de la cual se compone el medicamento.
        :param id_monodroga:
        :return:
        """
        self.id_monodroga = id_monodroga

    def setCantidadMonodroga(self, cantidad_monodroga):
        """
        Setea la cantidad de la monodroga de la cual se compone el medicamento.
        :param cantidad_monodroga:
        :return:
        """
        self.cantidad_monodroga = cantidad_monodroga

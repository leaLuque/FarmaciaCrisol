#coding=utf-8
__author__ = 'waldo'

from sqlalchemy.orm import aliased

from baseDatos.objetoBase import ObjetoBase

class LoteProducto(ObjetoBase):
    """
    Objeto LoteProducto a almacenar en la base de datos.
    """
    requeridos = ("cod_barra", "cod_lote")
    noRequeridos=()

    def __init__(self, id_lote, id_producto, cantidad):
        """
        Constructor de la clase LoteProducto.
        :param id_lote:
        :param id_producto:
        :param cantidad:
        :return:
        """
        self.id_lote = id_lote
        self.id_producto = id_producto
        self.cantidad = cantidad

    def getIdLote(self):
        """
        Devuelve el id del lote.
        :return: id_lote
        """
        return self.id_lote

    def getIdProducto(self):
        """
        Devuelve el id del producto.
        :return: id_producto
        """
        return self.id_producto

    def getCantidad(self):
        """
        Devuelve la cantidad del lote/producto.
        :return: id_producto.
        """
        return self.cantidad

    def setIdLote(self, id_lote):
        """
        Setea el id del lote.
        :param id_lote:
        :return:
        """
        self.id_lote = id_lote

    def setIdProducto(self, id_producto):
        """
        Setea el id del producto.
        :param id_producto:
        :return:
        """
        self.id_producto = id_producto

    def setCantidad(self, cantidad):
        """
        Setea la cantidad del lote/producto.
        :param cantidad:
        :return:
        """
        self.cantidad = cantidad

    @classmethod
    def buscarTodosLoteProducto(cls, sesion, producto, lote):
        """
        Devuelve todos los lotes/productos almacenados en la base de datos.
        :param sesion:
        :param producto:
        :param lote:
        :return:
        """
        return sesion.query(producto.codigo_barra, producto.id_medicamento, producto.id_presentacion,
                 lote.codigo, cls.cantidad).\
        filter(cls.id_producto == producto.codigo_barra, cls.id_lote == lote.codigo, producto.baja == False).\
        order_by(producto.codigo_barra)

    @classmethod
    def buscarLoteProductoPorProducto(cls, sesion, producto, lote, varBusq):
        """
        Devuelve todos los lotes/productos almacenados en la base de datos para un producto determinado.
        :param sesion:
        :param producto:
        :param lote:
        :param varBusq:
        :return:
        """
        return sesion.query(producto.codigo_barra, producto.id_medicamento, producto.id_presentacion,
                 lote.codigo, cls.cantidad).\
        filter(cls.id_producto == producto.codigo_barra, cls.id_lote == lote.codigo,
               producto.codigo_barra == varBusq).\
        order_by(producto.codigo_barra)

    @classmethod
    def buscarLoteProductoPorLote(cls, sesion, producto, lote, varBusq):
        """
        Devuelve todos los lotes/productos almacenados en la base de datos para un lote determinado.
        :param sesion:
        :param producto:
        :param lote:
        :param varBusq:
        :return:
        """
        return sesion.query(producto.codigo_barra, producto.id_medicamento, producto.id_presentacion,
                 lote.codigo, cls.cantidad).\
        filter(cls.id_producto == producto.codigo_barra, cls.id_lote == lote.codigo,
               lote.codigo == varBusq).\
        order_by(producto.codigo_barra)

    #TODO los dos siguientes los hizo leandro.
    def descontarCantidad(self, cantidad):
        if self.cantidad < cantidad:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad

    def aumentarCantidad(self, cantidad):
        self.cantidad += cantidad

    @classmethod
    def buscarLoteProducto(cls, sesion, var1, var2):
        """
        Devuelve el lote/producto correspondiente a un lote y un producto determinado.
        :param sesion:
        :param var1:
        :param var2:
        :return:
        """
        return sesion.query(cls).filter(cls.id_producto == var1, cls.id_lote == var2)

    @classmethod
    def buscarFraccionable(cls, sesion, producto, lote, presentacion, var):
        """
        Devuelve los subproductos de un producto fraccionable.
        :param sesion:
        :param producto:
        :param lote:
        :param presentacion:
        :param var:
        :return:
        """
        producto_1 = aliased(producto)
        producto_2 = aliased(producto)
        return sesion.query(producto_2.codigo_barra, producto_2.id_medicamento, producto_2.id_presentacion,
                            lote.codigo, cls.cantidad).\
                filter(producto_1.id_presentacion == presentacion.tipo).\
                filter(producto_1.id_medicamento == producto_2.id_medicamento).\
                filter(presentacion.sub_presentacion == producto_2.id_presentacion).\
                filter(producto_2.codigo_barra == cls.id_producto).\
                filter(cls.id_lote == lote.codigo).\
                filter(producto_1.codigo_barra == var).\
                filter(producto_2.baja == False)

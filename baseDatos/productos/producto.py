# coding=utf-8
__author__ = 'waldo'

from sqlalchemy import func

from baseDatos.objetoBase import ObjetoBase
from baseDatos.productos import Medicamento
from baseDatos.productos.loteProducto import LoteProducto

class Presentacion(ObjetoBase):
    """
    Objeto Presentacion a almacenar en la base de datos.
    """
    requeridos = ("tipo", "unidad_medida")
    noRequeridos = ()

    def __init__(self, tipo, unidad_medida, cantidad_fracciones, sub_presentacion, super_presentacion):
        """
        Constructor de la clase Presentacion.
        :param tipo:
        :param unidad_medida:
        :param cantidad_fracciones:
        :param sub_presentacion:
        :param super_presentacion:
        :return:
        """
        ObjetoBase.__init__(self)
        self.tipo=tipo
        self.unidad_medida=unidad_medida
        self.cantidad_fracciones=cantidad_fracciones
        self.sub_presentacion=sub_presentacion
        self.super_presentacion=super_presentacion

    def getTipo(self):
        """
        Devuelve el tipo de la presentación.
        :return: tipo
        """
        return self.tipo

    def getUnidadMedida(self):
        """
        Devuelve la unidad de medida de la presentación.
        :return: unidad_medida
        """
        return self.unidad_medida

    def getCantidadFracciones(self):
        """
        Devuelve la cantidad de fracciones de la presentación.
        :return: cantidad_fracciones
        """
        return self.cantidad_fracciones

    def getSubPresentacion(self):
        """
        Devuelve la subpresentación de la presentación.
        :return: sub_presentacion
        """
        return self.sub_presentacion

    def getSuperPresentacion(self):
        """
        Devuelve la super presentación de la presentación.
        :return: super_presentacion
        """
        return self.super_presentacion

    def setTipo(self, tipo):
        """
        Setea el tipo de la presentación.
        :param tipo:
        :return:
        """
        self.tipo = tipo

    def setUnidadMedida(self, unidad_medida):
        """
        Setea la unidad de medida de la presentación.
        :param unidad_medida:
        :return:
        """
        self.unidad_medida = unidad_medida

    def setCantidadFracciones(self, cantidad_fracciones):
        """
        Setea la cantidad de fraccciones de la presentación.
        :param cantidad_fracciones:
        :return:
        """
        self.cantidad_fracciones = cantidad_fracciones

    def setSubPresentacion(self, sub_presentacion):
        """
        Setea la subpresentación de la presentación.
        :param sub_presentacion:
        :return:
        """
        self.sub_presentacion = sub_presentacion

    def setSuperPresentacion(self, super_presentacion):
        """
        Setea la super presentación de la presentación.
        :param super_presentacion:
        :return:
        """
        self.super_presentacion = super_presentacion

    @classmethod
    def listarFraccionables(cls, sesion):
        """
        Devuelve todas las subpresentaciones del las presentaciones fraccionables.
        :param sesion:
        :return:
        """
        return sesion.query(cls).\
            filter(Presentacion.sub_presentacion == None, Presentacion.super_presentacion == None,
                Presentacion.baja == False, Presentacion.cantidad_fracciones == 1)

class Lote(ObjetoBase):
    """
    Objeto Lote a almacenar en la base de datos.
    """
    requeridos = ("codigo", "cod_barra")
    noRequeridos=()

    def __init__(self, codigo, fecha_vencimiento):
        """
        Constructor de la clase Lote.
        :param codigo:
        :param fecha_vencimiento:
        :return:
        """
        self.codigo=codigo
        self.fecha_vencimiento=fecha_vencimiento

    def getCodigo(self):
        """
        Devuelve el código del lote.
        :return: codigo
        """
        return self.codigo

    def getFechaVencimiento(self):
        """
        Devuelve la fecha de vencimiento del lote.
        :return: fecha_vencimiento
        """
        return self.fecha_vencimiento

    def setCodigo(self, codigo):
        """
        Setea el código del lote.
        :param codigo:
        :return:
        """
        self.codigo = codigo

    def setFechaVencimiento(self, fecha_vencimiento):
        """
        Setea la fecha de vencimiento del lote.
        :param fecha_vencimiento:
        :return:
        """
        self.fecha_vencimiento = fecha_vencimiento

    def getCantidad(self,sesion):
        """
        Devuelve la cantidad de un producto para uno o más lotes.
        :param sesion:
        :return:
        """
        cantidad=0
        query=sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for a in query:
            cantidad+=a.cantidad
        return cantidad

    @classmethod
    def obtenerLoteProducto(cls,producto,sesion):
        query=sesion.query(cls).join(LoteProducto).filter(LoteProducto.id_lote==cls.codigo).\
                filter(LoteProducto.id_producto==producto).order_by(cls.fecha_vencimiento)
        return query.all()

class Producto(ObjetoBase):
    """
    Objeto Producto a almacenar en la base de datos.
    """
    requeridos = ("codigo_barra", "nomb_med", "tipo_pres", "importe", "cod_lote")
    noRequeridos=()

    def __init__(self, codigo_barra, id_medicamento, id_presentacion, importe):
        """
        Cosntructor de la clase Producto.
        :param codigo_barra:
        :param id_medicamento:
        :param id_presentacion:
        :param importe:
        :return:
        """
        ObjetoBase.__init__(self)
        self.codigo_barra = codigo_barra
        self.id_medicamento = id_medicamento
        self.id_presentacion = id_presentacion
        self.importe = importe

    def getCodigoBarra(self):
        """
        Devuelve el código de barra del producto.
        :return: codigo_barra
        """
        return self.codigo_barra

    def getIdMedicamento(self):
        """
        Devuelve el id del medicamento del cual se compone el producto.
        :return: id_medicamento
        """
        return self.id_medicamento

    def getIdPresentacion(self):
        """
        Devuelve el id de la presentación de la cual se compone el producto.
        :return: id_presentacion
        """
        return self.id_presentacion

    def getImporte(self):
        """
        Devuelve el importe del producto.
        :return: importe
        """
        return self.importe

    def setCodigoBarra(self, codigo_barra):
        """
        Setea el código de barra del producto.
        :param codigo_barra:
        :return:
        """
        self.codigo_barra = codigo_barra

    def setIdMedicamento(self, id_medicamento):
        """
        Setea el id del medicamento del cual se compone el producto.
        :param id_medicamento:
        :return:
        """
        self.id_medicamento = id_medicamento

    def setIdPresentacion(self, id_presentacion):
        """
        Setea el id de la presentacion de la cual se compone el producto.
        :param id_presentacion:
        :return:
        """
        self.id_presentacion = id_presentacion

    def setImporte(self, importe):
        """
        Setea el importe del producto.
        :param importe:
        :return:
        """
        self.importe = importe

    def getCantidad(self,sesion):
        """
            Devuelve la cantidad del producto.
        :param sesion:
        :return cantidad:
        """
        cantidad=0
        query=sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for a in query:
            cantidad+=a.cantidad
        return cantidad

    def getNombreMonodroga(self,sesion):
        """
            Devuelve el nombre de la monodroga del producto.
        :param sesion:
        :return Nombre Monodroga:
        """
        instance=sesion.query(Medicamento.id_monodroga).\
            filter(Medicamento.nombre_comercial == self.id_medicamento)
        return (instance.first().id_monodroga)

    def buscarLotes(self, sesion):
        """
        Busca los lotes y sus cantidades para un producto
        :param Sesion
        :return Arreglo con los lotes y cantidades correspondiente a un producto
		"""
        lotes={}
        query = sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for elemento in query:
            lotes[elemento.id_lote]=elemento.cantidad
        return lotes
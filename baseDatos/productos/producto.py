__author__ = 'waldo'
from baseDatos.objetoBase import ObjetoBase
from baseDatos.productos import Medicamento
from baseDatos.productos.loteProducto import LoteProducto
from sqlalchemy import func
class Presentacion(ObjetoBase):
    requeridos = ("tipo", "unidad_medida")
    noRequeridos = ()

    def __init__(self, tipo, unidad_medida, cantidad_fracciones, sub_presentacion, super_presentacion):
        ObjetoBase.__init__(self)
        self.tipo=tipo
        self.unidad_medida=unidad_medida
        self.cantidad_fracciones=cantidad_fracciones
        self.sub_presentacion=sub_presentacion
        self.super_presentacion=super_presentacion

    def getTipo(self):
        return self.tipo

    def getUnidadMedida(self):
        return self.unidad_medida

    def getCantidadFracciones(self):
        return self.cantidad_fracciones

    def getSubPresentacion(self):
        return self.sub_presentacion

    def getSuperPresentacion(self):
        return self.super_presentacion

    def setTipo(self, tipo):
        self.tipo = tipo

    def setUnidadMedida(self, unidad_medida):
        self.unidad_medida = unidad_medida

    def setCantidadFracciones(self, cantidad_fracciones):
        self.cantidad_fracciones = cantidad_fracciones

    def setSubPresentacion(self, sub_presentacion):
        self.sub_presentacion = sub_presentacion

    def setSuperPresentacion(self, super_presentacion):
        self.super_presentacion = super_presentacion

    @classmethod
    def listarFraccionables(cls, sesion):
         return sesion.query(cls).\
             filter(Presentacion.sub_presentacion == None, Presentacion.super_presentacion == None,
                    Presentacion.baja == False, Presentacion.cantidad_fracciones == 1)

    # def __init__(self, tipo, unidad, cantidad):
    #     self.tipo = tipo
    #     self.unidad = unidad
    #     self.cantidad = cantidad
    #     self.super_presentacion = None
    #     self.sub_presentaciones = []
    #
    # def __str__(self):
    #     return "%s" % self.tipo
    #
    # def agregar_subpresentacion(self, presentacion):
    #     self.sub_presentaciones.append(presentacion)
    #     presentacion.super_presentacion = self

class Lote(ObjetoBase):
    requeridos = ("codigo", "cod_barra")
    noRequeridos=()

    def __init__(self, codigo, fecha_vencimiento):
        self.codigo=codigo
        self.fecha_vencimiento=fecha_vencimiento

    def getCodigo(self):
        return self.codigo

    def getFechaVencimiento(self):
        return self.fecha_vencimiento

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setFechaVencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def getCantidad(self,sesion):
        cantidad=0
        query=sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for a in query:
            cantidad+=a.cantidad
        return cantidad

    @classmethod
    def loteValido(cls,numeroLote,sesion):
        lote=None
        query=sesion.query(Lote).filter(Lote.codigo==numeroLote)
        for a in query:
            lote=a
        return lote

    @classmethod
    def obtenerLoteProducto(cls,producto,sesion):
        query=sesion.query(cls).join(LoteProducto).filter(LoteProducto.id_lote==cls.codigo).\
                filter(LoteProducto.id_producto==producto).order_by(cls.fecha_vencimiento)
        return query.all()

class Producto(ObjetoBase):
    requeridos = ("codigo_barra", "nomb_med", "tipo_pres", "importe", "cod_lote")
    noRequeridos=()

    def __init__(self, codigo_barra, id_medicamento, id_presentacion, importe):
        ObjetoBase.__init__(self)
        self.codigo_barra = codigo_barra
        self.id_medicamento = id_medicamento
        self.id_presentacion = id_presentacion
        self.importe = importe

    def getCodigoBarra(self):
        return self.codigo_barra

    def getIdMedicamento(self):
        return self.id_medicamento

    def getIdPresentacion(self):
        return self.id_presentacion

    def getImporte(self):
        return self.importe

    def setCodigoBarra(self, codigo_barra):
        self.codigo_barra = codigo_barra

    def setIdMedicamento(self, id_medicamento):
        self.id_medicamento = id_medicamento

    def setIdPresentacion(self, id_presentacion):
        self.id_presentacion = id_presentacion

    def setImporte(self, importe):
        self.importe = importe

    def getCantidad(self,sesion):
        cantidad=0
        query=sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for a in query:
            cantidad+=a.cantidad
        return cantidad

    def __str__(self):
        return self.id_medicamento + self.id_presentacion

    @classmethod
    def buscarCantidad(cls, sesion, lote):
        return sesion.query(lote.id_producto, cls.id_medicamento,
                 cls.id_presentacion, func.sum(lote.cantidad)).\
        filter(cls.codigo_barra == lote.id_producto).\
            group_by(lote.id_producto, cls.id_medicamento,
                 cls.id_presentacion)\
        .order_by(lote.id_producto)

    def buscarLotes(self,sesion):
        """
            Busca los lotes y sus cantidades para un producto
        :param
            Sesion
        :return
            Arreglo con los lotes y cantidades correspondiente a un producto
        """
        lotes={}
        query = sesion.query(LoteProducto).filter(LoteProducto.id_producto==self.codigo_barra)
        for elemento in query:
            lotes[elemento.id_lote]=elemento.cantidad
        return lotes

    def getNombreMonodroga(self,sesion):
        instance=sesion.query(Medicamento.id_monodroga).\
            filter(Medicamento.nombre_comercial == self.id_medicamento)
        return (instance.first().id_monodroga)

    # def __init__(self, codigo, importe, cantidad, presentacion, lote, medicamento):
    #     self.codigo = codigo
    #     self.importe = importe
    #     self.cantidad = cantidad
    #     self.presentacion = presentacion
    #     self.lote = lote
    #     self.medicamento = medicamento
    #     productos.append(self)

    # def vender(self, cantidad):
    #     while self.cantidad < cantidad:
    #         prod = self.obtener_super_producto()
    #         prod.fraccionar(self)
    #     self.cantidad -= cantidad
    #
    # def obtener_super_producto(self):
    #     sp = self.presentacion.super_presentacion
    #     prods = [ p for p in productos if p.presentacion == sp and p.medicamento == self.medicamento ]
    #     if prods:
    #         return prods[0]
    #     raise Exception("no puedo mas")
    #
    # def fraccionar(self, producto):
    #     while self.cantidad == 0:
    #         prod = self.obtener_super_producto()
    #         prod.fraccionar(self)
    #     self.cantidad -= 1
    #     producto.cantidad += self.presentacion.cantidad
    #
    # def __str__(self):
    #     return "%s - %s (%d)" % (self.medicamento, self.presentacion, self.cantidad)

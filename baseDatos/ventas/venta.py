# -*- coding:utf-8 -*-
from baseDatos.productos import ObjetoBase
from baseDatos.productos import Producto
from datetime import date

class Remito(ObjetoBase):
    def __init__(self, numero,cliente):
        ObjetoBase.__init__(self)
        self.numero=numero
        self.cliente=cliente
        self.fecha_emision=date.today()
        self.cobrado=None
        self.anulado=False

    def getFechaEmision(self):
        return self.fecha_emision

    def getCliente(self):
        return self.cliente

    def getCobrado(self):
        return self.cobrado

    def setCobrado(self,numeroFactura):
        self.cobrado=numeroFactura

    def anular(self):
        self.anulado=True

    def estoyCobrado(self):
        return self.cobrado

    @classmethod
    def getRemito(cls,numero,sesion):
        query=sesion.query(Remito).filter(Remito.numero==numero, Remito.baja==False)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def buscarDetalles(self,numero,sesion):
        return sesion.query(DetalleRemito).filter(DetalleRemito.id_remito==numero, DetalleRemito.baja==False)

    @classmethod
    def existeRemito(cls,numero,sesion):
        query=sesion.query(Remito).filter(Remito.numero==numero,Remito.baja==False)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def obtenerNumero(cls,sesion):
        return sesion.query(cls).count()+1

    @classmethod
    def getDetalle(cls,remito,linea,sesion):
        return sesion.query(DetalleRemito).filter(DetalleRemito.id_remito==remito,
                                                  DetalleRemito.nro_linea==linea)
    @classmethod
    def obtenerTodosRemitos(cls,sesion):
        return sesion.query(cls).filter(cls.anulado==False).filter(cls.baja==False)

class DetalleRemito(ObjetoBase):
    def __init__(self,id_remito,nro_linea,producto,cantidad):
        ObjetoBase.__init__(self)
        self.id_remito=id_remito
        self.nro_linea=nro_linea
        self.producto=producto
        self.cantidad=cantidad

    def getIdRemito(self):
        return self.id_remito

    def subTotal(self,sesion):
        query=sesion.query(Producto).filter(Producto.codigoBarra==self.producto)
        print (query.importe)

class Factura(ObjetoBase):
    def __init__(self,numero):
        self.numero=numero
        self.fecha_emision=date.today()
        self.anulado=False
        self.nota_credito=None

    def getFechaEmision(self):
        return self.fecha_emision

    def getDetalles(self,sesion):
        return sesion.query(DetalleFactura).filter(DetalleFactura.id_factura==self.numero)

    def anular(self):
        self.anulado=True

    def setNC(self,nota):
        self.nota_credito=nota

    def getNC(self):
        return self.nota_credito

    def getFechaEmision(self):
        return self.fecha_emision

    @classmethod
    def buscarDetalles(self,numero,sesion):
        return sesion.query(DetalleFactura).filter(DetalleFactura.id_factura==numero)

    @classmethod
    def existeFactura(cls,numero,sesion):
        query=sesion.query(Factura).filter(Factura.numero==numero)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def generarNumero(cls,sesion):
        return sesion.query(cls).count()+1

class DetalleFactura(ObjetoBase):

    def __init__(self,id_factura,producto,cantidad,importe, descuento, nro_linea):
        self.id_factura=id_factura
        #TODO Resolver el problema de la enumeracion de la linea
        self.producto=producto
        self.cantidad=cantidad
        self.descuento=descuento
        self.importe=importe
        self.nro_linea=nro_linea

    def getDescuento(self):
        return self.descuento

    def getIdFactura(self):
        return self.id_factura

    def subTotal(self,sesion):
        query=sesion.query(Producto).filter(Producto.codigoBarra==self.producto)
        return query.importe*self.cantidad

class NotaCredito(ObjetoBase):

    def __init__(self,numero):
        self.numero=numero
        self.fecha_emision=date.today()
        self.anulado=False

    def getDetalles(self,sesion):
        pass

    def anular(self):
        self.anulado = True

    def getTotal(self,sesion):
        query = sesion.query(DetalleNotaCredito).filter(DetalleNotaCredito.nro_nota == self.numero)
        total = 0
        for value in query:
            total += value.importe
        return total

    @classmethod
    def generarNumero(cls,sesion):
        return sesion.query(cls).count()+1

    def getDetalle(cls,nota,linea,sesion):
        return sesion.query(DetalleNotaCredito).filter(DetalleNotaCredito.nro_nota==nota,
                                                       DetalleNotaCredito.nro_linea==linea)

    @classmethod
    def getNotaCredito(cls,sesion,numero):
        return sesion.query(NotaCredito).filter(NotaCredito.numero == numero).first()


class DetalleNotaCredito(ObjetoBase):

    def __init__(self,nro_nota,nro_linea,nro_factura,linea_factura):
        self.nro_nota=nro_nota
        self.nro_linea=nro_linea
        self.nro_factura=nro_factura
        self.linea_factura=linea_factura
        self.importe=0
        self.descuento=0

    def setImporte(self,importe):
        self.importe=importe

    def setDescuento(self,descuento):
        self.descuento=descuento

class CobroCliente(ObjetoBase):

    def __init__(self,numero,factura,tipo,importe):
        self.numero=numero
        self.id_factura=factura
        self.tipo=tipo
        self.importe=importe
        self.nota_credito=None

    def setNC(self,nro_nota):
        self.nota_credito=nro_nota

    @classmethod
    def obtenerNumero(cls,sesion):
        return sesion.query(cls).count()+1

    @classmethod
    def getTotalNC(cls,sesion,notac):
        """
            Retorna el total de todas las facturas
            abonadas con el numero de Nota de Credito
            pasado como parametro
        :param sesion:
        :param notac:
        :return:
        """
        query = sesion.query(CobroCliente).filter(CobroCliente.nota_credito == notac)
        total = 0
        for value in query:
            total += value.importe

        return total


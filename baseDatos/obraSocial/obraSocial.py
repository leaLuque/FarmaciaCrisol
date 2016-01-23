from datetime import date
from baseDatos.productos import ObjetoBase
#TODO Cambiar la ubicacion de la referencia al objeto base

class ObraSocial(ObjetoBase):

    def __init__(self,razon_social,cuit,direccion):
        self.razon_social=razon_social
        self.cuit=cuit
        self.direccion=direccion

    def getDescuento(self,producto,sesion):
        query=sesion.query(Descuento).filter(Descuento.obra_social==self.razon_social).filter(Descuento.producto==producto)
        if query.count()==0:
            return 0
        else:
            for a in query:
                return a.descuento

    @classmethod
    def getObraSocial(cls,obra,sesion):
        query=sesion.query(ObraSocial).filter(ObraSocial.razon_social==obra)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

class Descuento(ObjetoBase):
    def __init__(self,producto,obra_social,descuento):
        self.producto=producto
        self.obra_social=obra_social
        self.descuento=descuento


class FacturaLiquidacion(ObjetoBase):
    def __init__(self,numero, nro_factura):
        ObjetoBase.__init__(self)
        self.numero=numero
        self.fecha_emision=date.today()
        self.nro_factura = nro_factura

    def getNumero(self):
        return self.numero

    # def getFechaEmision(self):
    #     return self.fecha_emision
    #
    # def getDetalles(self,sesion):
    #     return sesion.query(DetalleFacturaLiquidacion).filter(DetalleFacturaLiquidacion.id_factura==self.numero)
    #
    # def anular(self):
    #     self.anulado=True
    #
    # @classmethod
    # def buscarDetalles(self,numero,sesion):
    #     return sesion.query(DetalleFacturaLiquidacion).filter(DetalleFacturaLiquidacion.id_factura==numero)
    #
    # @classmethod
    # def existeFactura(cls,numero,sesion):
    #     query=sesion.query(FacturaLiquidacion).filter(FacturaLiquidacion.numero==numero)
    #     if query.count()==0:
    #         return None
    #     else:
    #         for a in query:
    #             return a
    #
    # @classmethod
    # def generarNumero(cls,sesion):
    #     return sesion.query(cls).count()+1

class CobroObraSocial(ObjetoBase):
    def __init__(self,numero,cheque_deposito,importe, id_factura_liquidacion):
        ObjetoBase.__init__(self)
        self.numero=numero
        self.fecha_emision=date.today()
        self.cheque_deposito = cheque_deposito
        self.importe=importe
        self.id_factura_liquidacion=id_factura_liquidacion

    def getIdFacturaLiquidacion(self):
        return self.id_factura_liquidacion
from datetime import date
from baseDatos.productos import ObjetoBase

class ObraSocial(ObjetoBase):
    """
        Clase que modela a la Obra Social
    """

    def __init__(self,razon_social,cuit,direccion):
        """
            Constructor de la clase ObraSocial
        :param razon_social Nombre de la Obra Social:
        :param cuit Cuit de la Obra Social:
        :param direccion Dirección de la Obra Social:
        """
        self.razon_social=razon_social
        self.cuit=cuit
        self.direccion=direccion

    def getDescuento(self,producto,sesion):
        """
            Devuelve el descuento para el producto seleccionado
        :param producto Id_Producto:
        :param sesion Sesion actual con la Base de Datos:
        :return Descuento:
        """
        query=sesion.query(Descuento).filter(Descuento.obra_social==self.razon_social).filter(Descuento.producto==producto)
        if query.count()==0:
            return 0
        else:
            for a in query:
                return a.descuento

    @classmethod
    def getObraSocial(cls,obra,sesion):
        """
            Devuelve la Obra Social
        :param obra Razón social
        :param sesion Sesión actual con la Base de Datos:
        :return Objecto de tipo Obra Social:
        """
        query=sesion.query(ObraSocial).filter(ObraSocial.razon_social==obra)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

class Descuento(ObjetoBase):
    """
        Clase que modela el Descuento de Obra Social
    """
    def __init__(self,producto,obra_social,descuento):
        """
            Constructor de la clase Descuento
        :param producto Id_Producto:
        :param obra_social Razón social de la OS:
        :param descuento Descuento de la OS:
        """
        self.producto=producto
        self.obra_social=obra_social
        self.descuento=descuento


class FacturaLiquidacion(ObjetoBase):
    """
        Clase que modela la Factura de Liquidacion
    """
    def __init__(self,numero, nro_factura):
        """
            Constructor de la clase FacturaLiquidacion
        :param numero Número de factura de liquidación:
        :param nro_factura Número de factura:
        :return:
        """
        ObjetoBase.__init__(self)
        self.numero=numero
        self.fecha_emision=date.today()
        self.nro_factura = nro_factura

    def getNumero(self):
        """
            Devuelve el número de la factura de liquidación
        :return Id_FacturaLiquidación
        """
        return self.numero

class CobroObraSocial(ObjetoBase):
    """
        Clase que modela el cobro a la Obra Social
    """
    def __init__(self,numero,cheque_deposito,importe, id_factura_liquidacion):
        """
            Constructor de la clase CobroObraSocial
        :param numero:
        :param cheque_deposito:
        :param importe:
        :param id_factura_liquidacion:
        :return:
        """
        ObjetoBase.__init__(self)
        self.numero=numero
        self.fecha_emision=date.today()
        self.cheque_deposito = cheque_deposito
        self.importe=importe
        self.id_factura_liquidacion=id_factura_liquidacion

    def getIdFacturaLiquidacion(self):
        """
            Devuelve el id de la Factura Liquidada
        :return Id_Factura:
        """
        return self.id_factura_liquidacion
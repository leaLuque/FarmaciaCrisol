# -*- coding:utf-8 -*-
__author__ = "leandro"

from datetime import date

from baseDatos.productos import ObjetoBase
from baseDatos.productos import Producto
from baseDatos.productos import LoteProducto
from baseDatos.obraSocial import FacturaLiquidacion


class Remito(ObjetoBase):
    """
        Clase que modela la logica del Remito
    """

    def __init__(self, numero,cliente):
        """
            Constructor de la clase Remito
        :param numero Numero de Remito:
        :param cliente DNI del cliente:
        :return:
        """
        ObjetoBase.__init__(self)
        self.numero = numero
        self.cliente = cliente
        self.fecha_emision = date.today()
        self.cobrado = None
        self.anulado = False

    def getAnulado(self):
        """
            Devuelve el valor del campo anulado.
        :return Anulado:
        :rtype Boolean:
        """
        return self.anulado

    def getFechaEmision(self):
        """
            Devuelve la fecha de emision del Remito
        :return Fecha de Emitsion:
        :rtype Datetime:
        """
        return self.fecha_emision

    def getCliente(self):
        """
            Devuelve el Dni del cliente asociado con
            el Remito
        :return DNI del cliente:
        :rtype Integer:
        """
        return self.cliente

    def getCobrado(self):
        """
            Devuelve si el Remito se encuentra
            cobrado o no
        :return True(cobrado) o False(no cobrado):
        :rtype Boolean:
        """
        if self.cobrado == None:
            return False
        else:
            return True

    def setCobrado(self,numeroFactura):
        """
            Indica como cobrado al Remito
        :param numeroFactura Numero de Factura asociada al Remito:
        :return:
        """
        self.cobrado=numeroFactura

    def anular(self):
        """
            Anula el Remito
        :return:
        """
        self.anulado=True

    @classmethod
    def getRemito(cls,numero,sesion):
        """
            Devuelve el Remito con el numero dado. Si no
            existe devuelve None
        :param numero Numero de Sesion:
        :param sesion Sesion actual con la Base de Datos:
        :return Remito:
        :rtype Objeto de Tipo Remito:
        """
        query=sesion.query(Remito).filter(Remito.numero==numero, Remito.baja==False)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def buscarDetalles(self,numero,sesion):
        """
            Devuelve los detalles asociados con el numero
            de remito provisto
        :param numero Numero de Remito:
        :param sesion Sesion actual con la Base de Datos:
        :return DetalleRemito:
        :rtype Objeto de DetalleRemito:
        """
        return sesion.query(DetalleRemito).filter(DetalleRemito.id_remito==numero, DetalleRemito.baja==False)

    @classmethod
    def existeRemito(cls,numero,sesion):
        """
            Indica si el numero de remito pasado como
            parametro, existe en el sistema
        :param numero:
        :param sesion:
        :return Remito:
        :rtype Objeto de tipo Remito:
        """
        query = sesion.query(Remito).filter(Remito.numero == numero,Remito.baja == False)
        if query.count() == 0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def obtenerNumero(cls,sesion):
        """
            Obtiene el siguiente numero de remito
        :param sesion:
        :return Numero de Remito:
        :rtype Integer:
        """
        return sesion.query(cls).count()+1

    @classmethod
    def getDetalle(cls,remito,linea,sesion):
        """
            Devuelve el detalle particular de un remito dado
        :param remito Numero de remito:
        :param linea Numero de linea del remito:
        :param sesion Sesion actual con la Base de Datos:
        :return :
        :rtype :
        """
        return sesion.query(DetalleRemito).filter(DetalleRemito.id_remito == remito,
                                                  DetalleRemito.nro_linea == linea,
                                                  DetalleRemito.baja == False).first()

    @classmethod
    def obtenerTodosRemitos(cls,sesion):
        """
            Obtiene todos los Remitos en el sistema
        :param sesion Sesion Actual con la Base de Datos:
        :return Remtiso actuales en el sistema:
        :rtype Coleccion de objetos tipo Remito:
        """
        return sesion.query(cls).filter(cls.anulado==False).filter(cls.baja==False)

class DetalleRemito(ObjetoBase):
    """
        Clase que modela la logica del Detalle de Remito
    """
    def __init__(self,id_remito,nro_linea,producto,cantidad):
        """
            Constructor de la Clase Detalle Remito
        :param id_remito:
        :param nro_linea:
        :param producto:
        :param cantidad:
        :return:
        """
        ObjetoBase.__init__(self)
        self.id_remito=id_remito
        self.nro_linea=nro_linea
        self.producto=producto
        self.cantidad=cantidad

    def getIdRemito(self):
        """
            Devuelve el numero de remito al cual
            pertenece el Detalles
        :return Numeo de Remito:
        :rtype Integer:
        """
        return self.id_remito

    def agregarLotes(self,sesion,lotes):
        """
            Agrega los lotes correspondientes en la conformacion
            de la cantidad del detalle
            :param sesion Sesion actual con la Base de Datos:
            :param lotes Diccionario que tiene el código de lote y la cantidad
            :return:
        """

        for lote in lotes:
            temp = LoteDetallado(self.id_remito,self.nro_linea,lote[0].id_lote,lote[1],True)
            temp.guardar(sesion)

    def devolverLotes(self,sesion):
        """
            Devuelve todos los lotes que conforman la cantidad
            del Detalle
            :param sesion Sesion actual con la Base de Datos
            :return Diccionario con los lotes y sus cantidades
        """

        query = sesion.query(LoteDetallado.lote,LoteDetallado.cantidad).filter(LoteDetallado.nro_detalle == self.id_remito).\
                            filter(LoteDetallado.linea_detalle == self.nro_linea).filter(LoteDetallado.es_remito == True).\
                            filter(LoteDetallado.baja == False)

        temp = {}

        for value in query:
            temp[value[0]] = value[1]

        return temp

    def eliminarLotesAsociados(self,sesion):
        """
            Elimina las entradas en el tabla LoteDetallado
            para el Detalle en Particular
        :param sesion Sesion actual con la Base de Datos:
        :return:
        """
        query = sesion.query(LoteDetallado).filter(LoteDetallado.nro_detalle == self.id_remito).\
                            filter(LoteDetallado.linea_detalle == self.nro_linea).filter(LoteDetallado.es_remito == True).\
                            filter(LoteDetallado.baja == False)

        for value in query:
            value.setBaja(True)
            value.modificar(sesion)

    def devolver(self,sesion):
        """
            Devuelve el detalle correspondiente
            :param sesion Sesion actual con la Base de Datos:
            :return:
        """
        lotes_detalle = self.devolverLotes(sesion)
        for lote in lotes_detalle:
            loteP = LoteProducto.buscarLoteProducto(sesion,self.producto,lote).first()
            loteP.aumentarCantidad(lotes_detalle[lote])
            loteP.modificar(sesion)
        self.eliminarLotesAsociados(sesion)
        self.borrar(sesion)

class Factura(ObjetoBase):
    """
        Clase que modela la lógica de Factura
    """
    def __init__(self,numero):
        """
            Constructor de la clase Factura
        :param numero Numero de la Factura:
        :return:
        """
        self.numero=numero
        self.fecha_emision=date.today()
        self.anulado=False
        self.nota_credito=None
        self.obra = None

    def setObra(self,obra):
        """
            Setea el valor de la obra
        :param obra Razón social de la obra:
        :return:
        """
        self.obra = obra

    def getObra(self):
        """
            Devuelve la obra asociada con la factura
        :return obra:
        """
        return self.obra

    def getFechaEmision(self):
        """
            Devuelve la fecha emision de la Factura
        :return Fecha de emision:
        :rtype Datetime:
        """
        return self.fecha_emision

    def getDetalles(self,sesion):
        """
            Devuelve los detalles correspondientes a una factura
        :param sesion Sesion actual con la Base de Datos:
        :return Coleccion de los detalles de Factura:
        :rtype Coleccion de objetos tipo DetalleFactura:
        """
        return sesion.query(DetalleFactura).filter(DetalleFactura.id_factura==self.numero)

    def getAnulado(self):
        """
            Devuelve el valor del campo anulado.
        :param sesion Sesion actual con la Base de Datos:
        :return Anulado:
        :rtype Boolean:
        """
        return self.anulado

    def anular(self):
        """
            Anula la factura
        :return:
        """
        self.anulado=True

    def setNC(self,nota):
        """
            Establece el numero de Nota de Credito
            a la Factura
        :param nota Numero de Nota de Crédito:
        :return:
        """
        self.nota_credito=nota

    def getNC(self):
        """
            Devuelve la Nota de Crédito asociada
            con la factura
        :return Numero de la Nota de Crédito:
        :rtype Integer:
        """
        return self.nota_credito

    def getCobros(self,sesion):
        """
            Devuelve los cobros asociados a una factura
        :param sesion Sesion actual con la Base de Datos:
        :return:
        """
        query = CobroCliente.buscar(CobroCliente.id_factura,sesion,self.numero)
        temp = []
        for valor in query:
            temp.append(valor)
        return temp

    def estaLiquidada(self,sesion):
        """
            Indica si la factura se encuentra vinculada a
            una factura de liquidacion a obra social
        :param sesion Sesion actual con la Base de Datos:
        :return Boolean:
        """
        query = FacturaLiquidacion.buscarAlta(FacturaLiquidacion.nro_factura,sesion,self.numero)
        if query == None:
            return False
        else:
            return True

    @classmethod
    def existeFactura(cls,numero,sesion):
        """
            Indica si una determinada factura existe o no. Si existe
            devuelve la Factura en cuestion, sino None.
        :param numero Número de Factura:
        :param sesion Sesion actual con la Base de Datos:
        :return Factura:
        :rtype Objeto de tipo Factura:
        """
        query=sesion.query(Factura).filter(Factura.numero == numero).filter(Factura.anulado == False)
        if query.count()==0:
            return None
        else:
            for a in query:
                return a

    @classmethod
    def generarNumero(cls,sesion):
        """
            Genera el numero de la Factura
        :param sesion Sesion actual con la Base de Datos:
        :return Número de Factura:
        :rtype Integer:
        """
        return sesion.query(cls).count()+1

    @classmethod
    def getDetalle(cls,factura,linea,sesion):
        """
            Devuelve el detalle particular de una factura dada
        :param remito Numero de factura:
        :param linea Numero de linea de la factura:
        :param sesion Sesion actual con la Base de Datos:
        :return :
        :rtype :
        """
        return sesion.query(DetalleFactura).filter(DetalleFactura.id_factura == factura,
                                                  DetalleFactura.nro_linea == linea,
                                                  DetalleFactura.baja == False).first()

class DetalleFactura(ObjetoBase):
    """
        Clase que modela la logica del Detalle de Factura
    """

    def __init__(self,id_factura,producto,cantidad,importe, descuento, nro_linea):
        """
            Constructor de la clase DetalleFactura
        :param id_factura Numero de factura:
        :param producto Código de barra del producto:
        :param cantidad Cantidad de Producto:
        :param importe Importe Unitario de Producto:
        :param descuento Descuento de Producto:
        :param nro_linea Núḿero de linea del Detalle:
        :return:
        """
        self.id_factura=id_factura
        self.producto = producto
        self.cantidad = cantidad
        self.descuento = descuento
        self.importe = importe
        self.nro_linea = nro_linea

    def getDescuento(self):
        """
            Devuelve el descuento asociado con el detalle
        :return Descuento del Detalle:
        :rtype Float
        """
        return self.descuento

    def getIdFactura(self):
        """
            Devuelve el numero de factura asociado con
            el detalle
        :return NUmero de Factura del Detalle:
        :rtype Integer:
        """
        return self.id_factura

    def agregarLotes(self,sesion,lotes):
        """
            Agrega los lotes correspondientes en la conformacion
            de la cantidad del detalle
            :param sesion Sesion actual con la Base de Datos:
            :param lotes Diccionario que tiene el código de lote y la cantidad
            :return:
        """

        for lote in lotes:
            temp = LoteDetallado(self.id_factura,self.nro_linea,lote[0].id_lote,lote[1],False)
            temp.guardar(sesion)

    def devolverLotes(self,sesion):
        """
            Devuelve todos los lotes que conforman la cantidad
            del Detalle
            :param sesion Sesion actual con la Base de Datos
            :return Diccionario con los lotes y sus cantidades
        """

        query = sesion.query(LoteDetallado.lote,LoteDetallado.cantidad).filter(LoteDetallado.nro_detalle == self.id_factura).\
                            filter(LoteDetallado.linea_detalle == self.nro_linea).filter(LoteDetallado.es_remito == False).\
                            filter(LoteDetallado.baja == False)

        temp = {}

        for value in query:
            temp[value[0]] = value[1]

        return temp

    def eliminarLotesAsociados(self,sesion):
        """
            Elimina las entradas en el tabla LoteDetallado
            para el Detalle en Particular
        :param sesion Sesion actual con la Base de Datos:
        :return:
        """
        query = sesion.query(LoteDetallado).filter(LoteDetallado.nro_detalle == self.id_factura).\
                            filter(LoteDetallado.linea_detalle == self.nro_linea).filter(LoteDetallado.es_remito == False).\
                            filter(LoteDetallado.baja == False)

        for value in query:
            value.setBaja(True)
            value.modificar(sesion)

    def devolver(self,sesion):
        """
            Devuelve el detalle correspondiente
            :param sesion Sesion actual con la Base de Datos:
            :return:
        """
        lotes_detalle = self.devolverLotes(sesion)
        for lote in lotes_detalle:
            loteP = LoteProducto.buscarLoteProducto(sesion,self.producto,lote).first()
            loteP.aumentarCantidad(lotes_detalle[lote])
            loteP.modificar(sesion)
        self.eliminarLotesAsociados(sesion)
        self.borrar(sesion)


class NotaCredito(ObjetoBase):
    """
        Clase que modela la lógica de la Nota de Crédito
    """

    def __init__(self,numero):
        """
            Constructor de la clase Nota de Crédito
        :param numero Número de la Nota de Crédito:
        :return:
        """
        self.numero=numero
        self.fecha_emision=date.today()
        self.anulado=False

    def anular(self):
        """
            Anula la Nota de Crédito
        """
        self.anulado = True

    def getTotal(self,sesion):
        """
            Devuelve el total de la Nota de Crédito
        :param sesion Sesion actual con la Base de Datos:
        :return Total de la Nota de Crédito:
        :rtype Float:
        """
        query = sesion.query(DetalleNotaCredito).filter(DetalleNotaCredito.nro_nota == self.numero)
        total = 0
        for value in query:
            total += value.importe
        return total

    @classmethod
    def generarNumero(cls,sesion):
        """
            Genera el número de la Nota de Crédito
        :param sesion Sesion actual con la Base de Datos:
        :return Número actual de la Nota de Crédito:
        :rtype Integer:
        """
        return sesion.query(cls).count()+1

    @classmethod
    def getNotaCredito(cls,sesion,numero):
        """
            Devuelve una Nota de Crédito particular
        :param sesion Sesion actual con la Base de Datos:
        :param numero Número de la Nota de Crédito:
        :return Nota de Crédito:
        :rtype Objeto de tipo NotaCrédito
        """
        return sesion.query(NotaCredito).filter(NotaCredito.numero == numero).first()

class DetalleNotaCredito(ObjetoBase):
    """
        Clase que modela la lógica del Detalle de la Nota de Crédito
    """
    def __init__(self,nro_nota,nro_linea,nro_factura,linea_factura):
        """
            Constructor de la clase DetalleNotaCredito
        :param nro_nota Número de la Nota de Crédito:
        :param nro_linea Número de la linea del Detalles:
        :param nro_factura Número de la Factura:
        :param linea_factura Número de la linea del Detalle de Factura:
        :return:
        """
        self.nro_nota=nro_nota
        self.nro_linea=nro_linea
        self.nro_factura=nro_factura
        self.linea_factura=linea_factura
        self.importe=0
        self.descuento=0

    def setImporte(self,importe):
        """
            Establece el valor del importe del Detalle de
            la Nota de Crédito
        :param importe Valor de Importe:
        :return:
        """
        self.importe=importe

    def setDescuento(self,descuento):
        """
            Establece el valor del descuento del Detalle de
            la Nota de Crédito
        :param descuento Valor de Descuento:
        :return:
        """
        self.descuento=descuento

class CobroCliente(ObjetoBase):
    """
        Clase que modela la logica del Cobro al Cliente
    """

    def __init__(self,numero,factura,tipo,importe):
        """
            Constructor de la clase CobroCliente
        :param numero Número de cobro:
        :param factura Número de factura:
        :param tipo Tipo de Cobro:
        :param importe Importe cobrado:
        :return:
        """
        self.numero=numero
        self.id_factura=factura
        self.tipo=tipo
        self.importe=importe
        self.nota_credito=None

    def setNC(self,nro_nota):
        """
            Establece el número de nota de crédito
            asociado con el cobro.
        :param nro_nota Número de Nota de Crédito:
        :return:
        """
        self.nota_credito=nro_nota

    @classmethod
    def obtenerNumero(cls,sesion):
        """
            Obtiene el numero actual del cobro
            a emplear.
        :param sesion Sesion actual con la Base de Datos:
        :return Número de cobro:
        :rtype Integer:
        """
        return sesion.query(cls).count()+1

    @classmethod
    def getTotalNC(cls,sesion,notac):
        """
            Retorna el total de todas las facturas
            abonadas con el numero de Nota de Credito
            pasado como parametro
        :param sesion Sesion actual con la Base de Datos:
        :param notac Numero de la Nota de Credito:
        :return Total de la Nota de Crédito:
        :rtype Integer:
        """
        query = sesion.query(CobroCliente).filter(CobroCliente.nota_credito == notac)
        total = 0
        for value in query:
            total += value.importe

        return total

class LoteDetallado(ObjetoBase):
    """
        Clase que modela la logica de los lotes que pertenecen
        a un detalle de venta remito o venta contado
    """

    def __init__(self,nro_detalle,linea_detalle,lote,cantidad,es_remito):
        """
            Constructor de la clase LoteDetallado
        :param nro_detalle:
        :param linea_detalle:
        :param lote:
        :param cantidad:
        :param es_remito:
        :return:
        """
        self.nro_detalle = nro_detalle
        self.linea_detalle = linea_detalle
        self.lote = lote
        self.cantidad = cantidad
        self.es_remito = es_remito
        self.baja = False
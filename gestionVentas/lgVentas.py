# -*- coding:utf-8 -*-
__author__ = 'leandro'


from datetime import *

from PyQt4 import QtGui

from baseDatos.ventas.venta import NotaCredito
from gui import CRUDWidget,MdiWidget
from ventanas import Ui_vtnDevolucionDeCliente, Ui_vtnReintegroCliente, Ui_vtnVentaContado
from baseDatos.obraSocial import ObraSocial as ObraSocialModel
from baseDatos.productos import Producto as ProductoModel
from baseDatos.productos import Medicamento as MedicamentoModel
from baseDatos.productos import Monodroga as MonodrogaModel
from baseDatos.obraSocial import Descuento as DescuentoModel
from baseDatos.productos import Lote as LoteModel
from baseDatos.productos import LoteProducto as LoteProductoModel
from baseDatos.ventas import Factura as FacturaModel
from baseDatos.ventas import DetalleFactura as DetalleFacturaModel
from baseDatos.ventas import NotaCredito as NotaCreditoModel
from baseDatos.ventas import DetalleNotaCredito as DetalleNCModel
from baseDatos.ventas import CobroCliente as CobroClienteModel
from genComprobantes import generarNotaCredito,generarFactura



class DevolucionDeCliente(CRUDWidget, Ui_vtnDevolucionDeCliente):

    """
        Clase encargada de modelar la funcionalidad de Devolucion al Cliente

    """

    def __init__(self,mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.btnBuscar.pressed.connect(self.buscarFactura)
        self.tableFactura.doubleClicked.connect(self.devolverDetalle)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.lineNumero.returnPressed.connect(self.buscarFactura)
        self.facturaSeleccionada = None
        self.notaCredito = None
        self.productosSeleccionados = 0
        self.lotesDevueltos = {}
        self.data = []

    def validadores(self):
        pass

    def buscarFactura(self):
        """
            Busca y carga los detalles correspondientes
            al Nro de Factura ingresado.
        :return:
        """
        if not self.lineNumero.isEnabled():
            self.lineNumero.setEnabled(True)
            self.lineNumero.clear()
            self.limpiarTabla(self.tableFactura)
        else:
            self.numeroFacturaActual=str(self.lineNumero.text())
            if len(self.numeroFacturaActual)==0:
                self.showMsjEstado("No se ha ingresado numero de factura")
            else:
                self.facturaSeleccionada=FacturaModel.existeFactura(int(self.numeroFacturaActual),self.sesion)
                if self.facturaSeleccionada==None:
                    QtGui.QMessageBox.warning(self,"Aviso","La factura seleccionada no existe")
                else:
                    #TODO CARGAR SOLO LOS DETALLES DE FACTURA QUE NO ESTAN UNA NOTA DE CREDITO
                    if self.facturaSeleccionada.getNC()!=None:
                        QtGui.QMessageBox.information(self,"Aviso","La factura ya ha sido devuelta")
                    else:
                        self.lineNumero.setEnabled(False)
                        self.cargarObjetos(self.tableFactura,self.facturaSeleccionada.getDetalles(self.sesion),
                        ["producto","cantidad","importe"])

    def obtenerValoresItem(self,row):
        """
            Obtiene los valores de una fila de
            la Tabla de Detalles de Factura
        :param row Numero de Fila:
        :return Arreglo con valores de la fila:
        """
        values=[]
        for col in range(0,self.tableFactura.columnCount()):
            values.append(self.tableFactura.item(row,col).text())
        return values

    def obtenerNumeroLinea(self,value):
        """
            Busca el numero de linea correspondiente al
            producto seleccionado
        :param value Numero del producto seleccionado:
        :return Numero de Linea de Factura del producto:
        """
        query=self.facturaSeleccionada.getDetalles(self.sesion).\
            filter(DetalleFacturaModel.id_factura==self.numeroFacturaActual,DetalleFacturaModel.producto==value)
        for a in query:
            return a.nro_linea

    def armarItem(self,item,cantidad, nroLineaNC):
        """
            Genera y guarda el Detalle de la Nota de Credito
            correspondiente a una devolucion
        :param item Arreglo con informacion del Detalle de Factura:
        :param cantidad Cantidad Devuelta:
        :param nroLineaNC Nro de Linea en la Nota de Credito:
        :return:
        """
        linea_factura=self.obtenerNumeroLinea(str(item[0]))
        row=self.tableNC.rowCount()
        self.tableNC.insertRow(row)
        for col, elemento in enumerate(item):
            self.tableNC.setItem(row,col,QtGui.QTableWidgetItem(item[col]))
        self.tableNC.item(row,1).setText(str(cantidad))
        detalleNC=DetalleNCModel(self.notaCredito.numero,nroLineaNC,self.facturaSeleccionada.numero,linea_factura)
        detalleNC.guardar(self.sesion)

        self.data.append([str(item[0]),cantidad,0,float(item[2])])

    def devolverDetalle(self):
        """
            Incorpora el Detalle de Factura seleccionado
            por el usuario a la Nota de Credito
        :return:
        """
        itemActual=self.tableFactura.currentItem()
        ok=QtGui.QMessageBox.information(self,"Confirmacion","¿Desea devolver este detalle?")
        if ok:
            producto=int(self.tableFactura.item(itemActual.row(),0).text())
            cantOriginal=cantidadFactura=int(self.tableFactura.item(itemActual.row(),1).text())
            finalizeActualizacion=False
            if self.productosSeleccionados==0:
                self.notaCredito=NotaCreditoModel(NotaCreditoModel.generarNumero(self.sesion))
                self.notaCredito.guardar(self.sesion)
            while not finalizeActualizacion:
                cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
                if not ok:
                    QtGui.QMessageBox.information(self,"Aviso","No se ingreso cantidad")
                else:
                    if cantidad > cantidadFactura:
                        QtGui.QMessageBox.information(self,"Aviso","La cantidad ingresada supera la esperada")
                    else:
                        lote, ok=QtGui.QInputDialog.getText(self,"Lote","Ingrese lote")
                        if not ok:
                            QtGui.QMessageBox.information(self,"Aviso","No se ingreso lote")
                        else:
                            loteP=LoteProductoModel.buscarLoteProducto(self.sesion,producto,str(lote)).first()
                            if loteP==None:
                                QtGui.QMessageBox.information(self,"Aviso","El lote ingresado no se corresponde con el producto")
                            else:
                                loteP.aumentarCantidad(cantidad)
                                loteP.modificar(self.sesion)
                                self.lotesDevueltos[loteP]=cantidad
                                cantidadFactura-=cantidad
                                self.tableFactura.item(itemActual.row(),1).setText(str(cantidadFactura))
                                if cantidadFactura==0:
                                    finalizeActualizacion=True
                                    self.productosSeleccionados+=1
            self.armarItem(self.obtenerValoresItem(itemActual.row()),cantOriginal,self.productosSeleccionados)
            self.tableFactura.removeRow(itemActual.row())
        else:
            return

    def limpiarVentana(self):
        """
            Limpia los componentes de la ventana
        :return:
        """
        self.limpiarTabla(self.tableFactura)
        self.lineNumero.setEnabled(True)
        self.lineNumero.clear()
        self.limpiarTabla(self.tableNC)

    def calcularTotal(self):
        """
            Calculo el total a devolver en la
            Nota de Credito
        :return Total a Devolver:
        """
        subtotales=[]
        for row in range(0,self.tableNC.rowCount()):
            subtotales.append(float(self.tableNC.item(row,2).text()))
        return sum(subtotales)

    def confirmarOperacion(self):
        """
            Imprime la Nota de Credito, una vez que el
            usuario confirmo la operacion.
        :return:
        """
        self.productosSeleccionados=0
        if self.notaCredito!=None:
            self.facturaSeleccionada.setNC(self.notaCredito.numero)
            self.facturaSeleccionada.modificar(self.sesion)
            cobroC=CobroClienteModel.buscar(CobroClienteModel.id_factura,self.sesion,self.facturaSeleccionada.numero).first()
            if cobroC.tipo=="Efectivo":
                QtGui.QMessageBox.information(self,"Devolucion","El importe en efectivo a entregar es de: $%.2f" % self.calcularTotal())
            QtGui.QMessageBox.information(self,"Devolucion Cliente","La devolucion ha sido exitosa")

            #Se genera un diccionario con los datos necesarios para imprimir la nota de credito
            data = {}
            data["numero"] = self.notaCredito.numero
            data["fecha"] = self.notaCredito.fecha_emision
            data["detalles"] = self.data
            generarNotaCredito(data)

            self.notaCredito=None
            self.facturaSeleccionada=None
            self.productosSeleccionados=0

        else:
            QtGui.QMessageBox.information(self,"Devolucion Cliente","No se ha efectuado ninguna devolucion")

        self.limpiarVentana()
        self.data = []

    def cancelarOperacion(self):
        """
            Anula la Nota de Credito creada, actuliza el stock
            de los productos a sus valores originales y limpia la ventana.
            Si la Nota de Credito no fue creada limpia la ventana.
            :return:
        """
        self.productosSeleccionados=0
        if self.notaCredito!=None:
            ok=QtGui.QMessageBox.warning(self,"Advertencia","Ya se ha efectuado una nota de credito. ¿Desea Anularla?")
            if ok:
                for lote in self.lotesDevueltos:
                    lote.descontarCantidad(self.lotesDevueltos[lote])
                    lote.modificar(self.sesion)
                    self.notaCredito.anular()
                    self.notaCredito.modificar(self.sesion)
                self.limpiarVentana()
                self.lotesDevueltos={}
                QtGui.QMessageBox.information(self,"Devolucion Cliente","La nota de credito ha sido anulada")
        else:
            self.limpiarVentana()

class ReintegroCliente(CRUDWidget, Ui_vtnReintegroCliente):

    """
    Clase encargada de modelar la funcionalidad de Reintegro al cliente

    """

    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.cargarObras()
        self.btnBuscarOs.pressed.connect(self.buscarOs)
        self.tableOs.itemDoubleClicked.connect(self.obtenerObra)
        self.btnBuscarFac.pressed.connect(self.buscarFactura)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.tableFactura.itemDoubleClicked.connect(self.agregarProducto)
        self.detallesReintegrables = []
        self.detallesImprimibles = []

    def cargarObras(self):
        """
            Carga las Obras Sociales disponibles
            en la tabla correspondiente
        :return:
        """
        self.cargarObjetos(self.tableOs,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def buscarOs(self):
        """
            Busca una Obra Social de acuerdo
            a los criterios del usuario
        :return:
        """
        if self.lineRazon.isEnabled():
            print("buscar por filtrado")
        else:
            self.lineRazon.clear()
            self.lineRazon.setEnabled(True)
            self.lineCuit.clear()
            self.lineCuit.setEnabled(True)
            self.tableOs.setEnabled(True)

    def obtenerObra(self):
        """
            Carga la Obra Social seleccionada
            en los campos correspondientes.
        :return:
        """
        rowActual = self.tableOs.currentItem().row()
        self.lineRazon.setText(str(self.tableOs.item(rowActual,0).text()))
        self.lineRazon.setEnabled(False)
        self.obraSocial=str(self.tableOs.item(rowActual,0).text())
        self.lineCuit.setText(str(self.tableOs.item(rowActual,1).text()))
        self.lineCuit.setEnabled(False)
        self.tableOs.setEnabled(False)

    def buscarFactura(self):
        """
            Busca la factura indica por el usuario.
            En caso de no existir, notifica lo mismo
        :return:
        """
        if not self.lineNumeroFac.isEnabled():
            self.lineNumeroFac.setEnabled(True)
            self.lineNumeroFac.clear()
            self.limpiarTabla(self.tableFactura)
        else:
            print "hola"
            self.numeroFacturaActual=str(self.lineNumeroFac.text())
            if len(self.numeroFacturaActual)==0:
                self.showMsjEstado("No se ha ingresado numero de factura")
            else:
                self.facturaSeleccionada=FacturaModel.existeFactura(int(self.numeroFacturaActual),self.sesion)
                if self.facturaSeleccionada==None:
                    QtGui.QMessageBox.information(self,"Aviso","La factura seleccionada no existe")
                else:
                    #TODO CORREGIR LA PARTE DE LAS FECHAS
                    if self.facturaSeleccionada.getFechaEmision()+timedelta(days=7)<date.today():
                        #TODO CHEQUEAR ESTA PARTE PORQUE HAY DUDAS
                        #QtGui.QMessageBox.information(self,"Aviso","El tiempo permitido para el reintegro ha expirado")
                        pass

                    else:
                        self.lineNumeroFac.setEnabled(False)
                        self.cargarObjetos(self.tableFactura,self.facturaSeleccionada.getDetalles(self.sesion),
                            ["producto","cantidad","importe"])

    def agregarProducto(self):
        """
            Agrega un producto a la Nota de Credito
        :return:
        """
        itemActual=self.tableFactura.currentItem()
        producto = int(self.tableFactura.item(itemActual.row(),0).text())
        descuento = DescuentoModel.buscar(DescuentoModel.obra_social,self.sesion,self.obraSocial).\
                        filter(DescuentoModel.producto==producto)[0].descuento
        cantidad = int(self.tableFactura.item(itemActual.row(), 1).text())
        importe = float(self.tableFactura.item(itemActual.row(), 2).text()) - \
                    float(self.tableFactura.item(itemActual.row(), 2).text())*descuento
        medio = float(self.tableFactura.item(itemActual.row(),2).text())- importe
        importeEfectivo = float("%.2f" % (medio))
        row = self.tableNC.rowCount()
        self.tableNC.insertRow(row)
        self.tableNC.setItem(row, 0, QtGui.QTableWidgetItem(str(producto)))
        self.tableNC.setItem(row, 1, QtGui.QTableWidgetItem(str(cantidad)))
        self.tableNC.setItem(row, 2, QtGui.QTableWidgetItem(str(importeEfectivo)))
        self.detallesReintegrables.append([int(self.numeroFacturaActual),itemActual.row()+1,descuento,importeEfectivo])
        self.detallesImprimibles.append([producto,cantidad,descuento,importe])
        self.tableFactura.hideRow(itemActual.row())

    def confirmarOperacion(self):
        """
            Confirma la operacion y asienta los datos de la
            Nota de Credito en la BD.
        :return:
        """

        ok = QtGui.QMessageBox.information(self,"Confirmacion","¿Desea generar la Nota Crédito?",\
                                           QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Accepted)

        if (ok==1):
            notaCredito = NotaCreditoModel(NotaCredito.generarNumero(self.sesion))
            notaCredito.guardar(self.sesion)
            for lineaNC, data in enumerate(self.detallesReintegrables):
                detalleNC = DetalleNCModel(notaCredito.numero, lineaNC+1, data[0], data[1])
                detalleNC.setImporte(data[3])
                detalleNC.setDescuento(data[2])
                detalleNC.guardar(self.sesion)
            QtGui.QMessageBox.information(self,"Aviso","La Nota de Credito ha sido generada con exito")

            #Se genera un diccionario con los datos necesarios para imprimir la nota de credito
            data = {}
            data["numero"] = notaCredito.numero
            data["fecha"] = notaCredito.fecha_emision
            data["detalles"] = self.detallesImprimibles
            generarNotaCredito(data)
        else:
            QtGui.QMessageBox.information(self,"Aviso","La Nota de Credito no ha sido generada")

        self.obraSocial = None
        self.detallesReintegrables = []
        self.detallesImprimibles = []
        self.limpiarVentana()

    def cancelarOperacion(self):
        """
            Cancela la operacion en curso y limpia la ventana
        :return:
        """

        ok = QtGui.QMessageBox.information(self,"Confirmacion","¿Desea cancelar la operacion?",\
                                           QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Accepted)
        if (ok==1):
            self.detallesReintegrables = []
            self.detallesImprimibles = []
            self.obraSocial = None
            self.limpiarVentana()

    def limpiarVentana(self):
        """
            Limpia la ventana una vez que la operacion finalizó
            :return:
        """
        self.limpiarTabla(self.tableFactura)
        self.limpiarTabla(self.tableNC)
        self.lineCuit.clear()
        self.lineRazon.clear()
        self.lineNumeroFac.clear()
        self.lineCuit.setEnabled(True)
        self.lineRazon.setEnabled(True)
        self.tableOs.setEnabled(True)
        self.lineNumeroFac.setEnabled(True)

class VentaContado(CRUDWidget, Ui_vtnVentaContado):

    """
        Clase encargada de modelar el comportamiento de Venta al Contado

    """

    def __init__(self,mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.cargar_obras()
        self.lineCuit.setEnabled(False)
        self.lineObra.setEnabled(False)
        self.lineMedicamento.returnPressed.connect(self.buscarXMedicamento)
        self.lineMonodroga.returnPressed.connect(self.buscarXMonodroga)
        self.btnBuscar.setEnabled(False)
        self.tableObra.setVisible(False)
        self.tableObra.itemDoubleClicked.connect(self.cargarObra)
        self.tableProductos.itemDoubleClicked.connect(self.agregarProducto)
        self.btnBuscar.pressed.connect(self.limpiarObra)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.rbtnObra.pressed.connect(self.habilitarObras)
        self.btnActualizar.pressed.connect(self.actualizar)
        self.productosAgregados=0
        self.lotesVentas={}
        self.facturaCobrada=False
        self.obraSocialSeleccionada=None
        self.factura = None
        self.data = []
        self.cargarProductosSinObra()


    def buscarXMonodroga(self):
        """
            Filtra los productos segun la
            Monodroga indicada por el usuario
        :return:
        """

        nombreMonodroga = str(self.lineMonodroga.text())
        if len(nombreMonodroga) == 0:
            if self.obraSocialSeleccionada == None:
                self.cargarProductosSinObra()
            else:
                self.cargar_productos(self.obraSocialSeleccionada)
        else:
            data = self.getContenidoTabla(self.tableProductos)
            data = filter(lambda x: x[3].upper() == nombreMonodroga.upper() , data)
            self.limpiarTabla(self.tableProductos)
            for row, value in enumerate(data):
                self.tableProductos.insertRow(row)
                for col in range(0,self.tableProductos.columnCount()):
                    self.tableProductos.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def buscarXMedicamento(self):
        """
            Filtra los productos segun el
            Medicamento indicada por el usuario
        :return:
        """

        nombreMedicamento= str(self.lineMedicamento.text())
        if len(nombreMedicamento) == 0:
            if self.obraSocialSeleccionada == None:
                self.cargarProductosSinObra()
            else:
                self.cargar_productos(self.obraSocialSeleccionada)
        else:
            data = self.getContenidoTabla(self.tableProductos)
            data = filter(lambda x: x[1].upper() == nombreMedicamento.upper() , data)
            self.limpiarTabla(self.tableProductos)
            for row, value in enumerate(data):
                self.tableProductos.insertRow(row)
                for col in range(0,self.tableProductos.columnCount()):
                    self.tableProductos.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def actualizar(self):
        """
            Actualiza la informacion de la
            tabla de Productos
        :return:
        """
        if self.obraSocialSeleccionada!=None:
            self.cargar_productos(self.obraSocialSeleccionada)
        else:
            self.cargarProductosSinObra()

    def habilitarObras(self):
        """
            Muestra las Obras Sociales si no hay una factura creada.
            Si la factura ya se encuentra creada, notifica que no
            es posible cambiar la Obra Social actual.
        :return:
        """
        if self.factura!=None:
            QtGui.QMessageBox.information(self,"Aviso","Ya existe una factura. "
                                                       "No se puede seleccionar otra obra social")
        else:
            if not self.rbtnObra.isChecked():
                self.btnBuscar.setEnabled(True)
                self.lineObra.setEnabled(True)
                self.lineCuit.setEnabled(True)
                self.tableObra.setVisible(True)
            else:
                self.lineObra.clear()
                self.lineCuit.clear()
                self.btnBuscar.setEnabled(False)
                self.lineObra.setEnabled(False)
                self.lineCuit.setEnabled(False)
                self.tableObra.setVisible(False)
                self.obraSocialSeleccionada=None
                self.cargarProductosSinObra()

    def cargarProductosSinObra(self):
        """
            Carga en la tabla de Productos todos los productos
            sin descuento de Obra Social
        :return:
        """

        self.limpiarTabla(self.tableProductos)

        ##Cnsulta para obtener todos los productos del sistema, con su correspondiente
        ##codigo de barra, monodroga, descuento, importe
        query=self.sesion.query(ProductoModel.codigo_barra,ProductoModel.id_medicamento,ProductoModel.id_presentacion,MonodrogaModel.nombre,ProductoModel.importe).\
            join(MedicamentoModel).filter(ProductoModel.id_medicamento==MedicamentoModel.nombre_comercial).\
            join(MonodrogaModel).filter(MedicamentoModel.id_monodroga==MonodrogaModel.nombre).\
            filter(ProductoModel.baja==False).order_by(ProductoModel.codigo_barra)

        ##Se cargan los datos obtenidos en la tabla de Producto
        for n, obj in enumerate(query):
            self.tableProductos.insertRow(n)
            self.tableProductos.setItem(n, 0, QtGui.QTableWidgetItem(str(obj[0])))
            self.tableProductos.setItem(n, 1, QtGui.QTableWidgetItem(str(obj[1])))
            self.tableProductos.setItem(n, 2, QtGui.QTableWidgetItem(str(obj[2])))
            self.tableProductos.setItem(n, 3, QtGui.QTableWidgetItem(str(obj[3])))
            self.tableProductos.setItem(n, 4, QtGui.QTableWidgetItem(str(0)))
            self.tableProductos.setItem(n, 5, QtGui.QTableWidgetItem(str(obj[4])))

        ##Se carga la cantidad de cada producto en la tabla
        for row,producto in enumerate(ProductoModel.buscarTodos(ProductoModel.codigo_barra,self.sesion)):
            self.tableProductos.setItem(row,6,QtGui.QTableWidgetItem(str(producto.getCantidad(self.sesion))))

    def cargar_productos(self, obraSocial):
        """
            Carga en la tabla de Productos todos los
            productos del sistema con los correspondientes descuentos
            de la Obra Social seleccionada
        :param obraSocial:
        :return:
        """
        self.limpiarTabla(self.tableProductos)

        query=self.sesion.query(ProductoModel.codigo_barra,ProductoModel.id_medicamento,ProductoModel.id_presentacion,MonodrogaModel.nombre,DescuentoModel.descuento,ProductoModel.importe).\
            join(MedicamentoModel).filter(ProductoModel.id_medicamento==MedicamentoModel.nombre_comercial).\
            join(MonodrogaModel).filter(MedicamentoModel.id_monodroga==MonodrogaModel.nombre).\
            join(DescuentoModel).filter(DescuentoModel.producto==ProductoModel.codigo_barra).\
            filter(DescuentoModel.obra_social==obraSocial,ProductoModel.baja==False).order_by(ProductoModel.codigo_barra)

        for n, obj in enumerate(query):
            self.tableProductos.insertRow(n)
            for m, campo in enumerate(obj):
                self.tableProductos.setItem(n, m, QtGui.QTableWidgetItem(str(campo)))

        for row,producto in enumerate(ProductoModel.buscarTodos(ProductoModel.codigo_barra,self.sesion)):
            self.tableProductos.setItem(row,6,QtGui.QTableWidgetItem(str(producto.getCantidad(self.sesion))))

    def cargarObra(self):
        """
            Carga la informacion de la Obra Social
            seleccionada por el usuario
        :return:
        """
        rowActual=self.tableObra.currentItem().row()
        self.lineObra.setText(str(self.tableObra.item(rowActual,0).text()))
        self.lineCuit.setText(str(self.tableObra.item(rowActual,1).text()))
        self.tableObra.hide()
        self.lineObra.setEnabled(False)
        self.lineCuit.setEnabled(False)
        self.obraSocialSeleccionada = str(self.lineObra.text())
        self.cargar_productos(self.obraSocialSeleccionada)
        self.gbProducto.setVisible(True)

    def limpiarObra(self):
        """
            Permite buscar las obras sociales si aun
            no hay ninguna seleccionada.
            Limpia los campos correspondientes a las
            Obras Sociales, si ya hay una cargada.
        :return:
        """
        if self.tableObra.isVisible():
            #TODO Implementar la busqueda por criterio en la tabla
            print "Implementar esto"
            pass
        else:
            self.lineObra.clear()
            self.lineObra.clear()
            self.lineCuit.clear()
            self.lineObra.setEnabled(True)
            self.lineCuit.setEnabled(True)
            self.tableObra.setVisible(True)
            self.limpiarTabla(self.tableProductos)
            self.gbProducto.hide()

    def validadores(self):
        pass

    def cargar_obras(self):
        """
            Carga todos las obras Sociales en el sistema
            en la tabla de Obras Sociales
        :return:
        """
        self.cargarObjetos(self.tableObra,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def descontarCantidad(self,detalle,producto,cantidad):
        """
            Actualiza el stock en una determinada cantidad,
            de un producto dado
        :param detalle Detalle de la Factura :
        :param producto Codigo de barra del producto:
        :param cantidad Cantidad a descontar:
        :return:
        """
        query=LoteModel.obtenerLoteProducto(producto,self.sesion)
        valores=[]
        for a in query:
            loteProducto=LoteProductoModel.buscarLoteProducto(self.sesion,producto,a.codigo).first()
            if cantidad<=loteProducto.cantidad:
                loteProducto.descontarCantidad(cantidad)
                loteProducto.modificar(self.sesion)
                valores.append([loteProducto,cantidad])
                break
            else:
                cantidad-=loteProducto.cantidad
                valores.append([loteProducto,loteProducto.cantidad])
                loteProducto.descontarCantidad(loteProducto.cantidad)
                loteProducto.modificar(self.sesion)
        self.lotesVentas[detalle]=valores

    def agregarProducto(self):
        """
            Agrega un producto seleccionada a la Factura
        :return:
        """
        itemActual=self.tableProductos.currentItem()
        cantidad, ok = QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
        if not ok:
            self.showMsjEstado("No se ha seleccionado cantidad del producto")
        else:
            cantidadProducto=int(self.tableProductos.item(itemActual.row(),6).text())
            if cantidad>cantidadProducto:
                QtGui.QMessageBox.information(self,"Aviso","La cantidad ingresada es mayor que la del stock")
            else:
                if self.productosAgregados==0:
                    self.factura=FacturaModel(FacturaModel.generarNumero(self.sesion))
                    self.factura.guardar(self.sesion)
                self.productosAgregados+=1
                rowItemActual=itemActual.row()
                rows=self.tableFactura.rowCount()
                self.tableFactura.insertRow(rows)

                #--Carga de items en la tabla--*
                producto = int(self.tableProductos.item(rowItemActual,0).text())
                importeActual=float(self.tableProductos.item(rowItemActual,5).text())
                descuentoActual=float(self.tableProductos.item(rowItemActual,4).text())
                subtotal=importeActual*(1-descuentoActual)
                ####-------------------------#####
                detalleFactura=DetalleFacturaModel(self.factura.numero,producto,cantidad,
                    subtotal*cantidad,descuentoActual,self.productosAgregados
                )
                self.descontarCantidad(detalleFactura,producto,cantidad)
                self.tableFactura.setItem(rows,0,QtGui.QTableWidgetItem(str(detalleFactura.producto)))
                self.tableFactura.setItem(rows,1,QtGui.QTableWidgetItem(str(detalleFactura.cantidad)))
                self.tableFactura.setItem(rows, 2, QtGui.QTableWidgetItem(str("%.2f"%(subtotal*cantidad))))

                detalleFactura.guardar(self.sesion)

                self.data.append([
                    producto, cantidad, subtotal*cantidad, descuentoActual
                ])

                self.actualizar()

    def limpiarVentana(self):
        """
            Limpia la ventana actual
        :return:
        """
        self.lineObra.clear()
        self.lineObra.setEnabled(True)
        self.lineCuit.clear()
        self.lineCuit.setEnabled(True)
        self.tableObra.setVisible(False)
        self.limpiarTabla(self.tableProductos)
        self.limpiarTabla(self.tableFactura)
        self.cargarProductosSinObra()
        self.obraSocialSeleccionada=None

    def calcularTotal(self):
        """
            Calcula el total a pagar
        :return Total a Pagar:
        """
        subtotales=[]
        for row in range(0,self.tableFactura.rowCount()):
            subtotales.append(float(self.tableFactura.item(row,2).text()))
        importeTotal=sum(subtotales)
        return importeTotal

    def cobrarEfectivo(self):
        """
            Vincula la factura con un cobro con
            Efectivo
        :return:
        """
        efectivo,ok=QtGui.QInputDialog.getText(self,"Cobro Efectivo",("El importe total es: $%.2f. Por favor ingrese monto" % self.calcularTotal()))
        try:
            if float(efectivo)>=self.calcularTotal():
                QtGui.QMessageBox.information(self,"Cobro Efectivo","Su vuelto es:%.2f" % (float(efectivo)-self.calcularTotal()))
                cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Efectivo",self.calcularTotal())
                cobroCliente.guardar(self.sesion)
                self.facturaCobrada=True
            else:
                QtGui.QMessageBox.information(self,"Cobro Efectivo","El importe seleccionado es menor al total")
        except ValueError:
            pass

    def cobrarTarjDebito(self):
        """
            Vincula la factura con un cobro con
            Tarjeta de Debito
        :return:
        """
        efectivo,ok=QtGui.QInputDialog.getText(self,"Cobro Tarjeta Debito",("El importe total es: $%.2f. Por favor ingrese monto" % self.calcularTotal()))

        try:
            if float(efectivo) == self.calcularTotal():
                cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Tarjeta Debito",self.calcularTotal())
                cobroCliente.guardar(self.sesion)
                self.facturaCobrada=True
            else:
                QtGui.QMessageBox.information(self,"Aviso","El monto ingresado no coincide con el total de la factura")
        except ValueError:
            pass

    def cobrarNC(self):
        """
            Efectua el cobro de la factura empleando
            la Nota de Credito indicada por el usuario
        :return:
        """
        totalFactura = self.calcularTotal()
        numero,ok = QtGui.QInputDialog.getText(self,"Cobro c/Nota de Crédito","Ingrese número de Nota de Crédito")
        notaCredito = NotaCreditoModel.getNotaCredito(self.sesion,int(numero))
        if notaCredito == None:
            QtGui.QMessageBox.information(self,"Aviso","La Nota de Crédito ingresada no existe")
        elif notaCredito.getTotal(self.sesion) < totalFactura:
            QtGui.QMessageBox.information(self,"Aviso","El monto de la Nota de Credito es insuficiente")
        elif notaCredito.getTotal(self.sesion) - CobroClienteModel.getTotalNC(self.sesion,notaCredito.numero) < totalFactura:
             dif = notaCredito.getTotal(self.sesion) - CobroClienteModel.getTotalNC(self.sesion,notaCredito.numero)
             QtGui.QMessageBox.information(self,"Aviso","La Nota solo posee $" + str(dif))
        else:
            cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Nota Credito",totalFactura)
            cobroCliente.setNC(notaCredito.numero)
            cobroCliente.guardar(self.sesion)
            self.facturaCobrada=True

    def cobrarTarjCredito(self):
        """
            Vincula la factura con un cobro
            con Tarjeta de Credito
        :return:
        """
        cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Tarjeta Credito",self.calcularTotal())
        cobroCliente.guardar(self.sesion)
        self.facturaCobrada=True

    def cobrar(self):
        """
            Establece que metodo emplear para cobrar, en funcion
            de la seleccion del usuario
        :return:
        """

        opcionActual=str(self.cboPago.currentText().toUtf8())

        if opcionActual=="Efectivo":
            self.cobrarEfectivo()
        elif opcionActual=="Nota de Crédito":
            self.cobrarNC()
        elif opcionActual=="Tarjeta de Débito":
            self.cobrarTarjDebito()
        else:
            self.cobrarTarjCredito()

        return opcionActual

    def confirmarOperacion(self):
        """
            Confirma la operacion si todo ha sido exitoso.
            De lo contrario notifica que la Factura todavia no ha sido
            cobrada o que no se efectuo ninguna venta
        :return:
        """
        if self.factura==None:
            QtGui.QMessageBox.information(self,"Aviso","No se ha efectuado ninguna venta")
        else:
            formapago = self.cobrar()
            if self.facturaCobrada:
                QtGui.QMessageBox.information(self,"Venta","La venta se ha realizado con exito")
                data = {}
                data["numero"] = self.factura.numero
                data["fecha"] = self.factura.fecha_emision
                data["detalles"] = self.data
                data["formaPago"] = formapago
                generarFactura(data)
                self.factura = None
                self.facturaCobrada = False
                self.data = []
                self.productosAgregados=0
                self.limpiarVentana()
            else:
                QtGui.QMessageBox.information(self,"Aviso","La factura aun no ha sido cobrada")

    def cancelarOperacion(self):
        """
            Cancela la operacion actual, y reestablece
            los stocks a sus valores originales
        :return:
        """
        if self.factura!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","¿Desea anular la factura creada?")
            if ok:
                self.factura.anular()
                QtGui.QMessageBox.information(self,"Aviso","Factura Anulada")
                for detalle in self.lotesVentas:
                    for loteVenta in self.lotesVentas[detalle]:
                        loteVenta[0].aumentarCantidad(loteVenta[1])
                        loteVenta[0].modificar(self.sesion)
                self.lotesVentas={}
        self.factura=None
        self.productosAgregados=0
        self.data = []
        self.limpiarVentana()
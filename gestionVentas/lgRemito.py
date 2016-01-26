# -*- coding:utf-8 -*-
__author__ = 'leandro'

from datetime import date

from PyQt4 import QtGui

from ventanas import Ui_vtnRegistrarCobroRemito, Ui_vtnVentaConRemito, Ui_vtnRemito
from gui import CRUDWidget,MdiWidget
from baseDatos.clientes import Cliente as ClienteModel
from baseDatos import Producto as ProductoModel
from baseDatos.ventas import Remito as RemitoModel
from baseDatos.ventas import DetalleRemito as DetalleRemitoModel
from baseDatos.obraSocial import ObraSocial as ObraSocialModel
from baseDatos.productos import LoteProducto as LoteProductoModel
from baseDatos.productos import Lote as LoteModel
from baseDatos.ventas import CobroCliente as CobroClienteModel
from baseDatos.ventas import Factura as FacturaModel
from baseDatos.ventas import DetalleFactura as DetalleFacturaModel
from genComprobantes import generarFactura, generarRremito
from validarDatos import ValidarDatos



class Remito(CRUDWidget,Ui_vtnRemito):
    """
        Clase que modela la logica de las operaciones
        Devolucion y Modificacion de Remito
    """

    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()

    def actualizar(self):
        """
            Actualiza la informacion de las tablas de Remito y Detalles.

        :return:
        """
        self.limpiarTabla(self.tableDetalles)
        self.limpiarTabla(self.tableRemito)
        self.cargar_remitos()

    def cargar_remitos(self):
        """
            Carga los remitos que se encuentran en el sistema
            en la tabla correspondiente
        :return:
        """
        self.cargarObjetos(self.tableRemito,
            RemitoModel.obtenerTodosRemitos(self.sesion).all(),
            ("numero", "cliente", "fecha_emision")
        )

    def cargarDetalles(self):
        """
            Carga los detalles de un remito seleccionado por el usuario
        :return:
        """
        self.limpiarTabla(self.tableDetalles)
        itemActual=self.tableRemito.currentItem()
        valor=int(self.tableRemito.item(itemActual.row(),0).text())
        self.lineNumero.setText(str(valor))
        self.cargarObjetos(self.tableDetalles,
            RemitoModel.buscarDetalles(valor,self.sesion),
            ("nro_linea","producto","cantidad")
        )
        ##Para el calculo de subtotal. Como el subtotal es una dato calculado, no se puede hacer explicita la carga
        ##como sucede en el cargarObjetos
        importes=[]
        for a in self.sesion.query(DetalleRemitoModel).filter(DetalleRemitoModel.id_remito==valor):
            for b in self.sesion.query(ProductoModel).filter(ProductoModel.codigo_barra==a.producto):
                importes.append(b.importe * a.cantidad)
        for row in range(0,self.tableDetalles.rowCount()):
            self.tableDetalles.setItem(row, 3, QtGui.QTableWidgetItem(str(importes[row])))

    def eliminarDetalle(self):
        """
            Elimina un detalle especifico del remito seleccionado por el usuario
        :return:
        """
        itemActual=self.tableDetalles.currentItem()
        ok=QtGui.QMessageBox.information(self,"Confirmacion","¿Desea eliminar este item?")
        if ok:
            linea=int(self.tableDetalles.item(itemActual.row(),0).text())
            producto=int(self.tableDetalles.item(itemActual.row(),1).text())
            cantidadRemito=int(self.tableDetalles.item(itemActual.row(),2).text())
            finalizeActualizacion=False
            while not finalizeActualizacion:
                cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
                if not ok:
                    QtGui.QMessageBox.information(self,"Aviso","No se ingreso cantidad")
                else:
                    if cantidad > cantidadRemito:
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
                                cantidadRemito-=cantidad
                                self.tableDetalles.item(itemActual.row(),2).setText(str(cantidadRemito))
                                if cantidadRemito==0:
                                    finalizeActualizacion=True
            detalle=RemitoModel.getDetalle(int(self.lineNumero.text()),int(linea),self.sesion).first()
            detalle.borrar(self.sesion)

            self.tableDetalles.removeRow(itemActual.row())

        else:
            return

    def eliminar(self):
        """
            Elimina un remito seleccionado, una vez que fueron dado de baja todos
            sus detalles
        :return:
        """
        itemActual=self.tableRemito.currentItem()
        if itemActual==None:
            QtGui.QMessageBox.information(self,"Aviso","No se ha seleccionado remito para eliminar")
        else:
            numeroRemito=int(self.tableRemito.item(itemActual.row(),0).text())
            remitoSeleccionado=RemitoModel.buscar(RemitoModel.numero,self.sesion,numeroRemito).first()
            if self.tableDetalles.rowCount()==0:
                remitoSeleccionado.borrar(self.sesion)
                self.tableRemito.removeRow(itemActual.row())
                self.objectDeleted.emit()
            else:
                QtGui.QMessageBox.information(self,"Aviso","Debe dar de baja cada detalle")

    def buscarRemito(self):
        """
            Filtra los remitos actuales por numero, de acuerdo al
            valor ingresado por el usuario
        :return:
        """

        #Estable el valor que se desea buscar
        valor = self.lineNumero.text()

        for i in range(0,self.tableRemito.rowCount()):
            self.tableRemito.setRowHidden(i,False)

        if (not valor == ""):
            for i in range(0,self.tableRemito.rowCount()):
                if not self.tableRemito.item(i,0).text() == valor:
                    self.tableRemito.hideRow(i)

    @classmethod
    def delete(cls, mdi):
        """
            Establece el comportamiento de la ventana de Baja de Remito
        :param mdi:
        :return:
        """
        gui=super(Remito,cls).delete(mdi)
        gui.cargar_remitos()
        gui.tableDetalles.setEnabled(True)
        gui.tableRemito.clicked.connect(gui.cargarDetalles)
        gui.tableDetalles.itemDoubleClicked.connect(gui.eliminarDetalle)
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnActualizar.pressed.connect(gui.actualizar)
        gui.btnBuscar.pressed.connect(gui.buscarRemito)
        gui.lineNumero.returnPressed.connect(gui.buscarRemito)
        return gui

    @classmethod
    def update(cls, mdi):
        """
            Establece el comportamiento de la ventana de Modificacion de Remito
        :param mdi:
        :return:
        """
        gui=super(Remito,cls).update(mdi)
        gui.cargar_remitos()
        gui.btnActualizar.pressed.connect(gui.actualizar)
        gui.tableRemito.clicked.connect(gui.cargarDetalles)
        gui.tableDetalles.itemDoubleClicked.connect(gui.eliminarDetalle)
        gui.btnBuscar.pressed.connect(gui.buscarRemito)
        gui.lineNumero.returnPressed.connect(gui.buscarRemito)
        return gui

class VentaConRemito(CRUDWidget, Ui_vtnVentaConRemito):
    """
        Clase que modela la logica de la operacion
        de Venta con Remito
    """

    def __init__(self, mdi):
        """
            Setea las propiedades de la ventana y variables
        :param mdi Ventana Contenedora:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.btnBuscarCliente.pressed.connect(self.buscarCliente)
        self.lineDni.returnPressed.connect(self.buscarClienteXDNI)
        self.lineApellido.returnPressed.connect(self.buscarClienteXApellido)
        self.lineNombre.returnPressed.connect(self.buscarClienteXNombre)
        self.lineMedicamento.returnPressed.connect(self.buscarXMedicamento)
        self.lineMonodroga.returnPressed.connect(self.buscarXMonodroga)
        self.tableClientes.itemDoubleClicked.connect(self.cargarLines)
        self.tableProductos.itemDoubleClicked.connect(self.agregarProducto)
        self.tableRemito.itemDoubleClicked.connect(self.cambiarCantidad)
        self.btnEliminar.pressed.connect(self.eliminarDetalle)
        self.btnAceptar.pressed.connect(self.aceptar)
        self.btnCancelar.pressed.connect(self.cancelar)
        self.cargar_clientes()
        self.cargar_productos()
        self.gbProducto.hide()
        self.gbRemito.hide()
        self.remito=None
        self.productosAgregados=0
        self.lotesVentas={}
        self.dniCliente = None
        self.detalles = [] #Arreglo que mantiene todos los detalles agregados al Remito

    def cargar_productos(self):
        """
            Carga los productos que se encuentran en el
            sistema en la Tabla de Productos
        :return:
        """
        for n, obj in enumerate(ProductoModel.buscarTodos("codigo_barra",self.sesion).all()):
            self.tableProductos.insertRow(n)
            self.tableProductos.setItem(n, 0, QtGui.QTableWidgetItem(str(obj.codigo_barra)))
            self.tableProductos.setItem(n, 1, QtGui.QTableWidgetItem(str(obj.id_medicamento)))
            self.tableProductos.setItem(n, 2, QtGui.QTableWidgetItem(str(obj.id_presentacion)))
            self.tableProductos.setItem(n, 3, QtGui.QTableWidgetItem(obj.getNombreMonodroga(self.sesion)))
            self.tableProductos.setItem(n, 4, QtGui.QTableWidgetItem(str(obj.getCantidad(self.sesion))))
            self.tableProductos.setItem(n, 5, QtGui.QTableWidgetItem(str(obj.importe)))

    def cargar_clientes(self):
        """
            Carga los clientes cargados en el sistema
            en la Tabla de Clientes
        :return:
        """
        self.cargarObjetos(self.tableClientes,
            ClienteModel.buscarTodos("dni", self.sesion).all(),
            ("dni", "nombre", "apellido")
        )

    def validadores(self):
         ##Esta parte analiza los campos requeridos para el cliente
        requeridos = ["nombre", "apellido", "dni"]
        camposRequeridos = [ getattr(self, "line%s" % campo.title()) for campo in requeridos ]
        ValidarDatos.setValidador(camposRequeridos)

        camposRequeridos = [getattr(self,"lineMonodroga")]
        ValidarDatos.setValidador(camposRequeridos)

        camposRequeridos = [getattr(self,"lineMedicamento")]
        ValidarDatos.setValidador(camposRequeridos)

    def buscarCliente(self):
        """
            Busca los clientes de acuerdo al criterio de
            busqueda establecido por el usuario
        :return:
        """
        if self.lineDni.isEnabled():
            pass
        else:
            self.lineDni.setEnabled(True)
            self.lineApellido.setEnabled(True)
            self.lineNombre.setEnabled(True)
            self.lineNombre.clear()
            self.lineDni.clear()
            self.lineApellido.clear()
            self.limpiarTabla(self.tableClientes)
            self.tableClientes.setVisible(True)
            self.cargar_clientes()

    def buscarClienteXDNI(self):
        """
            Carga en la tabla de Clientes aquellos cuyo DNI
            sea igual al indicado por el usuario
        :return:
        """

        dni = str(self.lineDni.text())
        if dni == "":
            self.limpiarTabla(self.tableClientes)
            self.cargar_clientes()
        else:
            data = self.getContenidoTabla(self.tableClientes)
            newData = filter(lambda x: x[0]==dni, data)
            self.limpiarTabla(self.tableClientes)
            for row, value in enumerate(newData):
                    self.tableClientes.insertRow(row)
                    for col in range(0,self.tableClientes.columnCount()):
                         self.tableClientes.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def buscarClienteXNombre(self):
        """
            Carga en la tabla de Clientes aquellos cuyo Nombre
            sea igual al indicado por el usuario
        :return:
        """
        nombre = str(self.lineNombre.text())
        if nombre == "":
            self.limpiarTabla(self.tableClientes)
            self.cargar_clientes()
        else:
            data = self.getContenidoTabla(self.tableClientes)
            newData = filter(lambda x: x[1].upper() == nombre.upper(), data)
            self.limpiarTabla(self.tableClientes)
            for row, value in enumerate(newData):
                    self.tableClientes.insertRow(row)
                    for col in range(0,self.tableClientes.columnCount()):
                         self.tableClientes.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def buscarClienteXApellido(self):
         """
            Carga en la tabla de Clientes aquellos cuyo Apellido
            sea igual al indicado por el usuario
         :return:
         """
         apellido = str(self.lineApellido.text())
         if apellido == "":
            self.limpiarTabla(self.tableClientes)
            self.cargar_clientes()
         else:
            data = self.getContenidoTabla(self.tableClientes)
            newData = filter(lambda x: x[2]==apellido, data)
            self.limpiarTabla(self.tableClientes)
            for row, value in enumerate(newData):
                    self.tableClientes.insertRow(row)
                    for col in range(0,self.tableClientes.columnCount()):
                         self.tableClientes.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def buscarXMonodroga(self):
        """
            Filtra los productos segun la
            Monodroga indicada por el usuario
        :return:
        """

        nombreMonodroga = str(self.lineMonodroga.text())
        if len(nombreMonodroga) == 0:
            self.limpiarTabla(self.tableProductos)
            self.cargar_productos()
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
            self.limpiarTabla(self.tableProductos)
            self.cargar_productos()
        else:
            data = self.getContenidoTabla(self.tableProductos)
            data = filter(lambda x: x[1].upper() == nombreMedicamento.upper() , data)
            self.limpiarTabla(self.tableProductos)
            for row, value in enumerate(data):
                self.tableProductos.insertRow(row)
                for col in range(0,self.tableProductos.columnCount()):
                    self.tableProductos.setItem(row, col, QtGui.QTableWidgetItem(value[col]))

    def cargarLines(self):
        """
            Carga los lines correspondientes con la informacion
            del cliente seleccionado
        :return:
        """
        self.lineDni.setEnabled(False)
        self.lineNombre.setEnabled(False)
        self.lineApellido.setEnabled(False)
        #Recuperar la informacion de un item
        row=self.tableClientes.currentItem().row()
        infoItem=[]
        for col in range(0,self.tableClientes.columnCount()):
            infoItem.append(self.tableClientes.item(row,col).text())

        self.dniCliente = int(infoItem[0])

        #Cargar la info del item en los lines
        self.lineDni.setText(infoItem[0])
        self.lineNombre.setText(infoItem[1])
        self.lineApellido.setText(infoItem[2])
        self.tableClientes.hide()
        self.gbProducto.setVisible(True)
        self.gbRemito.setVisible(True)

    def descontarCantidad(self,detalle,producto,cantidad):
        """
            Descuenta la cantidad especificada de un
            determinado producto
        :param detalle Detalle Remito:
        :param producto Codigo de Barra del producto:
        :param cantidad Cantidad del Producto:
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
            Agrega un producto seleccionado al Remito creado
        :return:
        """
        itemActual=self.tableProductos.currentItem()
        if itemActual==None:
            self.showMsjEstado("No se ha seleccionado ningun producto para agregar")
        else:
            cantidad, ok = QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
            if not ok:
                self.showMsjEstado("No se ha seleccionado cantidad del producto")
            else:
                if cantidad>int(self.tableProductos.item(itemActual.row(),4).text()):
                    self.showMsjEstado("La cantidad seleccionada es mayor a la actual")
                else:
                    rowItemActual=itemActual.row()
                    rows=self.tableRemito.rowCount()
                    if self.productosAgregados==0:
                        self.remito=RemitoModel(RemitoModel.obtenerNumero(self.sesion),int(self.lineDni.text()))
                        self.remito.guardar(self.sesion)
                    self.productosAgregados+=1

                    codigo = int(self.tableProductos.item(rowItemActual,0).text())
                    subtotal = cantidad*float(self.tableProductos.item(rowItemActual,5).text())

                    self.tableRemito.insertRow(rows)
                    self.tableRemito.setItem(rows, 0, QtGui.QTableWidgetItem(str(codigo)))
                    self.tableRemito.setItem(rows, 1, QtGui.QTableWidgetItem(str(cantidad)))
                    self.tableRemito.setItem(rows, 2, QtGui.QTableWidgetItem(str(subtotal)))

                    self.detalles.append([codigo,cantidad,subtotal])

                    self.detalle=DetalleRemitoModel(self.remito.numero,self.productosAgregados,
                        int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                    self.descontarCantidad(self.detalle,int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                    self.detalle.guardar(self.sesion)
                    self.limpiarTabla(self.tableProductos)
                    self.cargar_productos()

    def cambiarCantidad(self):
        """
            Modifica la cantidad de un producto en
            la Tabla de Productos
        :return:
        """
        itemActual=self.tableRemito.currentItem()
        cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
        if ok:
            importeUnitario=float(self.tableRemito.item(itemActual.row(),2).text())/int(self.tableRemito.item(itemActual.row(),1).text())
            itemCantidad=self.tableRemito.item(itemActual.row(),1)
            itemCantidad.setText(str(cantidad))
            itemImporte=self.tableRemito.item(itemActual.row(),2)
            itemImporte.setText(str(int(cantidad)*importeUnitario))

    def eliminarDetalle(self):
        print("Eliminando Detalle")

    def limpiarVentana(self):
        """
            Limpia la ventana actual
        :return:
        """
        self.lineDni.setEnabled(True)
        self.lineDni.clear()
        self.lineNombre.setEnabled(True)
        self.lineNombre.clear()
        self.lineApellido.setEnabled(True)
        self.lineApellido.clear()
        self.lineMedicamento.clear()
        self.lineMonodroga.clear()
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.limpiarTabla(self.tableClientes)
        self.limpiarTabla(self.tableProductos)
        self.limpiarTabla(self.tableRemito)
        self.tableClientes.setVisible(True)
        self.cargar_clientes()
        self.cargar_productos()

    def aceptar(self):
        """
            Confirma la operacion en curso, y envia
            la informacion necesaria para imprimir el comprobante.
            Si no se ha efectuado ninguna venta, se notifica
        :return:
        """
        if self.remito==None:
            QtGui.QMessageBox.information(self,"Venta con Remito","No se ha efectuado ninguna venta")
        else:
            QtGui.QMessageBox.information(None,"Venta","La venta se ha realizado con exito")

            self.limpiarTabla(self.tableRemito)

            ##Se envian los datos necesarios para generar el comprobante
            data = {}
            data["numero"] = self.remito.numero
            data["fecha"] = self.remito.fecha_emision
            data["datosCliente"] = ClienteModel.getDatosCliente(self.sesion,self.dniCliente)
            data["detalles"] = self.detalles
            generarRremito(data)

        self.remito=None
        self.productosAgregados=0
        self.limpiarVentana()
        self.detalles = []
        self.dniCliente = None

    def cancelar(self):
        """
            Cancela la operacion en curso, anulando el
            Remito creado y restaurando el stock de los productos a
            sus valores originales.
        :return:
        """
        if self.remito!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","¿Desea anular el remito creado?")
            if ok:
                self.remito.anular()
                QtGui.QMessageBox.information(self,"Aviso","Remito Anulado")
                for detalle in self.lotesVentas:
                    for loteVenta in self.lotesVentas[detalle]:
                        loteVenta[0].aumentarCantidad(loteVenta[1])
                        loteVenta[0].modificar(self.sesion)
                self.lotesVentas={}
                self.cargar_productos()
        self.remito=None
        self.productosAgregados=0
        self.limpiarVentana()

class RegistrarCobroRemito(CRUDWidget, Ui_vtnRegistrarCobroRemito):

    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.cargar_obras()
        self.tableObras.hide()
        self.lineRazonSocial.setEnabled(False)
        self.btnBuscarOs.setEnabled(False)
        self.tableRemitos.setEnabled(False)

        self.rbtnRazonSocial.pressed.connect(self.habilitarObras)
        self.tableObras.itemDoubleClicked.connect(self.cargarLineObra)
        self.btnBuscarOs.pressed.connect(self.buscarObra)
        self.lineRazonSocial.returnPressed.connect(self.buscarObra)
        self.btnBuscarRemito.pressed.connect(self.buscarRemito)
        self.btnAgregar.pressed.connect(self.agregarRemito)
        self.lineNumero.returnPressed.connect(self.buscarRemito)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)

        self.obraSocialSeleccionada=None
        self.factura=None
        self.remitosAgregados=0
        self.detallesAgregados=0
        self.remitoActual=None
        self.remitosCobrados=[]
        self.importeTotal=0
        self.itemsDeFactura = []

    def buscarObra(self):
        """
            Busca las obras sociales solicitadas por el usuario
        :return:
        """
        if self.lineRazonSocial.isEnabled():
            valor = str(self.lineRazonSocial.text()).upper()
            for i in range(0,self.tableObras.rowCount()):
                self.tableObras.setRowHidden(i,False)

            if (not valor == ""):
                for i in range(0,self.tableObras.rowCount()):
                    if not self.tableObras.item(i,0).text() == valor:
                        self.tableObras.hideRow(i)
        else:
            self.lineRazonSocial.setEnabled(True)

    def cargarLineObra(self):
        """
            Establece el valor del line de obra de acuerdo con
            lo seleccionado por el cliente.
        :return:
        """
        if self.lineRazonSocial.isEnabled():
            itemActual=self.tableObras.currentItem()
            razonSocial=str(self.tableObras.item(itemActual.row(),0).text())
            self.obraSocialSeleccionada=razonSocial
            self.lineRazonSocial.setText(razonSocial)
            self.lineRazonSocial.setEnabled(False)
        else:
            QtGui.QMessageBox.warning(self,"Advertencia","Ya se ha seleccionado una obra social")

    def habilitarObras(self):
        """
            Muestra todas las Obras Sociales habilitadas,
            de acuerdo a si existe factura o no.
        :return:
        """
        if self.factura!=None:
            QtGui.QMessageBox.information(self,"Aviso","Ya existe una factura. "
                                                       "No se puede modificar la obra social")
        else:
            if not self.rbtnRazonSocial.isChecked():
                self.btnBuscarOs.setEnabled(True)
                self.lineRazonSocial.setEnabled(True)
                self.tableObras.setVisible(True)
            else:
                self.lineRazonSocial.clear()
                self.btnBuscarOs.setEnabled(False)
                self.lineRazonSocial.setEnabled(False)
                self.tableObras.setVisible(False)
                self.obraSocialSeleccionada=None

    def validadores(self):
        pass

    def cargar_obras(self):
        """
            Carga todas las Obras Sociales disponibles
        :return:
        """
        self.cargarObjetos(self.tableObras,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def buscarRemito(self):
        """
            Busca el remito ingresado por el usuario. Si existe carga los detalles
            del mismo. Si existe pero ya fue cobrado o si no existe, se le notifica
            al usuario.
        :return:
        """

        if self.lineNumero.isEnabled():
            numeroRemito=self.lineNumero.text()
            if len(numeroRemito)==0:
                self.showMsjEstado("No se ha ingresado numero de remito")
            else:
                self.remitoActual = RemitoModel.existeRemito(int(numeroRemito),self.sesion)
                if self.remitoActual== None:
                    QtGui.QMessageBox.warning(self,"Advertencia","El remito ingresado no existe")
                else:
                    if self.remitoActual.getCobrado() == True:
                        QtGui.QMessageBox.information(self,"Aviso","El remito ingresado ya sido cobrado")
                    else:
                        detallesRemitos=RemitoModel.buscarDetalles(int(numeroRemito),self.sesion)
                        self.limpiarTabla(self.tableRemitos)
                        self.cargarObjetos(self.tableRemitos,
                            detallesRemitos,("producto","cantidad")
                        )
                        importes=[]
                        for a in detallesRemitos:
                            for b in self.sesion.query(ProductoModel).filter(ProductoModel.codigo_barra==a.producto):
                                importes.append(b.importe * a.cantidad)
                        for row in range(0,self.tableRemitos.rowCount()):
                            self.tableRemitos.setItem(row, 2, QtGui.QTableWidgetItem(str(importes[row])))
                        self.lineNumero.setEnabled(False)
        else:
            self.lineNumero.clear()
            self.lineNumero.setEnabled(True)
            self.limpiarTabla(self.tableRemitos)

    def obtenerValoresTabla(self,tabla):
        """
            Obtiene un arreglo que contiene arreglos
            que representan los valores de cada row
        :param tabla :
        :return:
        """
        values=[]
        for row in range(0,tabla.rowCount()):
            valuesItem=[]
            for col in range(0,tabla.columnCount()):
                valuesItem.append(tabla.item(row,col).text())
            values.append(valuesItem)
        return values

    def armarItemFactura(self,itemRemito,obraSocial,nroFactura,nroLinea):
        """
            Arma el Item de la Factura correspondiente a un Item
            del Remito seleccionado por el usuario
        :param itemRemito Arreglo con los valores de un item del Remito actual:
        :param obraSocial Obra Social seleccionada por el usuario:
        :param nroFactura Numero de Factura Actual:
        :param nroLinea Numero de Linea de la Factura Actual:
        :return:
        """
        producto=str(itemRemito[0])
        cantidad=str(itemRemito[1])
        importe=str(itemRemito[2])
        if obraSocial==None:
            descuento=0
        else:
            descuento=obraSocial.getDescuento(producto,self.sesion)
        subtotal=(float(importe)*(1-descuento))
        detalleFactura=DetalleFacturaModel(nroFactura,producto,cantidad,subtotal,descuento,nroLinea)
        detalleFactura.guardar(self.sesion)
        itemFactura=[str(producto),str(cantidad),("%.2f" % subtotal),str(descuento)]
        self.itemsDeFactura.append(itemFactura)
        return itemFactura

    def mostrarTotal(self):
        """
            Actualiza el label de Importe total, mostrando
            lo que se debe cobrar
        :return:
        """
        subtotales=[]
        for row in range(0,self.tableFactura.rowCount()):
            subtotales.append(float(self.tableFactura.item(row,2).text()))
        self.lblImporteTotal.setText("Importe Total: $%.2f" % sum(subtotales))
        self.importeTotal=sum(subtotales)

    def agregarRemito(self):
        """
            Agrega el remito seleccionado por el usuario
            a un arreglo de Remitos por cobrar.
        :return:
        """
        if self.tableRemitos.rowCount()==0:
            self.showMsjEstado("No se ha seleccionado remito para agregar")
        else:
            if self.remitosAgregados==0:
                self.factura=FacturaModel(FacturaModel.generarNumero(self.sesion))
                self.factura.guardar(self.sesion)
            self.remitosAgregados+=1
            if self.obraSocialSeleccionada==None:
                obraSocial=None
            else:
                obraSocial=ObraSocialModel.getObraSocial(self.obraSocialSeleccionada,self.sesion)
            for row,item in enumerate(self.obtenerValoresTabla(self.tableRemitos)):
                self.tableFactura.insertRow(row)
                self.detallesAgregados+=1
                for col,value in enumerate(self.armarItemFactura(item,obraSocial,self.factura.numero,self.detallesAgregados)):
                    self.tableFactura.setItem(row,col,QtGui.QTableWidgetItem(str(value)))
            self.remitoActual.setCobrado(self.factura.numero)
            self.remitoActual.modificar(self.sesion)
            self.remitosCobrados.append(self.remitoActual)
            self.mostrarTotal()
            self.limpiarTabla(self.tableRemitos)
            self.lineNumero.setEnabled(True)
            self.lineNumero.clear()

    def limpiarForm(self):
        """
            Limpia la ventana una vez que se finalizó
            la operación.
        :return:
        """
        self.remitosAgregados=0
        self.detallesAgregados=0
        self.factura=None
        self.remitoActual=None
        self.importeTotal=0
        self.limpiarTabla(self.tableFactura)
        self.limpiarTabla(self.tableRemitos)
        self.lineRazonSocial.clear()
        self.lineNumero.clear()
        self.lineNumero.setEnabled(True)
        self.rbtnRazonSocial.setChecked(False)
        self.tableObras.hide()
        self.lblImporteTotal.setText("Importe Total: $0.00")

    def confirmarOperacion(self):
        """
            Verifica si el cliente acepta la operación realizada.
            Si acepta genera la factura correspondiente, si no deshace lo
            realizado.
        :return:
        """

        if self.factura==None:
            QtGui.QMessageBox.information(self,"Aviso","No se ha realizado ningun cobro")
        else:
            efectivo,ok=QtGui.QInputDialog.getText(self,"Importe a pagar",("El importe a pagar es: $%.2f" % self.importeTotal))
            if float(efectivo) > self.importeTotal:
                QtGui.QMessageBox.information(self,"Cambio","Su vuelto es: $%.2f" % (float(efectivo)-self.importeTotal))
            else:
                 QtGui.QMessageBox.information(self,"Cambio","Su vuelto es: $0.00")
            cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Efectivo",self.importeTotal)
            cobroCliente.guardar(self.sesion)
            QtGui.QMessageBox.information(self,"Venta","El cobro ha sido exitoso")

            data = {}
            data["numero"] = self.factura.numero
            data["fecha"] = self.factura.fecha_emision
            data["detalles"] = self.itemsDeFactura
            data["formaPago"] = "Efectivo"
            generarFactura(data)

            self.limpiarForm()
            self.itemsDeFactura = []

    def cancelarOperacion(self):
        """
            Marca a todos los remitos afectados como No Cobrados
            cuando el usuario indica que quiere cancelar la operacion
        :return:
        """
        if self.factura!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","Existe una factura creada")
            if ok:
                self.limpiarForm()
                for remito in self.remitosCobrados:
                    remito.setCobrado(None)
                    remito.modificar(self.sesion)
                self.factura.anular()





# -*- coding:utf-8 -*-
__author__ = 'waldo'

import os

import pycha.bar
import pycha.line
import cairo
import pdfkit
import xlsxwriter
from PyQt4 import QtGui

from ventanas import Ui_vtnListar
from gui import MdiWidget
from baseDatos import Cliente, LoteProducto, Producto, Factura, Remito
from baseDatos import Producto as ProductoModel
from baseDatos import Factura as FacturaModel
from baseDatos import Remito as RemitoModel
from baseDatos import Cliente as ClienteModel

class Listar(MdiWidget, Ui_vtnListar):
    """
        Genera los listados (varios) en pdf y excel.
    """
    def __init__(self, mdi):
        """Constructor de la clase Listar.

        :param mdi: EL mdi referente a la ventana.
        :return:

        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.btnListar.pressed.connect(self.Listar)

    def Listar(self):
        """
        Genera el listado correspondiente de acuerdo a la opción seleccionada.
        :return:
        """
        self.listado = self.cbTipoListado.currentText()
        if (self.listado=="Facturas Liquidadas Pendientes de Cobro"):
            pass
        elif (self.listado=="Productos en Stock"):
            if self.rbtnExcel.isChecked():
                self.generarExcelProductos()
            else:
                lote_producto = LoteProducto.buscarTodos("id_lote", self.sesion).all()
                self.listarProductos(lote_producto)
                data = self.productosStock(lote_producto)
                self.diagramaBarras(data)
                pdfkit.from_file('reportes/listadoProductosStock.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')
        elif (self.listado=="Ventas Realizadas"):
            if self.rbtnExcel.isChecked():
                self.generarExcelVentas()
            else:
                facturas = Factura.buscarTodos(Factura.numero, self.sesion).all()
                remitos = Remito.buscarTodos(Remito.numero, self.sesion).all()
                ventasFact = self.cantidadVentasContado(facturas)
                ventasRem = self.cantidadVentasRemito(remitos)
                self.listarVentas(ventasFact, ventasRem)
                pdfkit.from_file('reportes/listadoVentas.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')
        else:
            if self.rbtnExcel.isChecked():
                self.generarExcelClientes()
            else:
                clientes = Cliente.buscarTodos(Cliente.dni, self.sesion).all()
                self.listarClientes(clientes)
                pdfkit.from_file('reportes/listadoClientes.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')

    def listarProductos(self, lote_producto):
        """
        Genera el html usado para generar el pdf final del listado de los productos en stock.
        :param lote_producto: arreglo que contiene todos los productos y sus diferentes lotes.
        :return:
        """
        #TODO esta bien q se de de baja un producto para el q hay stock???
        # hay q listar los dados de baja?? esto depende de la resp a la preg anterior.

        archivo = open("PlantillasListados/productosStock.html", "r")
        contenido = archivo.read()
        archivo.close()

        body = ""
        i = 0

        for lp in lote_producto:
            if (lp.getCantidad() > 0):
                i += 1
                producto = Producto.buscar(Producto.codigo_barra, self.sesion, lp.getIdProducto()).first()
                nr_prod = str(i)
                id_lote = str(lp.getIdLote())
                desc = str(producto.getIdMedicamento()) + """ """ + str(producto.getIdPresentacion())
                cant = str(lp.getCantidad())
                cadena = """<tr>

                <td><strong>{producto}</strong></td>
                <td class="text-right">{lote}</td>
                <td><strong>{descripcion}</strong></td>
                <td class="text-right">{cantidad}</td>
                </tr>""".format(producto=nr_prod, lote=id_lote, descripcion=desc, cantidad=cant)
                body += cadena
        contenido_nuevo = contenido.format(contenido=body)

        archivo = open("reportes/listadoProductosStock.html", "w")
        archivo.write(contenido_nuevo)
        archivo.close()

    #TODO en este listado se pueden usar las fechas de los campos de deFechaDesde y deFechaHasta
    def listarVentas(self, ventasFact, ventasRem):
        """
        Genera el html usado para generar el pdf final del listado de las Ventas realizadas.
        :param ventasFact: arreglo que contiene todas las ventas de contado realizadas.
        :param ventasRem: arreglo que contiene todas las ventas con remito realizadas.
        :return:
        """
        archivo = open("PlantillasListados/ventas.html", "r")
        contenido = archivo.read()
        archivo.close()

        tableFact = ""

        for fecha, cant in ventasFact:
            cadena = """<tr>

                <td><strong>{fecha}</strong></td>
                <td class="text-right">{cantidad}</td>
                </tr>""".format(fecha=str(fecha), cantidad=str(cant))
            tableFact += cadena

        tableRem = ""

        for fecha, cant in ventasRem:
            cadena = """<tr>

                <td><strong>{fecha}</strong></td>
                <td class="text-right">{cantidad}</td>
                </tr>""".format(fecha=str(fecha), cantidad=str(cant))
            tableRem += cadena

        contenido_nuevo = contenido.format(contenidoFact=tableFact, contenidoRem=tableRem)

        archivo = open("reportes/listadoVentas.html", "w")
        archivo.write(contenido_nuevo)
        archivo.close()

    def listarClientes(self, clientes):
        """
        Genera el html usado para generar el pdf final del listado de los Clientes.
        :param clientes: arreglo que contiene todos los clientes.
        :return:
        """
        archivo = open("PlantillasListados/clientes.html", "r")
        contenido = archivo.read()
        archivo.close()

        body = ""
        i = 0
        for cliente in clientes:
            i += 1
            nombre= str(cliente.getNombre()) + """ """ + str(cliente.getApellido())
            cadena = """<tr>

                <td><strong>{cliente}</strong></td>
                <td><strong>{nombre}</strong></td>
                <td class="text-right">{dni}</td>
                <td><strong>{direccion}</strong></td>
                <td class="text-right">{telefono}</td>
                </tr>""".format(cliente=str(i), nombre=nombre, dni=str(cliente.getDni()),
                                direccion=str(cliente.getDireccion()), telefono=str(cliente.getTelefono()))
            body += cadena
        contenido_nuevo = contenido.format(contenido=body)

        archivo = open("reportes/listadoClientes.html", "w")
        archivo.write(contenido_nuevo)
        archivo.close()

    def diagramaBarras(self, data):
        """
        Genera un diagraga de barras en una imagen png a incluir en el pdf,
        de acuerdo a los datos pasados por parametro.
        :param data: datos utilizados para generar el diagrama de barras.
        :return:
        """
        # Ancho y alto de la gráfica
        width, height = (550, 310)
        # Superficie cairo
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        # Los cargamos en el dataSet
        dataSet = (
            ('Puntos', [(i, l[1]) for i, l in enumerate(data)]),
        )
        # Opciones de la gráfica
        options = {
            'legend': {'hide': True},
            'axis': {
                'x': {
                    'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(data)],
                    'rotate': 25,
                },
                'y': {
                    'tickCount': 5,
                }
            },
            'background': {
                'chartColor': '#f3f9fb',
                'lineColor': '#d1e5ec'
            },
            'colorScheme': {
                'name': 'gradient',
                'args': {
                    'initialColor': 'red',
                },
            },
        }
        # Creamos la gráfica
        chart = pycha.bar.VerticalBarChart(surface, options)
        chart.addDataset(dataSet)
        chart.render()
        # La guardamos en un fichero .png
        surface.write_to_png('reportes/diagBarra.png')

    def productosStock(self, lote_producto):
        """
        Devuelve un los datos de los productos y su/s lote/s de aquellos que tengan una cantidad mayor a 0 en stock.
        :param lote_producto: arreglo de todos los lotes/productos almacenados en la base de datos.
        :return: data
        """
        data = []
        for lp in lote_producto:
            if (lp.getCantidad() > 0):
                producto = Producto.buscar(Producto.codigo_barra, self.sesion, lp.getIdProducto()).first()
                descripcion = str(producto.getIdMedicamento()) + " " + str (producto.getIdPresentacion())
                data.append((descripcion, lp.getCantidad()))
        return data

    def cantidadVentasContado(self, facturas):
        """
        Devuelve la cantidad de ventas de contado realizadas (por fecha).
        :param facturas: arreglo que contiene todas las facturas correpondientes a las ventas realizadas.
        :return: fch_cant
        """
        fch_cant = []
        cantidad = 0
        for factura in facturas:
            fecha = factura.getFechaEmision()
            if (cantidad == 0):
                cantidad += 1
                fch_cant.append((fecha, cantidad))
            else:
                i = 0
                for fch, cant in fch_cant:
                    i += 1
                    if (fecha == fch):
                        fch_cant.remove((fch, cant))
                        cant += 1
                        fch_cant.append((fch, cant))
                    else:
                        if (fch_cant.__len__() == i):
                            cantidad = 1
                            fch_cant.append((fecha, cantidad))
                            break
        fch_cant.sort()
        self.diagramaLinea(fch_cant, 'reportes/diagLineaFact.png', 'Ventas de Contado')
        return fch_cant

    def cantidadVentasRemito(self, remitos):
        """
        Devuelve la cantidad de ventas con remito realizadas (por fecha).
        :param remitos: arreglo que contiene todos los remitos correpondientes a las ventas realizadas.
        :return: ventas_rem
        """
        cantidad = 0
        ventas_rem = []
        for remito in remitos:
            fecha = remito.getFechaEmision()
            if (cantidad == 0):
                cantidad += 1
                ventas_rem.append((fecha, cantidad))
            else:
                i = 0
                for fch, cant in ventas_rem:
                    i += 1
                    if (fecha == fch):
                        ventas_rem.remove((fch, cant))
                        cant += 1
                        ventas_rem.append((fch, cant))
                    else:
                        if (ventas_rem.__len__() == i):
                            cantidad = 1
                            ventas_rem.append((fecha, cantidad))
                            break
        ventas_rem.sort()
        self.diagramaLinea(ventas_rem, 'reportes/diagLineaRem.png', 'Ventas con Remito')
        return ventas_rem

    def diagramaLinea(self, data, png, legend):
        """
        Genera un diagraga de lineas en una imagen png a incluir en el pdf,
        de acuerdo a los datos pasados por parametro.
        :param data: datos de la línea.
        :param png: dirección de la imagen donde guardar el diagrama.
        :param legend: leyenda a mostrar en el diagrama.
        :return:
        """
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)

        dataSet = (
            (legend, [(i, l[1]) for i, l in enumerate(data)]),
            )

        options = {
            'axis': {
                'x': {
                    'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(data)],
                    'rotate': 25,
                },
                'y': {
                    'tickCount': 5,
                }
            },
            'background': {
                'color': '#eeeeff',
                'lineColor': '#444444'
            },
            'colorScheme': {
                'name': 'gradient',
                'args': {
                    'initialColor': 'green',
                },
            },
            'legend': {
                'hide': False,
            },
        }
        chart = pycha.line.LineChart(surface, options)

        chart.addDataset(dataSet)
        chart.render()

        surface.write_to_png(png)

    def generarExcelProductos(self):
        """
            Crea el listado en Excel correspondiente al total de los
            productos en stock en la farmacia
        :return None:
        """
        data={}
        lotesProductos={}
        for producto in (ProductoModel.buscarTodos("codigo_barra",self.sesion).all()):
            nombreProducto = '%(medicamento)s %(presentacion)s' % \
                             {"medicamento":producto.id_medicamento,
                              "presentacion":producto.id_presentacion}
            data[nombreProducto.upper()]=producto.getCantidad(self.sesion)
            lotesProductos[nombreProducto]=producto.buscarLotes(self.sesion)

        documento=xlsxwriter.Workbook('Excel/StockProductos.xlsx')
        hoja=documento.add_worksheet('General')
        bold = documento.add_format({'bold': 1,})
        bold.set_align('center')
        hoja.set_column(0,0,45)
        hoja.set_column(1,1,15)
        ##Añado un grafico al documento
        grafico = documento.add_chart({'type':'column'})
        productos=list(data.keys())
        cantidades=list(data.values())
        hoja.write('A1','Producto',bold)
        hoja.write('B1','Cantidad',bold)
        hoja.write_column('A2',productos)
        hoja.write_column('B2',cantidades)
        grafico.add_series({
                'categories':[hoja.name,1,0,len(productos),0],
                'values': [hoja.name,1,1,len(cantidades),1]
        })
        grafico.set_x_axis({
            'name':'Productos',
            'name-font':{'size':16,'bold':True},
            'num_font':{'italic':True},
        })
        hoja.insert_chart('E3', grafico)
        for producto in lotesProductos:
            self.generarHojaProducto(documento,producto,lotesProductos[producto])
        documento.close()

        QtGui.QMessageBox.information(self, "Listado" , "El listado ha sido generado con exito")

    def generarHojaProducto(self,documento,producto,aLotes):
        """
            Crea un hoja correspondiente a cada producto, especificando sus
            lotes y cantidades
        :param: documento:
        :param: producto:
        :param: aLotes:
        :return None:
        """
        hoja=documento.add_worksheet(producto.upper()[0:20])
        bold = documento.add_format({'bold': 1,})
        bold.set_align('center')
        hoja.set_column(0,0,45)
        hoja.set_column(1,1,15)
        ##Añado un grafico al documento
        grafico = documento.add_chart({'type':'column'})
        lotes=list(aLotes.keys())
        cantidades=list(aLotes.values())
        hoja.write('A1','Lote',bold)
        hoja.write('B1','Cantidad',bold)
        hoja.write_column('A2',lotes)
        hoja.write_column('B2',cantidades)
        grafico.add_series({
                'categories':[hoja.name,1,0,len(lotes),0],
                'values': [hoja.name,1,1,len(cantidades),1]
        })
        grafico.set_x_axis({
            'name':'Lotes',
            'name-font':{'size':16,'bold':True},
            'num_font':{'italic':True},
        })
        hoja.insert_chart('E3', grafico)

    def generarExcelVentas(self):
        """
            Crea el documento Excel correspondiente a las ventas realizadas en
            un periodo de tiempo dado
        :return None :
        """
        ventas={}
        for factura in (FacturaModel.buscarTodos("numero",self.sesion).all()):
            if (factura.fecha_emision in ventas):
                ventas[factura.fecha_emision]+=1
            else:
                ventas[factura.fecha_emision]=1
        for remito in (RemitoModel.buscarTodos("numero",self.sesion).all()):
            if (remito.fecha_emision in ventas):
                ventas[remito.fecha_emision]+=1
            else:
                ventas[remito.fecha_emision]=1

        documento=xlsxwriter.Workbook('Excel/Ventas.xlsx')
        hoja=documento.add_worksheet('Ventas')
        bold = documento.add_format({'bold': 1,})
        date_format = documento.add_format({'num_format': 'yyyy/mm/dd'})
        bold.set_align('center')
        hoja.set_column(0,0,45)
        hoja.set_column(1,1,15)
        ##Añado un grafico al documento
        grafico = documento.add_chart({'type':'line'})
        fechas=list(ventas.keys())
        cantidades=list(ventas.values())
        hoja.write('A1','Fecha',bold)
        hoja.write('B1','Cantidad Vtas',bold)
        hoja.write_column('A2',fechas,date_format)
        hoja.write_column('B2',cantidades)
        grafico.add_series({
                'categories':[hoja.name,1,0,len(fechas),0],
                'values': [hoja.name,1,1,len(cantidades),1]
        })
        grafico.set_x_axis({
            'name':'Fechas',
            'name-font':{'size':16,'bold':True},
            'num_font':{'italic':True},
        })
        hoja.insert_chart('E3', grafico)
        documento.close()

        QtGui.QMessageBox.information(self, "Listado" , "El listado ha sido generado con exito")

    def generarExcelClientes(self):
        """
            Genera el documento Excel correspondiente a
            los clientes de la farmacia
        :return: None
        """
        datosClientes=[]
        for cliente in (ClienteModel.buscarTodos("dni",self.sesion).all()):
            datosUnCliente=[]
            datosUnCliente.append(cliente.dni)
            datosUnCliente.append(cliente.nombre)
            datosUnCliente.append(cliente.apellido)
            datosUnCliente.append(cliente.direccion)
            datosUnCliente.append(cliente.telefono)
            datosClientes.append(datosUnCliente)




        documento=xlsxwriter.Workbook('Excel/Clientes.xlsx')
        hoja=documento.add_worksheet('Clientes')
        bold = documento.add_format({'bold': 1,})
        bold.set_align('center')
        hoja.write('A1', 'DNI', bold)
        hoja.write('B1', 'Nombre', bold)
        hoja.write('C1', 'Apellido', bold)
        hoja.write('D1', 'Direccion', bold)
        hoja.write('E1', 'Telefono', bold)
        i = 2
        for cliente in datosClientes:
            row = 'A%(numero)d' % {"numero":i}
            hoja.write_row(row, cliente)
            i += 1

        documento.close()

        QtGui.QMessageBox.information(self, "Listado", "El listado ha sido generado con exito")

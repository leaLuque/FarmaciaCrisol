# -*- coding:utf-8 -*-
__author__ = 'waldo'

import os
from datetime import datetime

import pycha.bar
import cairo
import pycha.line
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
        """
        Constructor de la clase Listar.
        :param mdi:
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
                f = open('reportes/listadoProductosStock.html','w')
                data = self.productosStock(lote_producto)
                self.diagramaBarras(data)
                message = self.htmlProductosStock(lote_producto)
                f.write(message)
                f.close()
                pdfkit.from_file('reportes/listadoProductosStock.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')
        elif (self.listado=="Ventas Realizadas"):
            fechaDesde = self.deFechaDesde.dateTime()
            fechaHasta = self.deFechaHasta.dateTime()

            if fechaDesde > fechaHasta:
                QtGui.QMessageBox.information(self,"Aviso","La fecha Hasta es mayor que la fecha Desde")

            elif self.rbtnExcel.isChecked():
                self.generarExcelVentas(fechaDesde,fechaHasta)

            else:
                pass
            """else:
                facturas = Factura.buscarTodos(Factura.numero, self.sesion).all()
                remitos = Remito.buscarTodos(Remito.numero, self.sesion).all()
                data = self.cantidadVentas(facturas, remitos)
                #self.diagramaLinea(data)
                f = open('reportes/listadoVentas.html','w')
                ventas = self.cantidadVentas(facturas, remitos)
                message = self.htmlVentas(ventas)
                f.write(message)
                f.close()
                pdfkit.from_file('reportes/listadoVentas.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')"""
        else:
            if self.rbtnExcel.isChecked():
                self.generarExcelClientes()
            else:
                clientes = Cliente.buscarTodos(Cliente.dni, self.sesion).all()
                f = open('reportes/listadoClientes.html','w')
                message = self.htmlCliente(clientes)
                f.write(message)
                f.close()
                pdfkit.from_file('reportes/listadoClientes.html', 'reportes/list.pdf')
                os.system('evince reportes/list.pdf &')

    def htmlProductosStock(self, lote_producto):
        """
        Genera el html usado para generar el pdf final del listado de los productos en stock.
        :param lote_producto: arreglo que contiene todos los productos y sus diferentes lotes.
        :return: hmtl
        """
        #TODO esta bien q se de de baja un producto para el q hay stock???
        # hay q listar los dados de baja?? esto depende de la resp a la preg anterior.
        i = 0
        html = """<html>
            <head>
            </head>
            <body>
            <div id="contenedor">
              <header id="encabezado">
                <h1 align="center">Listado Productos en Stock</h1>
              </header>
              <div id="items">
                <table border width="100%">
                    <th bgcolor="#38B0DE">Producto</th>
                    <th bgcolor="#38B0DE">Nro Lote</th>
                    <th bgcolor="#38B0DE">Descripción</th>
                    <th bgcolor="#38B0DE">Cantidad</th>"""
        for lp in lote_producto:
            if (lp.getCantidad() > 0):
                i += 1
                producto = Producto.buscar(Producto.codigo_barra, self.sesion, lp.getIdProducto()).first()
                html += """<tr><td width="10%">""" + str(i)
                html += """</td><td width="10%">""" + str(lp.getIdLote())
                html += """</td><td width="70%">""" + str(producto.getIdMedicamento()) \
                        + """ """ + str(producto.getIdPresentacion())
                html += """</td><td width="10%">""" + str(lp.getCantidad())
                html += """</td></tr>"""
        html += """</table></div></div></body></html>"""
        html += """<img src="diagBarra.png">"""
        return html

    def htmlCliente(self, clientes):
        """
        Genera el html usado para generar el pdf final del listado de los Clientes.
        :param clientes: arreglo que contiene todos los clientes.
        :return: hmtl
        """
        i = 0
        html = """<html>
            <head>
            </head>
            <body>
            <div id="contenedor">
              <header id="encabezado">
                <h1 align="center">Listado Clientes</h1>
              </header>
              <div id="items">
                <table border width="100%">
                    <th bgcolor="#38B0DE">Cliente</th>
                    <th bgcolor="#38B0DE">Nombre y Apellido</th>
                    <th bgcolor="#38B0DE">DNI</th>
                    <th bgcolor="#38B0DE">Domicilio</th>
                    <th bgcolor="#38B0DE">Teléfono</th>"""
        for cliente in clientes:
            i += 1
            html += """<tr><td width="10%">""" + str(i)
            html += """</td><td width="35%">""" + str(cliente.getNombre()) + """ """ + str(cliente.getApellido())
            html += """</td><td width="10%">""" + str(cliente.getDni())
            html += """</td><td width="35%">""" + str(cliente.getDireccion())
            html += """</td><td width="10%">""" + str(cliente.getTelefono())
            html += """</td></tr>"""
        html += """</table></div></div></body></html>"""
        return html

    #TODO html de factura, nota de credito, remito.

    def htmlVentas(self, ventas):
        """
        Genera el html usado para generar el pdf final del listado de las Ventas realizadas.
        :param ventas: arreglo que contiene todas las ventas realizadas.
        :return: hmtl
        """
        i = 0
        html = """<html>
            <head>
            </head>
            <body>
            <div id="contenedor">
              <header id="encabezado">
                <h1 align="center">Listado Ventas Realizadas</h1>
              </header>
              <div id="items">
                <table border width="100%">
                    <th bgcolor="#38B0DE">Fehca de Emision</th>
                    <th bgcolor="#38B0DE">Cantidad</th>"""
        for fecha, cant in ventas:
            i += 1
            html += """<tr><td width="50%">""" + str(fecha)
            html += """</td><td width="50%">""" + str(cant)
            html += """</td></tr>"""
        html += """</table></div></div></body></html>"""
        html += """<img src="diagLinea.png">"""
        return html

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
                    'initialColor': 'blue',
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

    def cantidadVentas(self, facturas, remitos):
        """
        Devuelve la cantidad de ventas realizadas (factura y remito) por fecha.
        :param facturas: arreglo que contiene todas las facturas correpondientes a las ventas realizadas.
        :param remitos: arreglo que contiene todos los remitos correpondientes a las ventas realizadas.
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
        self.diagramaLinea(fch_cant, ventas_rem)
        for fch, cant in ventas_rem:
            fch_cant.append((fch, cant))
        return fch_cant

    def diagramaLinea(self, data1, data2):
        """
        Genera un diagraga de lineas en una imagen png a incluir en el pdf,
        de acuerdo a los datos pasados por parametro.
        :param data1: datos de la línea 1.
        :param data2: datos de la línea 2
        :return:
        """
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)

        dataSet = (
            ('lines', [(i, l[1]) for i, l in enumerate(data1)]),
            ('lines_2', [(i, l[1]) for i, l in enumerate(data2)]),
            )

        options = {
            'axis': {
                'x': {
                    'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(data1)],
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
                'hide': True,
            },
        }
        chart = pycha.line.LineChart(surface, options)

        chart.addDataset(dataSet)
        chart.render()

        surface.write_to_png('reportes/diagLinea.png')

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

    def generarExcelVentas(self,fechaDesde, fechaHasta):
        """
            Crea el documento Excel correspondiente a las ventas realizadas en
            un periodo de tiempo dado
        :param fechaDesde Fecha de Inicio de Listado:
        :param fechaHasta Fecha de Fin de Listado:
        :return None :
        """
        ventas={}
        for factura in (FacturaModel.buscarTodos("numero",self.sesion).all()):
            if factura.fecha_emision >= fechaDesde and factura.fecha_emision <= fechaHasta:
                if (factura.fecha_emision in ventas):
                    ventas[factura.fecha_emision]+=1
                else:
                    ventas[factura.fecha_emision]=1
        for remito in (RemitoModel.buscarTodos("numero",self.sesion).all()):
            if remito.fecha_emision >= fechaDesde and remito.fecha_emision <= fechaHasta:
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
        hoja.write('A1','DNI',bold)
        hoja.write('B1','Nombre',bold)
        hoja.write('C1','Apellido',bold)
        hoja.write('D1','Direccion',bold)
        hoja.write('E1','Telefono',bold)
        i=2
        for cliente in datosClientes:
            row='A%(numero)d' % {"numero":i}
            hoja.write_row(row,cliente)
            i+=1

        documento.close()

        QtGui.QMessageBox.information(self, "Listado" , "El listado ha sido generado con exito")

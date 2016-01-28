# -*- coding:utf-8 -*-
__author__ = 'leandro'

import os

import pdfkit


def generarNotaCredito(data):
    """
        Genera la Nota de Credito correspondiente
        para ser impresa.
        :return:
    """

    archivo = open("Comprobantes/nota_credito.html","r")
    contenido = archivo.read()
    archivo.close()

    body = ""
    total = 0

    for dato in data["detalles"]:
        producto = dato[0]
        cantidad = dato[1]
        descuento = dato[2]
        importe = "%.2f" % dato[3]
        total+=float(importe)
        cadena = """<tr>

            <td><strong>{producto}</strong></td>
            <td class="text-right">{cantidad}</td>
            <td class="text-right">{descuento}</td>
            <td class="text-right">{importe}</td>
          </tr>""".format(producto=producto,cantidad=cantidad,descuento=descuento,importe=importe)
        body+=cadena



    contenido_nuevo = contenido.format(numero=data["numero"],fecha=data["fecha"].strftime("%d/%m/%y"),
                                       nombre = "----", direccion = "----", telefono = "----", contenido = body,
                                       total = total)

    archivo = open("Comprobantes/nota.html","w")
    archivo.write(contenido_nuevo)
    archivo.close()

    pdfkit.from_file("Comprobantes/nota.html","nota.pdf")
    os.system("evince nota.pdf &")

def generarFactura(data):
    """
        Generar la factura correspondiente, para ser impresa
        :param data Diccionario que contiene informacion asociada con el comprobante:
    """
    archivo = open("Comprobantes/factura.html","r")
    contenido = archivo.read()
    archivo.close()


    body = ""
    total = 0

    for dato in data["detalles"]:
        producto = dato[0]
        cantidad = dato[1]
        descuento = float(dato[3])*100
        importe = dato[2]
        total+=float(importe)
        cadena = """<tr>

            <td><strong>{producto}</strong></td>
            <td class="text-right">{cantidad}</td>
            <td class="text-right">{descuento}</td>
            <td class="text-right">{importe}</td>
          </tr>""".format(producto=producto,cantidad=cantidad,descuento=descuento,importe=importe)
        body+=cadena



    contenido_nuevo = contenido.format(numero=data["numero"],fecha=data["fecha"].strftime("%d/%m/%y"),
                                       nombre = "----", direccion = "----", telefono = "----", contenido = body,
                                       total = total, forma_pago=data["formaPago"])


    archivo = open("Comprobantes/nota.html","w")
    archivo.write(contenido_nuevo)
    archivo.close()

    pdfkit.from_file("Comprobantes/nota.html","factura.pdf")
    os.system("evince factura.pdf &")

def generarRremito(data):

    """
        Generar el remito correspondiente, para ser impresa
        :param data Diccionario que contiene informacion asociada con el comprobante:

        Estructura del diccionario

        numero = Contiene el numero del remito
        fecha = Contiene fecha del remito
        datosCliente = Contiene un diccionario con los datos del cliente
                        El mismo contiene: nombre, apellido, telefono, direccion
        detalles = Contiene el arreglo con los detalles del remito

    """


    archivo = open("Comprobantes/remito.html","r")
    contenido = archivo.read()
    archivo.close()

    body = ""
    total = 0

    for dato in data["detalles"]:
        producto = dato[0]
        cantidad = dato[1]
        importe = dato[2]
        unitario = float(importe)/int(cantidad)
        total+=float(importe)
        cadena = """<tr>

            <td><strong>{producto}</strong></td>
            <td class="text-right">{cantidad}</td>
            <td class="text-right">{unitario}</td>
            <td class="text-right">{importe}</td>
          </tr>""".format(producto=producto,cantidad=cantidad,unitario=unitario,importe=importe)
        body+=cadena


    contenido_nuevo = contenido.format(numero = data["numero"],fecha = data["fecha"].strftime("%d/%m/%y"),
                                       nombre = data["datosCliente"]["nombre"], apellido = data["datosCliente"]["apellido"],
                                       telefono = data["datosCliente"]["telefono"], direccion = data["datosCliente"]["direccion"],
                                       contenido = body,
                                       total = total)

    archivo = open("Comprobantes/nota.html","w")
    archivo.write(contenido_nuevo)
    archivo.close()

    pdfkit.from_file("Comprobantes/nota.html","temp_remito.pdf")
    os.system("evince temp_remito.pdf &")


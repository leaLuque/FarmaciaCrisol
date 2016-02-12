# -*- coding:utf-8 -*-
import re

from PyQt4 import QtCore
from PyQt4.QtCore import QUrl, SIGNAL
from PyQt4.QtWebKit import QWebView, QWebPage

from gui import MdiWidget
from ventanas.vtnAyuda import Ui_vtnAyuda

class Ayuda (MdiWidget, Ui_vtnAyuda):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.view = QWebView(self)
        self.id_menu = [
            ("id_menu_usuario", [{1:"id_ing", 2:"ingresar()", 3:"» Ingresar"},
                                 {1:"id_salir", 2:"salir()", 3:"» Salir"}]),
            ("id_menu_venta", [{1:"id_vent_rem", 2:"ventaRem()", 3:"» Venta con Remito"},
                               {1:"id_reg_cob_rem", 2:"regCobRem()", 3:"» Registrar Cobro Remito"},
                               {1:"id_mod_rem", 2:"modRem()", 3:"» Modificar Remito"},
                               {1:"id_baja_rem", 2:"bajaRem()", 3:"» Baja Remito"},
                               {1:"id_vent_cont", 2:"ventaContado()", 3:"» Venta Contado"},
                               {1:"id_reint_clt", 2:"reintegroCliente()", 3:"» Reintegro Cliente"},
                               {1:"id_dev_clt", 2:"devCliente()", 3:"» Devolución Cliente"}]),
            ("id_menu_producto", [{1:"id_alta_prod", 2:"altaProd()", 3:"» Alta Producto"},
                                  {1:"id_baja_prod", 2:"bajaProd()", 3:"» Baja Producto"},
                                  {1:"id_mod_prod", 2:"modProd()", 3:"» Modificación Producto"},
                                  {1:"id_fracc_prod", 2:"fraccProd()", 3:"» Fraccionar Producto"},
                                  {1:"id_alta_med", 2:"altaMed()", 3:"» Alta Medicamento"},
                                  {1:"id_baja_med", 2:"bajaMed()", 3:"» Baja Medicamento"},
                                  {1:"id_mod_med", 2:"modMed()", 3:"» Modificación Medicamento"},
                                  {1:"id_alta_mon", 2:"altaMon()", 3:"» Alta Monodroga"},
                                  {1:"id_baja_mon", 2:"bajaMon()", 3:"» Baja Monodroga"},
                                  {1:"id_mod_mon", 2:"modMon()", 3:"» Modificación Monodroga"},
                                  {1:"id_alta_pres", 2:"altaPres()", 3:"» Alta Presentación"},
                                  {1:"id_baja_pres", 2:"bajaPres()", 3:"» Baja Presentación"},
                                  {1:"id_mod_pres", 2:"modPres()", 3:"» Modificación Presentación"},
                                  {1:"id_alta_lote", 2:"altaLote()", 3:"» Alta Lote"},
                                  {1:"id_mod_lote", 2:"modLote()", 3:"» Modificación Lote"},
                                  {1:"id_ajuste_neg_stock", 2:"ajusteNegStock()", 3:"» Ajuste Negativo de Stock"}]),
            ("id_menu_cliente", [{1:"id_alta_clt", 2:"altaCliente()", 3:"» Alta Cliente"},
                                 {1:"id_baja_clt", 2:"bajaCliente()", 3:"» Baja Cliente"},
                                 {1:"id_mod_clt", 2:"modCliente()", 3:"» Modificación Cliente"}]),
            ("id_menu_listado", [{1:"id_gen_list", 2:"genList()", 3:"» Generar Listados"}])
        ]
        self.view.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.view.connect(self.view, SIGNAL("linkClicked(const QUrl&)"), self.linkClicked)
        self.leerTxt("Ingresar", "img/capturas/ingresar.png", "ingresar", "id_menu_usuario")
        self.view.load(QUrl("web/index.html"))
        self.view.show()
        self.verticalLayout.addWidget(self.view)


    def linkClicked(self, url):
        self.view.page().mainFrame().addToJavaScriptWindowObject("Ayuda", self)
        self.view.page().mainFrame().evaluateJavaScript("id = getId(); Ayuda.cargarContenido(id);")
        self.view.reload()

    @QtCore.pyqtSlot(str)
    def cargarContenido(self, id):
        if (id == "id_menu_usuario" or id == "id_ing"):
            self.leerTxt("Ingresar", "img/capturas/ingresar.png", "ingresar", "id_menu_usuario")
        elif (id == "id_salir"):
            self.leerTxt("Salir", "img/capturas/salir.png", "salir", "id_menu_usuario")
        elif (id == "id_menu_venta" or id == "id_vent_rem"):
            self.leerTxt("Venta con Remito", "img/capturas/ventaRemito.png", "ventaRem", "id_menu_venta")
        elif (id == "id_reg_cob_rem"):
            self.leerTxt("Registrar Cobro Remito", "img/capturas/regCobRem.png", "regCobroRem", "id_menu_venta")
        elif (id == "id_mod_rem"):
            self.leerTxt("Modificar Remito", "img/capturas/modRem.png", "modRem", "id_menu_venta")
        elif (id == "id_baja_rem"):
            self.leerTxt("Baja Remito", "img/capturas/bajaRem.png", "bajaRem", "id_menu_venta")
        elif (id == "id_vent_cont"):
            self.leerTxt("Venta Contado", "img/capturas/ventaContado.png", "ventaContado", "id_menu_venta")
        elif (id == "id_reint_clt"):
            self.leerTxt("Reintegro Cliente", "img/capturas/reintCliente.png", "reintCliente", "id_menu_venta")
        elif (id == "id_dev_clt"):
            self.leerTxt("Devolución Cliente", "img/capturas/devCliente.png", "devCliente", "id_menu_venta")
        elif (id == "id_menu_producto" or id == "id_alta_prod"):
            self.leerTxt("Alta Producto", "img/capturas/altaProd.png", "altaProd", "id_menu_producto")
        elif (id == "id_baja_prod"):
            self.leerTxt("Baja Producto", "img/capturas/bajaProd.png", "bajaProd", "id_menu_producto")
        elif (id == "id_mod_prod"):
            self.leerTxt("Modificar Producto", "img/capturas/modProd.png", "modProd", "id_menu_producto")
        elif (id == "id_fracc_prod"):
            self.leerTxt("Fraccionar Producto", "img/capturas/fracProd.png", "fraccProd", "id_menu_producto")
        elif (id == "id_alta_med"):
            self.leerTxt("Alta Medicamento", "img/capturas/altaMed.png", "altaMed", "id_menu_producto")
        elif (id == "id_baja_med"):
            self.leerTxt("Baja Medicamento", "img/capturas/bajaMed.png", "bajaMed", "id_menu_producto")
        elif (id == "id_mod_med"):
            self.leerTxt("Modificar Medicamento", "img/capturas/modMed.png", "modMed", "id_menu_producto")
        elif (id == "id_alta_mon"):
            self.leerTxt("Alta Monodroga", "img/capturas/altaMon.png", "altaMon", "id_menu_producto")
        elif (id == "id_baja_mon"):
            self.leerTxt("Baja Monodroga", "img/capturas/bajaMon.png", "bajaMon", "id_menu_producto")
        elif (id == "id_mod_mon"):
            self.leerTxt("Modificar Monodroga", "img/capturas/modMon.png", "modMon", "id_menu_producto")
        elif (id == "id_alta_pres"):
            self.leerTxt("Alta Presentación", "img/capturas/altaPres.png", "altaPres", "id_menu_producto")
        elif (id == "id_baja_pres"):
            self.leerTxt("Baja Presentación", "img/capturas/bajaPres.png", "bajaPres", "id_menu_producto")
        elif (id == "id_mod_pres"):
            self.leerTxt("Modificar Presentación", "img/capturas/modPres.png", "modPres", "id_menu_producto")
        elif (id == "id_alta_lote"):
            self.leerTxt("Alta Lote", "img/capturas/altaLote.png", "altaLote", "id_menu_producto")
        elif (id == "id_mod_lote"):
            self.leerTxt("Modificar Lote", "img/capturas/modLote.png", "modLote", "id_menu_producto")
        elif (id == "id_ajuste_neg_stock"):
            self.leerTxt("Ajuste Negativo Stock", "img/capturas/ajusteNegStock.png", "ajusteNegStock", "id_menu_producto")
        elif (id == "id_menu_cliente" or id == "id_alta_clt"):
            self.leerTxt("Alta Cliente", "img/capturas/altaCliente.png", "altaCliente", "id_menu_cliente")
        elif (id == "id_baja_clt"):
            self.leerTxt("Baja Cliente", "img/capturas/bajaCliente.png", "bajaCliente", "id_menu_cliente")
        elif (id == "id_mod_clt"):
            self.leerTxt("Modificar Cliente", "img/capturas/modCliente.png", "modCliente", "id_menu_cliente")
        elif (id == "id_menu_listado" or id == "id_gen_list"):
            self.leerTxt("Generar Listado", "img/capturas/listar.png", "genList", "id_menu_listado")

    def leerTxt(self, titulo, imagen, pal_clave, id_menu_onclick):
        plantilla = open("Ayuda/contenidoPlantilla.html", "r")
        contenido_plantilla = plantilla.read()
        plantilla.close()

        body = """<h1 id="titulo"> {titulo} </h1>
            <div class="imgbox">
                <img src= {imagen} />
            </div>""".format(titulo=titulo, imagen=imagen)

        archivo = open("Ayuda/ayuda.txt", "r")
        contenido_txt = archivo.read()
        archivo.close()
        # cada m es un objeto tipo matcher
        patron = re.compile('(#start_' + pal_clave +').*(#end_' + pal_clave + ')', re.DOTALL)
        for m in re.finditer(patron, contenido_txt):
            # itera sobre cada parrafo encontrado
            sub = re.sub('#start_' + pal_clave, "", m.group(0))
            sub = re.sub('#end_' + pal_clave, "", sub)
            for match in re.split('#parrafo', sub):
                parrafo = """<p><strong><h3> {parrafo} </h3></strong></p>""".format(parrafo=match)
                body += parrafo

        indice = """"""
        for id, menu in self.id_menu:
            if (id == id_menu_onclick):
                for m in menu:
                    ind = """<li> <a href="#" id={id} onclick={onclick}><h3>{txt}</h3></a></li>""".\
                        format(id=m[1], onclick=m[2], txt=m[3])
                    indice += ind
        contenido_nuevo = contenido_plantilla.format(contenido=body, indice=indice)
        archivo = open("web/index.html", "w")
        archivo.write(contenido_nuevo)
        archivo.close()

    def ayudaVentana(self, ventana):
        self.cargarContenido(ventana)
        self.view.reload()

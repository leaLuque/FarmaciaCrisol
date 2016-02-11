# coding=utf-8
__author__ = 'waldo'

from PyQt4 import QtGui

from validarDatos import ValidarDatos

class MyMdi(QtGui.QMdiSubWindow):
    """
    Lógica de las ventanas.
    """
    def __init__(self, mainWindow):
        """
        Constructor de la clase MyMdi.
        :param mainWindow:
        :return:
        """
        super(MyMdi, self).__init__(mainWindow)
        self.mainWindow = mainWindow

    def closeEvent(self, event):
        """
        Oculta la ventana cuando se dispara el evento close.
        :param event:
        :return:
        """
        self.hide()
        #super(MyMdi, self).closeEvent(event)

    def window(self):
        """
        Devuelve l refenrencia a la ventana principal que contiene las subventanas.
        :return: mainWindow
        """
        return self.mainWindow

    def show(self):
        """
        Hace visible la ventena que se encontraba oculta.
        :return:
        """
        super(MyMdi, self).show()
        self.setFocus()
        if self.isMinimized():
            self.showNormal()

class MdiWidget(QtGui.QWidget):
    """
    Lógica de los widgets de las ventanas.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase MdiWidget.
        :param mdi:
        :return:
        """
        QtGui.QWidget.__init__(self, mdi)
        self.setupUi(self)


    def validadores(self, model):
        """
        Setea los campo requeridos (obligatorios) y los campos no requeridos (opcionales).
        Para una ventana determinada.
        :param model: referencia a la ventana.
        :return:
        """
        ##Esta parte analiza los campos requeridos para el cliente
        self.camposRequeridos = [getattr(self, "line%s" % campo.title()) for campo in model.requeridos]
        ValidarDatos.setValidador(self.camposRequeridos)
        ##Esta parte analiza los campos que son opcionales
        camposNoRequeridos=[getattr(self, "line%s" % campo.title()) for campo in model.noRequeridos]
        ValidarDatos.setValidador(camposNoRequeridos)

    def showMsjEstado(self, msj):
        """
        Muestra un mensaje en la barra de estado de la la ventana principal.
        :param msj: mensaje a ser mostrado en la barra de estado.
        :return:
        """
        self.mdi().window().setBarraEstado(msj)

    def mdi(self):
        """
        Devuelve una referencia a la ventana padre de la ventana.
        :return:
        """
        return self.parent()

    def cargarObjetos(self, tabla, queryset, atributos):
        """
        Carga la tabla de la ventana con los datos recibidos.
        :param tabla: tabla a rellenar con los datos.
        :param queryset: datos a colocar en la tabla.
        :param atributos: atributos correspondientes a los datos.
        :return:
        """
        for n, obj in enumerate(queryset):
            tabla.insertRow(n)
            for m, campo in enumerate(atributos):
                tabla.setItem(n, m, QtGui.QTableWidgetItem("%s" % getattr(obj, campo)))

    def limpiarTabla(self, tabla):
        """
        Vacia la tabla.
        :param tabla: tabla a vaciar.
        :return:
        """
        tabla.clearContents()
        tabla.setRowCount(0)

    def itemSeleccionado(self, tabla):
        """
        Devuelve el item (fila) de la tabla que fue seleccionado.
        :param tabla:
        :return:
        """
        return str(tabla.item(tabla.currentItem().row(), 0).text())

    def getContenidoTabla(self,tabla):
        """
            Devuelve la informacion actual de la tabla en
            un arreglo que contiene info de cada fila
        :param tabla QTableWidget de la ventana:
        :return Diccionario con informacion:
        """
        dataRow = []
        dataTable = {}

        for row in range(0,tabla.rowCount()):
            if not tabla.isRowHidden(row):
                for col in range(0,tabla.columnCount()):
                    dataRow.append(str(tabla.item(row,col).text()))
                dataTable[row] = dataRow
                dataRow = []

        return dataTable

    def getAllTabla(self,tabla):
        """
            Devuelve la informacion actual de la tabla en
            un arreglo que contiene info de cada fila
        :param tabla QTableWidget de la ventana:
        :return Diccionario con informacion:
        """
        dataRow = []
        dataTable = {}

        for row in range(0,tabla.rowCount()):
            for col in range(0,tabla.columnCount()):
                dataRow.append(str(tabla.item(row,col).text()))
            dataTable[row] = dataRow
            dataRow = []

        return dataTable

    def addHandlerSignal(self):
        pass

    def setVentana(self, ventana):
        """
        Setea el nombre de la ventana.
        :param ventana: Nombre de la ventana.
        :return:
        """
        self.ventana = ventana

    def getVentana(self):
        """
        Devuelve el nombre de la ventana.
        :return: Ventana.
        """
        return self.ventana

    def cancelarVentana(self):
        pass
__author__ = 'waldo'
from baseDatos.productos.objetoBase import ObjetoBase
class Monodroga(ObjetoBase):
    requeridos = ("nombre",)
    noRequeridos = ()

    def __init__(self, nombre, tipo_venta, descripcion):
        ObjetoBase.__init__(self)
        self.nombre=nombre
        self.tipo_venta=tipo_venta
        self.descripcion=descripcion

    def getNombre(self):
        return self.nombre

    def getTipoVenta(self):
        return self.tipo_venta

    def getDescripcion(self):
        return self.descripcion

    def setTipoVenta(self, tipo_venta):
        self.tipo_venta = tipo_venta

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setNombre(self, nombre):
        self.nombre = nombre

class Medicamento(ObjetoBase):
    requeridos = ("nombre_med", "nombre_mon")
    noRequeridos = ()

    def __init__(self, nombre_comercial, id_monodroga, cantidad_monodroga):
        ObjetoBase.__init__(self)
        self.nombre_comercial=nombre_comercial
        self.id_monodroga=id_monodroga
        self.cantidad_monodroga=cantidad_monodroga

    def getNombreComercial(self):
        return self.nombre_comercial

    def getIdMonodroga(self):
        return self.id_monodroga

    def getCantidadMonodroga(self):
        return self.cantidad_monodroga

    def setNombreComercial(self, nombre_comercial):
        self.nombre_comercial = nombre_comercial

    def setIdMonodroga(self, id_monodroga):
        self.id_monodroga = id_monodroga

    def setCantidadMonodroga(self, cantidad_monodroga):
        self.cantidad_monodroga = cantidad_monodroga

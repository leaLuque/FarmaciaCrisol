#coding=utf-8
__author__ = 'waldo'

from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.exc import FlushError

class ObjetoBase(object):
    """
    Objeto base del cual heredan los objetos a almacenar en la base de datos.
    """
    def __init__(self):
        """
        Constructor de la clase ObjetoBase.
        :return:
        """
        self.baja = False

    def getBaja(self):
        """
        Devuelve el estado de baja del objeto.
        :return: baja
        """
        return self.baja

    def setBaja(self, baja):
        """
        Setea el estado de baja del objeto.
        :param baja:
        :return:
        """
        self.baja = baja

    def guardar(self, sesion):
        """
        Guarda el objeto en la base de datos.
        :param sesion:
        :return: bool
        """
        try:
            sesion.add(self)
            sesion.commit()
            return True
        except IntegrityError:
            sesion.rollback()
            return False
        except FlushError:
            sesion.rollback()
            return False
        except InvalidRequestError:
            sesion.rollback()
            sesion.add(self)
            sesion.commit()
            return True

    # ----- Baja logica del objeto en la base
    def borrar(self, sesion):
        """
        Da de baja (lógica) del objeto almacenado en la base de datos.
        :param sesion:
        :return:
        """
        self.setBaja(True)
        sesion.commit()

    def modificar(self, sesion):
        """
        Modifica los datos del objeto almacenado en la base de datos.
        :param sesion:
        :return:
        """
        sesion.commit()

    def alta(self, sesion):
        """
        Da de alta un objeto que se encuentra dado de baja en la base de datos.
        :param sesion:
        :return:
        """
        self.setBaja(False)
        sesion.commit()

    @classmethod
    def buscarLike(cls, campo, sesion, varBusq):
        """
        Devuelve un arreglo con los objetos que coinciden o se asemejan con el contenido de la variable de busquedan.
        :param campo:
        :param sesion:
        :param varBusq:
        :return:
        """
        return sesion.query(cls).filter(campo.like('%'+varBusq+'%'), cls.baja == False).order_by(campo)

    @classmethod
    def buscarAlta(cls, campo, sesion, varBusq):
        """
        Devuelve un arreglo con el objeto que coincide con el contenido de la variable de busqueda,
        y que no fue dado de baja.
        :param campo:
        :param sesion:
        :param varBusq:
        :return:
        """
        return sesion.query(cls).filter(campo == varBusq, cls.baja == False)

    @classmethod
    def buscarTodos(cls, campo, sesion):
        """
        Devuelve un arreglo con todos los objetos almacenados en la base de datos que no fueron dados de baja.
        :param campo:
        :param sesion:
        :return:
        """
        if hasattr(cls, 'baja'):
            return sesion.query(cls).filter(cls.baja == False).order_by(campo)
        else:
            return sesion.query(cls).order_by(campo)

    @classmethod
    def buscar(cls, campo, sesion, varBusq):
        """
        Devuelve un arreglo con el objeto que coincide con el contenido de la variable de busqueda,
        y que fue o no dado de baja.
        :param campo:
        :param sesion:
        :param varBusq:
        :return:
        """
        return sesion.query(cls).filter(campo == varBusq)

    def bajaFisica(self,sesion):
        """
            Da de baja fisicamente el objeto
        :param sesion Sesion actual con la Base de Datos:
        :return:
        """
        sesion.delete(self)
        sesion.commit()
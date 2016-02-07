__author__ = 'leandro'


class PoolOfWindows():

    """
        Clase que modela un Pool, en donde se mantiene referencias
        de todas las ventanas existentes.
    """

    pool = {}

    @classmethod
    def addPool(cls,pool):
        """
            Añade el conjunto de ventanas
            pasadas como parametro
        :param pool Diccionario que mantiene Nombre de Ventana y Referencia:
        :return:
        """
        cls.pool = pool

    @classmethod
    def getVentana(cls,name_ventana):
        """
            Devuelve una referencia a una ventana particular
            inficada por parametro
        :param name_ventana Nombre de ventana:
        :return Referencia de ventana:
        """
        return cls.pool[name_ventana]

    @classmethod
    def getPool(cls):
        """
            Devuelve el pool de ventanas
        :return Diccionario con ventanas:
        """
        return cls.pool

    @classmethod
    def setHandlers(cls):
        """
            Setea los manejadores de señales entre
            ventanas
        :return:
        """
        for obj in cls.pool.values():
            obj.addHandlerSignal()
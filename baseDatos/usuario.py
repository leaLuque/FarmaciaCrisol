from .objetoBase import ObjetoBase

class Usuario(ObjetoBase):
    """
        Clase que modela al Usuario en el sistema
    """
    def __init__(self, id_usuario, password, role):
        """
            Constructor de la clase Usuario
        :param id_usuario Nickname del usuario:
        :param password Constraseña alfanumérica:
        :param role Role del usuario:
        :return:
        """
        self.id_usuario=id_usuario
        self.password=password
        self.role=role

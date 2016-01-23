from .objetoBase import ObjetoBase

class Usuario(ObjetoBase):
    def __init__(self, id_usuario, password, role):
        self.id_usuario=id_usuario
        self.password=password
        self.role=role

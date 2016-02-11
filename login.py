
from baseDatos.usuario import Usuario

class Login():
    """
        Esta clase se encarga del logeo de los usuarios que utilizan el sistema
    """
    def __init__(self, id_usuario, password, session):
        """
            Constructor de la clase Login
        :param id_usuario:
        :param password:
        :param session:
        :return:
        """
        self.id_usuario = id_usuario
        self.password = password
        self.session = session

    def loginValido(self):
        """
            Esta funcion retorna el rol correspondiente al usuario (si existe) y no
            devuelve None para indicar que el usuario no esta registrado
        :return role:
        """
        usuario = self.session.query(Usuario).filter(Usuario.id_usuario == self.id_usuario,
                                                      Usuario.password == self.password).first()
        if usuario:
            return usuario.role
        else:
            return None
# #Esta clase se encarga del logeo de los usuarios que utilizan el sistema
from baseDatos.usuario import Usuario
class Login():
    #Constructor que recibe el id del usuario, la pass ingresada y la session con la DB
    def __init__(self, id_usuario, password, session):
        self.id_usuario = id_usuario
        self.password = password
        self.session = session

    #Esta funcion retorna el rol correspondiente al usuario (si existe) y no
    #devuelve None para indicar que el usuario no esta registrado
    def loginValido(self):
        usuario = self.session.query(Usuario).filter(Usuario.id_usuario == self.id_usuario,
                                                      Usuario.password == self.password).first()
        if usuario:
            return usuario.role
        else:
            return None
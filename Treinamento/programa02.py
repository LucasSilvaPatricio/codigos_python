from abc import ABC, abstractmethod

class Validar(ABC):
    def __init__(self):
        self.validacao = False 
    
    @abstractmethod
    def validar(self) -> bool:
        self.validacao = True 
        return self.validacao


class Login(Validar):

    USER = 'adm'
    PASSWORD = 'adm123'

    def __init__(self):
        self._usuario = ''
        self.senha = ''
    
    @property 
    def usuario(self):...
    
    @usuario.setter
    def usuario(self,usuario):
        self._usuario = usuario

    def validar(self):
        validacao = self.usuario == Login.USER and self.senha == Login.PASSWORD
        if validacao:
            return super().validar

        return False

login = Login()
login.usuario = ''
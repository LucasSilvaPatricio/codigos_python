from abc import ABC, abstractmethod

class Login(ABC):

    def __init__(self, user=None, password=None):
        self._session = False
        self._user = user
        self._password = password

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @user.setter
    @abstractmethod
    def user(self, user):...

    @password.setter
    @abstractmethod 
    def password(self, password):...
  
    def login(self):
        self._session = True
   
    def logout(self):
        self._session = False

class GetUsersMaxin:
    def __init__(self):
        self.__users = []
    
    @property
    def users(self):
        return self.__users
    
    @users.setter 
    def users(self, user):
        self.__users = user 

    def getUserByQuantity(self, quant=1):
        for i in range(0,quant):
            print(f'User {i}')
            user = input('Digite um usuario: ')
            password = input('Digite a senha: ')
            self.users.append([{"name":user}, {"password": password}])

class SystemLogin(Login, GetUsersMaxin):

    # usuarios permitidos a fazer login 
    USER_DB = 'adm'
    PASS_DB = '123'

    def __init__(self, user=None, password=None):
        self.users = []
        super().__init__(user, password)
    
    @Login.user.setter 
    def user(self, user):
        self._user = user 

    @Login.password.setter 
    def password(self, password):
        self._password = password

    def login(self):
        for usuario, senha in self.users:

            if usuario['name'] == SystemLogin.USER_DB and senha['password'] == SystemLogin.PASS_DB:
                print(f'Usuario {usuario["name"]} está Logado.')
                super().login()
            else:
                print(f'Falha ao logar o usuario {usuario["name"]}!')

sysl = SystemLogin()
sysl.getUserByQuantity(3)
sysl.login()




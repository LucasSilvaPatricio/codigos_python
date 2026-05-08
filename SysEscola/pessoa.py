class Pessoa:

    def __init__(self):
        self._nome = None 
        self._cpf = None 
        self._idade = None 
        self._sexo = None 
        self._nascimento = None

    #getters

    @property
    def nome(self):
        return self._nome 
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def sexo(self):
        return self._sexo

    @property
    def nascimento(self):
        return self._nascimento
    

    # setters
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @cpf.setter
    def cpf(self,nome):
        self._cpf = nome

    @idade.setter
    def idade(self,nome):
        self._idade = nome
    
    @sexo.setter
    def sexo(self,nome):
        self._sexo = nome
    
    @nascimento.setter
    def nascimento(self,nome):
        self._nascimento = nome


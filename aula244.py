# __str__, __repr__, {self.y!r}, __add__, __gt__, __new__, __init__, __enter__, __exit__, context_manager, __call__

# funções e decoradores com classe e com metodos 

# !
def meu_planeta(metodo):

    def executar(*args, **kwargs):
        resultado = metodo(*args, **kwargs)
        return resultado 
    return executar

def myrepr(self):
    class_name = self.__class__.__name__ 
    dict_args = self.__dict__ 
    return f'{class_name}({dict_args})'

def addrepr(cls):
    cls.__repr__ = myrepr
    return cls 

@addrepr
class Planeta:

    def __init__(self, nome):
        self.nome = nome 
    
    #def __repr__(self):
    #    class_name = self.__class__.__name__ 
    #    dict_args = self.__dict__ 
    #    return f'{class_name}({dict_args})'

    @meu_planeta
    def nome_planeta(self):
        print(f'O nome desse planeta é {self.nome}')
        return self.nome
    
#estou adicionando um decorador que retorna para addrepr a classe fruta
@addrepr
class Fruta:
    
    def __init__(self, nome):
        self.nome = nome 
    
    #def __repr__(self):
    #    class_name = self.__class__.__name__ 
    #    dict_args = self.__dict__ 
    #    return f'{class_name}({dict_args})'
    
terra = Planeta('Terra')
marte = Planeta('Marte')

uva = Fruta('Uva')
banana = Fruta('Banana')

print(terra.nome_planeta())
print(marte.nome_planeta())

print(uva)
print(banana)
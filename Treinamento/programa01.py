
from abc import ABC, abstractmethod 
from contextlib import contextmanager 

class TesteMaxin:
    def __init__(self):
        ...
    
    def print_teste(self):
        print('apenas testando um maxin')

# classe abstrata       
class Geometry(ABC):

    def __init__(self,base=0,largura=0,altura=0):
        self.base = base 
        self.largura = largura
        self.altura = altura
    
    @abstractmethod
    def calc_area(self):...


class Triangulo(Geometry, TesteMaxin):

    def __init__(self):
        ...
    
    def calc_area(self):
        return super().calc_area()

class Cubo(Geometry, TesteMaxin):

    def __init__(self):
        ...
    
    def calc_area(self):
        return super().calc_area()

class Foo:
    def __init__(self,mult):
        self.mult = mult
    
    def __call__(self, metodo):
        def multiplicar(*args, **kwargs):
            resultado = metodo(*args,**kwargs)
            return resultado * self.mult 
        return multiplicar

class Foo2:
    def __init__(self,value):
        self.value = value
    
    def __call__(self, metodo) -> float:
        
        def interator(*args, **kwargs):
            resultado = metodo(*args, **kwargs)
            return resultado * self.value
        return interator

@Foo(10)
def soma(a,b):
    return a+b

@Foo2(2)
def div(a,b):
    return a/b

soma_num = soma(2,2)
div_num = div(4,2)

print(div_num)
print(soma_num)

# contextmanager 

# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

from functools import partial

class Carro:
    def __init__(self,nome=None):
        self._nome_carro = nome
        self._motor_carro = None
        self._fabricante_carro = None

    @property
    def nome(self):
        return self._nome_carro
    
    @property
    def motor(self):
        return self._motor_carro 
    
    @property 
    def fabricante(self):
        return self._fabricante_carro 
    
    @nome.setter 
    def nome(self,nome):
        self._nome_carro = nome 

    @motor.setter
    def motor(self,motor):
        self._motor_carro = motor
    
    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante_carro = fabricante

class Motor:
    def __init__(self,nome):
        self.nome = nome

class Fabricante:
    def __init__(self,nome):
        self._nome = nome

    @property 
    def nome(self):
        return self._nome.upper()

    @nome.setter 
    def nome(self,nome):
        self._nome = nome

fusca = Carro('fusca')
motor = Motor('1.0')
fabricante = Fabricante('Volkswagen')
fusca.motor = motor
fusca.fabricante = fabricante
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)

def soma(a,b,/):
    return a*b*10

clousoure = partial(
    soma,10
)

val = clousoure(10)
print(val)
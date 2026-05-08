"""
    interator, generator, hasatter, getatter, yield
"""
import os 

# o interator é um objeto.
nome_completo = 'Lucas da Silva Patricio'

# toda string tem um interator, recebi o interator de nome_completo
interador_para_string = nome_completo.__iter__()

# dentro da classe interator, temos o next, que retorna o próximo valor do iterável.
#print(interador_para_string.__next__())

# o generator é uma função especial.

def generator(n=0):
    for i in range(n):
        yield i # PAUSADO

    return 'Fim' # ACABA AQUI, RETORNA COMO EXCEPTION

gen = generator(10)

#print(gen.__next__())
#print(gen.__next__())
#print(gen.__next__())


def my_range(inicio=0,fim=10):

    number = []

    def count_for(x=0,y=10):
        while True:
            if x < y:
                yield x 
                x += 1
            else:
                return 'acabou'
    
    try:
        generator = count_for(inicio,fim)
        while True:
            number.append(generator.__next__())
    except StopIteration as stoped:
        ...
    
    return number

#print(my_range(0,10))

os.system('cls')
a = 10
b = 0

try:
    nome='a'
    print(nome-1)
    print(v[8])
    c = a/b
    v = '123'
    
except (ZeroDivisionError, NameError) as e:
    print('MSG:',e.__class__.__name__)
except TypeError as e:
    print('TypeError: ',e.__class__.__name__)
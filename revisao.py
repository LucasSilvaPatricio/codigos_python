"""
list, dict, tuple, closoure, lambda, *args e *kwargs, set, shallow copy e deepcopy
"""

"""def executa(funcao, *args,**kwargs):
    return funcao(*args,**kwargs)

def soma(a,b,**kwargs):
    for item in kwargs:
        print(item)
    return a+b 

usuarios = dict(nome='Vitor',idade='23',cor='amarelado',cabelo='indio')

print(executa(lambda a,b: a+b,(4,4),usuarios))

#def sorted_list(fun, my_list):
#    return fun(my_list) 

marcas = ['Nokia','Samsung','Motorola','Xiaomi']

def exe_lambda(fun,*args):
    return fun(*args)

my_lambda = lambda marcas: print(sorted(marcas))
exe_lambda(my_lambda,marcas )
#def exe_lambda(fun)
#print(marcas)

idade = 18 

resultado = [idade if idade >= 18 else idade * 2]
print(resultado)
"""
import pprint 

usuarios = {
    "usuario1": {
        "nome": "João",
        "idade": 25,
        "cidade": "São Paulo",
        "profissao": "Engenheiro"
    },
    "usuario2": {
        "nome": "Maria",
        "idade": 30,
        "cidade": "Rio de Janeiro",
        "profissao": "Advogada"
    },
    "usuario3": {
        "nome": "Carlos",
        "idade": 35,
        "cidade": "Belo Horizonte",
        "profissao": "Professor"
    }
}

def p(v):
    pprint.pprint(v)

# primeiro codigo feito com python
lista_de_usuarios = [  
    {chave: 
        {
            'nome':item['nome'],
            'idade':item['idade'],
            'cidade':item['cidade'],
            'profissao':item['profissao'],
            'ano_nascimento': 2023 - int(item['idade'])
         } 
    }

    for chave, item in usuarios.items()
    ]
#p(lista_de_usuarios)

#valor = True 

#if isinstance(valor, (str,float)):
#    print('o valor é um inteiro.')
#else:
#    print('o valor não é um inteiro.')


s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}
s3 = s1 ^ s2
print(s3)

def executa(fun,y):
    return fun(y)

funcao = lambda y: y
#h = funcao(4)
print(executa(funcao, 4))

lambda a,b: a* b


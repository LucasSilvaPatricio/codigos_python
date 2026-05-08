"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""
"""
sumval = lambda a,b,c: a+b+c 
def exec_lambda(fun,*args):
    return fun(*args)

print(exec_lambda(sumval,10,5,2))
"""
"""
FAÇA UMA FUNÇÃO QUE SOME O PRIMEIRO NOME COM O SEGUNDO NOME USANDO LAMBDA
"""
"""
def sum_name(**kwargs):
    return kwargs['first_name'] +' '+kwargs['second_name']

print(sum_name(**{'first_name': 'maria'},second_name='moreira'))

sum_name_lambda = lambda **kwargs: kwargs['first_name'] + ' ' + kwargs['second_name']
name = sum_name_lambda(**{'first_name':'maria','second_name':'moreira'})
print(name)
"""

# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

"""
def verifica_numero(texto='Sua resposta é '):
    def np(valor):
        return texto + 'Positivo' if valor > 0 else 'Negativo'
    return np

vf1 = verifica_numero('Seu valor foi: ')
print(vf1(-1))
"""
import os 

"""
def executar(a,b):

    def som():
        return a+b
    
    def sub():
        return a-b
    
    def mul():
        return a*b
    
    def div():
        return a/b

    return {
        'soma': som,
        'subitracao': sub,
        'multiplicacao': mul,
        'divisao': div
    }

#calculadora = executar(10,5)
#print(calculadora['subitracao']())
"""

os.system('cls')

def calc(**kwargs):
    return {
        'soma': lambda :kwargs['numero1'] + kwargs['numero2'],
        'subitracao': lambda :kwargs['numero1'] - kwargs['numero2'],
        'multiplicacao': lambda :kwargs['numero1'] * kwargs['numero2'],
        'divisao': lambda :kwargs['numero1'] / kwargs['numero2']
    }

c = calc(numero1=15, numero2=50)
#print(c['divisao']())

"""
Sua tarefa é implementar uma função chamada filtrar_pessoas_por_cidade(pessoas, cidade)
que recebe a lista de pessoas e o nome de uma cidade como parâmetros. A função deve retornar
uma nova lista contendo apenas as pessoas que moram na cidade especificada.
"""

from pprint import pprint


def filtrar_por_cidade(cidade):
    lista_de_resultados = [
        item
        for item in pessoas
        if item['cidade'] == cidade
    ]
    for item in pessoas:
        if item['cidade'] == cidade:
            lista_de_resultados.append(item)
    return lista_de_resultados

pessoas = [
    {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Maria', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Pedro', 'idade': 20, 'cidade': 'Belo Horizonte'},
    {'nome': 'Ana', 'idade': 27, 'cidade': 'São Paulo'},
]

def filtrar_por_cidade(cidade):
    return [item for item in pessoas if item['cidade'] == cidade]

resultados = filtrar_por_cidade('Rio de Janeiro')
pprint(resultados)

import copy 
nova_pessoa = copy.deepcopy(pessoas)
pessoas[0].update({'cidade':'ceara'})
pprint(pessoas);pprint(nova_pessoa)
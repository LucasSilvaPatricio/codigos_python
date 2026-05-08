"""
Higher Order Functions - Funções de primeira classe 
"""

def message(msg, name):
    return f'{msg}, {name}!'

def saudacao(*args):
    return message(*args)

def executa(function,*args):
    return function(*args)

print(
    f'Execução de uma função Higher-Order-Functions:',
    executa(saudacao,'Boa noite','Lucas')
)

def funcao_first_class_functions():
    return 'Sou uma função de primeira classe, pois estou sendo atribuida a uma variavel!'

first_class_function = funcao_first_class_functions

print(first_class_function())

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

s1 = criar_saudacao('Bom dia', 'Lucas!')
print(s1)
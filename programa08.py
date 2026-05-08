# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:26:30 2023

@author: Lucas
"""

"""

and, not, in, not in,interaveis, interpolação de string com %
"""

senha_de_acesso = '12345'

entrar = input('Digite "entrar" para entrar: ') or 'sair'
print(entrar)
senha = input('Digite a senha de acesso: ')

if entrar == 'entrar' and senha == senha_de_acesso:
    print('Entrou no sitema')
else:
    print('Saiu do Sistema')
 

print(True and True and 1 and 0)    # 0
print(None and 1 and True and 0)    # None
print(None or '' or 'ABC' or True)  # ABC
print(0 or None or '' or bool(1))   # True
print(0 or None or '' or bool(0))   # False

condicao = True

if condicao:
    print('Condição é verdadeira.')

condicao = False

if not condicao: 
    print('Essa condição não é verdadeira.')    
 
string = 'Lucas da Silva Patricio' 
procurar = 'Sil'

if procurar in string:
    print(f'{procurar=} existe em {string}.')

procurar = 'sil'

if procurar not in string:
    print(f'{procurar=} não existe em {string}.')

nome_completo = 'Lucas da Silva Patricio'
idade = 22
imc = 60 / (1.69 ** 2)

print('Nome: %s' % nome_completo)
print('Idade: %i, IMC:%.2f' %(idade, imc))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

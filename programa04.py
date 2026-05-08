# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:57:09 2023

@author: Lucas
"""

# divisão inteira //
# divisão valor float / 

#divisao1 = 35 // 9
#divisao2 = 10 / 2

#print(divisao1, divisao2)

# f-strings

nome = 'Julia Vitoria'
idade = 16
imc = 23.03942
patrimonio_liquido = 2492948923

string_1 = f'Nome: {nome}'
string_2 = f'Idade: {idade}'
string_3 = f'Imc: {imc:.2f}'
string_4 = f'Patrimônio: {patrimonio_liquido:,.2f}'

print(string_1)
print(string_2)
print(string_3)
print(string_4)

nome = 'Lucas'
idade = 22
altura = 1.69

string = 'Nome: {}, Idade: {}, Altura: {}'
print(string.format(nome, idade, altura))

string = 'Nome: {2}, Idade: {1}, Altura: {0}'
print(string.format(altura, idade, nome))

string = 'Nome: {nome}, Idade: {idade}, Altura: {altura:.1f}'
print(string.format(
    nome=nome, idade=idade, altura=altura
))


























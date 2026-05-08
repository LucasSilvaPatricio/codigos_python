# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:13:31 2023

@author: Lucas
"""

"""
    DocString
    
    Calcular IMC 
    
    IMC = peso / (altura * altura)
    
"""

nome_do_usuario = 'Lucas da Silva Patricio'
idade = 22
peso = 60
altura = 1.69

imc = peso / altura**2 # peso / (altura*altura)

#print(imc)

string = 'Nome: {nome} \nIdade: {idade} \nPeso: {peso} \nAltura: {altura} \nIMC: {imc:.2f}'

print(string.format(
    nome=nome_do_usuario, idade=idade, peso=peso, altura=altura, imc=imc
))

string = f'Nome: {nome_do_usuario} \nIdade: {idade} \nPeso: {peso} \nAltura: {altura} \nIMC: {imc:.2f}'

print(string)























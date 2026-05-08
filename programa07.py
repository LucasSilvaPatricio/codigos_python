# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:44:54 2023

@author: Lucas
"""

"""

    Exercicio para saber qual o maior valor
    
"""

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:
    
    print(
        f'{primeiro_valor=} é maior ou igual'
        f' ao {segundo_valor=}'
    )
    
else:
    
    print(
        f'{segundo_valor=} é maior'
        f' do que {primeiro_valor=}'
    )
    

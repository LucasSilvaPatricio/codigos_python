# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:04:03 2023

@author: Lucas
"""

condicao = input('Você deseja "sair" ou "entrar"?: ')

if condicao == 'sair':
    print('Você saiu do programa.')
elif condicao == 'entrar':
    print('Você entrou no programa.')
else:
    print('Nenhuma opção valida foi selecionada!')
    
print('Fim do programa.')

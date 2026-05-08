"""
Fazer um programa que mostra qual letra apareceu mais vezes em uma frase.
zfill, for, list
"""

#string = 'Vitor'
#print(string.zfill(10)) # preenche com 0 até ter 10 caracteres

import os
import random

lista_de_palavras = ['elefante','cavalo','porco','vaca']
letras_acertadas = ''
palavra_secreta = lista_de_palavras[random.randint(0,len(lista_de_palavras)-1)]
palavra_atual = ''
contador = 0

print(f'{"."*5}Jogo do adivinha!{"."*5}')
print('Digite [sair] para sair ')
while True:

    contador += 1

    letra_digitada = input('Digite uma letra: ')

    if letra_digitada.lower() == 'sair':
         break
       
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada == letra_digitada:
            letras_acertadas += letra_digitada

    palavra_atual = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
             palavra_atual += letra
        else: 
             palavra_atual += '*'             

    if palavra_atual == palavra_secreta:
         print('Parabens!!, você ganhou o jogo.'.upper())
         print(
              f'A palavra secreta era: {palavra_secreta}\n'
              f'Você fez {contador} tentativas!'
              )
         letras_acertadas = ''
         palavra_atual = ''
         contador = 0
         palavra_secreta = lista_de_palavras[random.randint(0,len(lista_de_palavras)-1)]
         continue

    print(palavra_atual)

    
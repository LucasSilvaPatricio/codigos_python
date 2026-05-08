
"""
   Faça um programa que peça 10 números inteiros, calcule e mostre
   a quantidade de números pares e a quantidade de números impares.

"""

numeros_impares = []
numeros_pares = []
contador = 0

while contador < 5:
    numero = input(f'Digite o {contador + 1} numero: ')
    
    numero = int(numero)
    
    if(numero%2==0):
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        
    contador = contador + 1

print('\nOs numeros pares que você digitou: ',end='')

for par in numeros_pares:
    print(par, end='')

print('\nOs numeros impares que você digitou: ',end='')

for impar in numeros_impares:
    print(impar, end='')


print('\n')

numeros_pares = []
numeros_impares = []

for i in range(0,5):
    numero = int(input(f'Digite o {i} numero: '))

    numeros_pares.append(str(numero)) if numero%2 == 0 else ...
    numeros_impares.append(str(numero)) if numero%2 == 1 else ...

print(f'Numeros pares: ', *[par for par in numeros_pares])
print(f'Numeros impares: ', *[impar for impar in numeros_impares])
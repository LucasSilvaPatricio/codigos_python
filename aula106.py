
"""
Argumentos nomeados de função
"""

def calcular(v1, v2, operacao='+'):
    
    if operacao == '+':
        print(f'A soma foi: {v1+v2}')
    elif operacao == '-':
        print(f'A subitração foi: {v1-v2}')
    else:
        print('Você passou uma operação invalida!')

# calcule a subtração de 20 por 10, mas coloque os valores na ordem crescente no argumento
calcular(v2=10,v1=20,operacao='-') # A subitração foi: 10
calcular(10,20,operacao='-') # A subitração foi: -10

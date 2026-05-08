"""
isdigit, Try, Except, simplificar codigo com condições em variaveis, 
id() retorna o endereço da memoria pro elemento

"""
print('----- Programa que dobra o valor -----')

digito = input('Digite um digito inteiro: ')

#if digito.isdigit():
#    print('Você inseriu um digito.')
#else:
#    print('Você não inseriu um digito, talvez seu numero seja de ponto flutuante.')

try:
    numero = int(digito)
    print('Você inseriu um digito.')
except:
    print('Você não inseriu um digito, talvez seu numero seja de ponto flutuante.')

v1 = 'a'
v2 = 'c'
v3 = 'a'

print(f'{id(v1)=}, {id(v2)=}, {id(v3)=}') # id(v1)=140710950306880, id(v2)=140710950016264, id(v3)=140710950306880

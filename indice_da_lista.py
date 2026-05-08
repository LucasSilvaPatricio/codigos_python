"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

nomes = ['Maria','Jose','Pedro','Mateus']

lista_enumerada = enumerate(nomes)

#for indice, nome in lista_enumerada:
#    print(indice, nome)

#for indice, nome in lista_enumerada:
#    print(indice, nome)

string = '000000000000000000000000000000000000000000000000000000000000'
nova_string = ''.join(string.split(' '))
string_enumerada = enumerate(nova_string)
tamanho = int(len(string))
for indice,letra in string_enumerada:
    print(f'{letra * (indice+1): <{tamanho}}')

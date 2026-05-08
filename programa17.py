"""
Desempacotamento
"""

nomes = ['Maria','João','Pedro','Matheus']
nomes = tuple(nomes)
new_list = list(nomes) # fez um copy para new list

nomes = list(nomes)

nomes_2 = new_list 
nomes[0] = 'Outro'
print(nomes_2)
#nome1, nome2, nome3, nome4 = nomes
#print(nome1, nome2, nome3, nome4)

# imprimir apenas o primeiro valor
#nome, *_ = nomes
#print(nome)

# imprimir o terceiro valor
#_,_,nome,*_ = nomes
#print(nome)

#lista_1 = [1,2,3]
#lista_2 = [4,5,6]
#lista_3 = lista_1 + lista_2

#lista_4 = lista_3.copy()
#lista_3[0] = 'A'
#print(lista_4)

"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
#lista = ['Maria', 'Helena', 'Luiz']
#lista.append('João')

#for indice, nome in enumerate(lista):
#    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, o soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
=================== Resultado
lista_soma = [2, 4, 6, 8]
"""
from itertools import count, zip_longest
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = [a + b for a,b in zip(lista_a,lista_b)]

print(lista_soma)

nome_completo = 'lucas silva'
#print(nome_completo.count('l'))

# count é um interator pois tem __iter__ e __next__
c1 = count(10,2)
# o count é interator e interavel
#print(hasattr(c1, '__iter__'))
#print(hasattr(c1, '__next__'))
#for c in c1:
#    print(c)
#    if c >= 100:
#        break 


from itertools import combinations, permutations

cartela = [v for v in range(1,61)]
jogadas_possiveis = list(combinations(cartela,6))
jogadas_possiveis = len(jogadas_possiveis)
print(f'na mega sena é possivel {jogadas_possiveis} jogadas.')


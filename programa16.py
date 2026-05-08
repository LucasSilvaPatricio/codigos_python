"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#nomes = ['Lucas','Vitor','Maria']
#nomes.pop() # remove o último item e retorna
#nomes.append('Carlos')

#del nomes[-1]

#print(nomes)

#string = 'lucas'.zfill(20)
#print('................................................')
#tamanho = len(string)+10
#print(type(tamanho))
#print(f'{string: >10}')

#numero = 123456789
#print(str(numero)[::-1])

# em variaveis mutaveis, apontam para o mesmo valor
"""
nomes_1 = ['Lucas','João','Pedro','Maria']
nomes_2 = nomes_1


del nomes_1[-1]
nomes_1.append('Joana')
nomes_2.append('teste')
print(f'{nomes_1=}')
print(f'{nomes_2=}')

print(id(nomes_1))
print(id(nomes_2))

digitos_1 = 'ABCDE'
digitos_2 = digitos_1+'1'

print(id(digitos_1))
print(id(digitos_2))

# lista.copy() copia a lista
"""

# concatena lista
#lista_1 = [1,2,3]
#lista_2 = [4,5,6]
#lista_3 = lista_1 + lista_2

#lista_4 = lista_3.copy()
#lista_3[0] = 'A'
#print(lista_4)

# extend
#nomes_1 = ['Maria','Jose']
#lista_1 = [1,2,3]
#lista_1.extend(nomes_1)
#print(lista_1)


"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
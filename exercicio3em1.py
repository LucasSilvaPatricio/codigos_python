# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos  = [
    { 'nome' : 'Produto 5' , 'preco' : 10.00 },
    { 'nome' : 'Produto 1' , 'preco' : 22.32 },
    { 'nome' : 'Produto 3' , 'preco' : 10.11 },
    { 'nome' : 'Produto 2' , 'preco' : 105.87 },
    { 'nome' : 'Produto 4' , 'preco' : 69.90 },
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

#import copy 

#for produto in produtos:
#    produto.update({'preco':produto['preco'] * 1.1})


#novos_produtos = copy.deepcopy(produtos)
#print(novos_produtos.sort(reverse=True))


#print(novos_produtos)

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def retorna_func(*args,**kwargs):
        resultado = funcao(*args)
        return resultado
    return retorna_func

#soma_com_cinco = criar_funcao(soma, 5)
soma_de_cinco = criar_funcao(soma)
print(soma_de_cinco(5,5))

#multiplica_por_dez = criar_funcao(multiplica, 10)
multiplica_por_dez = criar_funcao(multiplica)
print(multiplica_por_dez(10,10))


# intertools zip_longest 
# zip 
# faça um programa que some duas lista
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



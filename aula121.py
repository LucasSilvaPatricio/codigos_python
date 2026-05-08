
#dicionarios {} ou dict

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

#pessoa = {
#    'nome': 'Lucas',
#    'sobrenome': 'Silva',
#    'idade': 22,
#    'altura': 1.69
#}

#print(len(pessoa))
#print(pessoa.keys())
#print(pessoa.values())
#print(pessoa.items())
#pessoa.setdefault('email','vazio') # adiciona um valor default caso o valor não exista.
#print(pessoa)
#print(pessoa.get('nome')) # obtem o valor da chave passada.
#print(pessoa.get('contato',0)) # se não tiver a chave ele retorna 0
#retorno = pessoa.pop('altura') # apaga a chave passada e retorna o valor que foi apagado.
#print(pessoa, retorno)
#print(pessoa.popitem()) #apaga o ultimo item da lista e retorna, e não especifica a chave

#pessoa.update({'imovel':'sim'}) # adiciona um item
#tupla = (('imovel','sim'),('casado','sim'))
#pessoa.update((('imovel','sim'),('casado','sim')))
#lista = [['imovel','sim'],['casado','sim']]
#pessoa.update(lista)
#pessoa.update([('imovel','sim'),('casado','sim')])
#print(pessoa)
"""
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Silva',
    'idade': 22,
    'altura': 1.69
}
#print(pessoa['nome'])
chave = 'idade'
nova_pessoa = pessoa.copy() # cria uma copia do dicionario
nova_pessoa[chave] = 15
print(nova_pessoa[chave])
print(pessoa[chave])

print(pessoa.__len__())

pessoa_iter = pessoa.__iter__()
print(next(pessoa_iter))
print(next(pessoa_iter))
print(next(pessoa_iter))
print(next(pessoa_iter))


from copy import deepcopy

frutas = {
    'maçã': 'vermelha',
    'abacate': 'verde',
    'abacaxi': ['laranja','verde']
}

nova_lista_de_frutas = frutas.copy() #shallow copy | copia a lista mas os mutaveis(list,dict) não são copiados como nova lista
                                     #deepcopy | para resolver tal problema faça um deepcopy
nova_lista_de_frutas = deepcopy(frutas)

frutas['maçã'] = 'verde'
frutas['abacaxi'][0] = 'verde' 

print(nova_lista_de_frutas)

"""




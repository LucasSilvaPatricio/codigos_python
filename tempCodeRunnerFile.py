

numeros_range           = range(0,10)
lista_de_numeros        = list(numeros_range)

nova_lista_de_numeros   = [x**2 for x in lista_de_numeros if x%2 == 1]
print(lista_de_numeros)
print(nova_lista_de_numeros)

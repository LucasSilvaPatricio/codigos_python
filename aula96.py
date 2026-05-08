
usuarios = ['João','Pedro','Maria',1,2,3]
nova_lista = usuarios.copy()

nome1, nome2, nome3, *_, penultimo, ultimo = nova_lista

print(nome1, nome2, nome3)
#print(*_)
print(f'{ultimo=} e {penultimo=}')
#for nome in usuarios:
#    print(nome, end=' ')

#print(*usuarios)

# operadores ternarios
#print('Esse valor' if False else 'outro valor' if False else 'Fim')
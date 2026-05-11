
letra = 'x'
frase = "uma frase criada por mim"
index = 0
encontrado = True

while index < len(frase):
    if letra == frase[index]:
        break
    index += 1
else:
    encontrado=False

if encontrado:
    print(f'Letra {letra=} foi encontrada!')
else:
    print(f'Letra {letra=} não encontrado!')
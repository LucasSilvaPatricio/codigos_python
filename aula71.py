# DESCOBRIR QUAL LETRA MAIS APARECEU NA FRASE   

frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'


letra       = '' # letra que mais apareceu na frase
quantidade  = 0 # quantidade de vezes
i           = 0

while i < len(frase):

    letra_atual = frase[i].lower()
    if frase.lower().count(letra_atual) > quantidade and not letra_atual==' ':
        letra = letra_atual
        quantidade = frase.lower().count(letra_atual)
    i+=1

print(f'{letra=}, {quantidade=}')
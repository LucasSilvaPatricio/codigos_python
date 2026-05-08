"""
while  continue  break                       capitalize  is, is not  not  in  not in  endswith()  startswith()  lower()  whilw else                              
while, continue, break, += -= *= **= /= //=, capitalize, is, is not, not, in, not in, endswith(), startswith(), lower(), while else
"""

#string = 'String + E legal.'
#nova_string = '*'

#contador = 0
#while contador < len(string):
#    nova_string += f' {string[contador]} *'
#    if string[contador] == '-':
#        break
#    contador = contador + 1
#else:
#    print('Essa String não tem "-"')
#    print(nova_string)

#print('Fora do while')


condicao = True

while condicao:
    string = input('Digite uma idade valida: ').lower() or 'sair'

    if 's' in string and string.startswith('s'):
        break

    if not string.isdigit():
        continue
    
    idade = int(string)

    if type(idade) is type(1):
        print('É um inteiro.')

    if idade >= 18:
        print('maior de idade!'.capitalize()) # capitalize() retorna a primeira letra maiúscula.
    else:
        print('menor de idade!'.capitalize) # capitalize() retorna a primeira letra maiúscula.

    idade = bool(idade)

    if type(idade) is not type(1):
        print('Idade não é inteiro')

    senha = [1,2,3,4,6,7,8,9,0]

    if 5 not in senha:
        print(f'O numero 5 não está em {senha=}')

print('Programa encerrado.')
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

condicao = True

while condicao:

    print(
        f'Validador de CPF',sep='\n'
        f'Digite [S]air para sair do programa.'
    )

    cpf_entregue = input('Digite um CPF, separado por "." e "-": ')

    if 's' in cpf_entregue.lower()[0]:
        condicao = False 
        continue 

    if '.' not in cpf_entregue and '-' not in cpf_entregue:
        print('Esse CPF não é valido!')
        continue

    if len(cpf_entregue) != 14:
        print('CPF com tamanho incorreto!')
        continue 

    if cpf_entregue[3] != '.' or cpf_entregue[7] != '.' or cpf_entregue[11] != '-':
        print('O CPF precisa tá formatado como [000.000.000-00]!!')
        continue

    cpf_validado = ''

    cpf_formatado = cpf_entregue.split('.')
    cpf_formatado = ''.join(cpf_formatado).split('-')
    cpf_formatado = ''.join(cpf_formatado)

    contagem_regressiva = range(-10,-1,1)
    soma_dos_valores = 0

    # dígitos validadores
    primeiro_digito = 0
    segundo_digito = 0
    
    for indice, multiplicador in enumerate(contagem_regressiva):
    
        digito = int(cpf_formatado[indice]) # cada dígito do cpf
        print(digito)
        soma_dos_valores += digito * (multiplicador*-1) # o multiplicador * -1 apenas para inverter o for

    # primeiro digito calculado
    modulo_da_soma = soma_dos_valores % 11
    primeiro_digito = (11 - modulo_da_soma) if modulo_da_soma >= 2 else 0

    # zerando a variável soma_dos_valores para depois
    soma_dos_valores = 0

    # adiciona o primeiro digito validador ao cpf
    cpf_validado = cpf_formatado[0:9] + str(primeiro_digito)
    print(cpf_formatado[0:9])
    contagem_regressiva = range(-11,-1,1)

    for indice, multiplicador in enumerate(contagem_regressiva):
        digito = int(cpf_validado[indice])
        soma_dos_valores += digito * (multiplicador*-1)

    modulo_da_soma = soma_dos_valores % 11
    segundo_digito = (11 - modulo_da_soma) if modulo_da_soma >= 2 else 0

    cpf_validado = cpf_validado + str(segundo_digito)

    # verifica se o cpf é valido
    valido = cpf_formatado == cpf_validado
    if valido:
        print('Seu cpf é valido!')
        print(cpf_validado)
    else:
        print('Seu cpf não é valido!')
        #print(cpf_validado) # vai tá criando um novo CPF valido para o CPF invalido inserido, mudando os 2 ultimos digitos
        #                    # para digitos validos

print('Fim do programa, até logo ;)')
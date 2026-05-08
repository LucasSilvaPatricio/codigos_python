"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#numero_str = input('Digite um numero inteiro: ') 

#if numero_str.isdigit():

#    numero_int =  int(numero_str)

#    if numero_int%2 == 0:
#        print(f'O {numero_int} é par.')
#    else:
#        print(f'O numero {numero_int} é impar.')

#else:
#    print('O numero digito não é inteiro!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#hour = input('Qual a hora?: ')[:2]

#is_good_morning = hour >= 0 and hour <= 11
#is_good_afternoon = hour >= 12 and hour <= 17
#is_good_evening = hour >= 18 and hour <= 23

#if hour.isdigit(): 

#    hour = int(hour)
    
#    if is_good_morning:
#        print('Bom dia!')

#    if is_good_afternoon:
#        print('Boa tarde!')

#    if is_good_evening:
#        print('Boa noite!')
#else:
#    print('the time is invalid!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#nome = input('Digite seu nome: ')

#if len(nome) <= 4:
#    print('Seu nome é curto!')

#if len(nome) >= 5 and len(nome) <= 6:
#    print('Seu nome é normal.')

#if len(nome) > 6:
#    print('Seu nome é muito grande!')
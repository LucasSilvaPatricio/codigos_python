"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = int(input("Digite um numero inteiro: "))
    
    if numero%2==0:
        print(f"{numero} é um numero par\n")
    else:
        print(f"{numero} é um numero ímpar\n")

except ValueError:
    print("Você não digitou um numero inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = int(input("qual a hora?:"))
bom_dia = horas >= 0 and horas <= 11
boa_tarde = horas >= 12 and horas <= 17
boa_noite = horas >= 18 and horas <= 23

if bom_dia:
    print("Bom dia 0-11")
elif boa_tarde:
    print("Boa tarde 12-17")
elif boa_noite:
    print("Boa noite 18-23")
else:
    print("hora inválida")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome: ")

nome_tamanho = len(nome)
nome_curto = nome_tamanho <= 4
nome_normal = nome_tamanho >= 5 and nome_tamanho <= 6

if nome_curto:
    print("Seu nome é curto!")
elif nome_normal:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
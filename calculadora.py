while True:

    numero_1 = input("Digite um valor: ")
    numero_2 = input("Digite outro valor: ")
    operador = input("Digite o operador (+-/*)")

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print("Números inválidos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print('Realizando conta. Resultado: ')
    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float}=',numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float}=',numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float}=',numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float}=',numero_1_float * numero_2_float)
    else:
        print("Nunca chega nesse else")

    sair = input("Sair? [Y]es: ").lower().startswith("s")

    if sair:
        break
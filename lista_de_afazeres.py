import os
from functools import partial

# lista de afazeres e lista desfeita
to_do_list = []  # lista de afazeres
undone_list = []  # lista desfeita

menu_info = """
Comandos: [listar] - para visualizar lista.
          [desfazer] - para desfazer ação.
          [refazer] - para refazer novamente a ação desfeita.
          [sair] - para sair.
"""

# mensagem de aviso


def warning():
    print('Você não tem mais valores para continuar fazendo essa operação!')


# função para checar se pode remover ou adicionar valor.
def checks(lista):
    if not len(lista) > 0:
        return False
    return True


# imprimi a lista de afazeres
def print_to_do_list(lista_produtos):
    print('\nOs produtos na sua lista são: ')
    for produto in lista_produtos:
        print(f'=>{produto}')


refazer = partial(
    lambda: to_do_list.append(undone_list.pop()) if checks(
        undone_list) == True else warning()
)

# desfaz ação feita
desfazer = partial(
    lambda: undone_list.append(to_do_list.pop()) if checks(
        to_do_list) == True else warning()
)

# imprimi a lista
listar = partial(
    print_to_do_list
)

# adiciona produto a lista
adicionar = partial(
    lambda produto: to_do_list.append(produto)
)

while True:

    print(menu_info.upper())
    cmd = input('Digite o comando: ')
    os.system('cls')
    if cmd == 'listar':
        listar(to_do_list)
    elif cmd == 'desfazer':
        desfazer()
    elif cmd == 'refazer':
        refazer()
    elif cmd == 'sair':
        break
    else:
        # adiciona item na lista ao digitar
        adicionar(cmd)

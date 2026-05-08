"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista_de_compra = []

acao_escolhida = ''

while acao_escolhida != 's':

    print(
      f'Digite [(I)nserir] para inserir um valor na lista',
      f'Digite [(A)pagar] para apagar um valor na lista',
      f'Digite [(L)istar] para ver valores na lista',
      f'Para sair digite [(S)air]',
      sep='\n'
     )
    
    acao_escolhida = input(">>> ").lower()[0] or 's'

    if acao_escolhida == 'i':
        produto = input('Qual produto deseja inserir na lista?: ')
        lista_de_compra.append(produto)
        continue

    if acao_escolhida == 'a':
        indice_do_produto = input('Qual indice quer apagar?: ')
        # validar o indice do produto
        indice_do_produto = int(indice_do_produto)

        tamanho_da_lista = len(lista_de_compra)-1
        if indice_do_produto >= 0 and indice_do_produto <= tamanho_da_lista:
            del lista_de_compra[indice_do_produto]
        else:
            print('Indice escolhido não existe na lista!')

    if acao_escolhida == 'l':
        for indice,produto in enumerate(lista_de_compra):
            print(f'{indice} => {produto}')

import brazilcep


def imprimir_informacoes(address):
    def get_address():
        for key in address:
            print(address[key])

    return get_address


try:
    address = brazilcep.get_address_from_cep('63507280')
    imprimir_informacoes(address)()
except brazilcep.exceptions.CEPNotFound:
    print('CEP não encontrado.')
except brazilcep.exceptions.BlockedByFlood:
    print('Você fez muitas requisições. Tente novamente mais tarde!')
else:
    print('Busca CEP concluido com sucesso.')

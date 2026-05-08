# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#contador = 0

#def operation():

#    global contador 
#    contador = 1

#    def multiplicar(num):
#        global contador
#        contador = contador + 1
#        return num * contador 
#    return multiplicar

#op = operation()
#print(op(2))
#print(op(2))
#print(op(2))


# função duplica 
# função triplica 
# função quadruplica 

def criar_multiplicador(multi):
    def multiplicador(valor):
        return valor * multi 
    return multiplicador

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadriplica(2))

def divisao(a=0,b=0):
    calculo = 0
    if a > 0 and b == 0:
        raise ZeroDivisionError('essa divisão não existe.')
    else:
        calculo = a/b 
    return calculo

#print(divisao(10,0))
nome = 'maria'
metodo = 'upper'
if hasattr(nome,metodo):
    print(f'tem o metodo {metodo}')
    val = getattr(nome,metodo)()
    print(val)
else:
    print(f'não tem {metodo}')


try:
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print('MSG: ',e)


def generator(n=10):
    count = 0
    for i in range(0,n):
        if count < n:
            yield count 
            count+=1
        else:
            return 'acabou'

g = generator(10)

print(g.__next__())
print(g.__next__())
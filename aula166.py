
# estudar funções decoradoras, interator, generator e lambda
def decorate(fun):

    def return_function(*args,**kwargs):
        result = 0

        for v in args:
            result = v

        result = fun(result)
        return result
    
    return return_function

@decorate
def squared(result):
    return result * result

#squared_value = decorate(squared)
#print(f'Value squared is: {squared_value(10)}')
#print(squared(10))

string = 'teste de uma string'
iter_string = string.__iter__()
#print(next(iter_string))
#print(next(iter_string))
#print(next(iter_string))
#print(next(iter_string))
#print(next(iter_string))

def generator():
    while True:
        yield 1 


def func1(func2):
    def func3():
        return func2(2) 
    return func3

@func1 
def func4(x):
    return 1+1+x

#print(func4())

lista1 = [1,2,3]
lista2 = [4,5,6,7]

from itertools import zip_longest

print(list(zip(lista1,lista2)))

print(list(zip_longest(lista1,lista2)))
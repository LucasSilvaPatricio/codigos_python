
"""
    Closoure
"""

contador = -1
def retorna_valores(*args):
    number = list(args)
  
    def next_number():
        global contador
        contador = contador + 1
        return number[contador]
        

    return next_number

next_number = retorna_valores(1,2,3,4,5)

try:
    while True:
        print(next_number())
except Exception as error:
    ...

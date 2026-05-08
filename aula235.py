# exeception 


class MeuError(Exception):
    ... 

class OutroError(Exception):
    ...

def levantar():
    #division = 1/0 
    first_error = MeuError('Error personalizado')
    first_error.add_note('Um nota do primeiro error')
    raise first_error
    print('ok')
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    outro_exeception = OutroError("Segundo error!!!")
    outro_exeception.add_note('Um segundo error está sendo levantado [!]')
    outro_exeception.__notes__ += error.__notes__.copy()
    raise outro_exeception
else:
    print('Executando se não tiver nada capturado no exception')
finally:
    print('Executando sempre')


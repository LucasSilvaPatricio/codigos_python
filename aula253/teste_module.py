import enum 

class Semana(enum.Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7

if isinstance(Semana.DOMINGO, Semana):
    print('É instancia de enum')
else:
    print('Não é instancia de enum')

print(Semana.SEXTA.name)
print(Semana.SEXTA.value)

mes = enum.Enum('Mes',['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO'])
#print(type(mes))
if isinstance(mes.JANEIRO, mes):
    print('É instancia de enum')
else:
    print('Não é instancia de enum')

print(mes.ABRIL.name)
print(mes.ABRIL.value)

"""Comentario sobre o meu modulo

Lorem ipsum egestas vitae pharetra tristique litora habitant, quam et interdum cubilia auctor at leo, sem hac curae sodales rhoncus posuere. aenean bibendum netus metus molestie cubilia tempus quisque dapibus risus curae, nulla ipsum adipiscing suscipit molestie dictum donec potenti laoreet donec, morbi elit feugiat nam convallis massa vivamus mauris feugiat. id ullamcorper aliquet platea pulvinar hendrerit malesuada iaculis est sit, quam justo magna eu purus maecenas vivamus sed non pharetra, est maecenas rutrum sem phasellus litora pellentesque arcu. class fringilla nisi velit pharetra pretium quam, neque tellus est platea scelerisque himenaeos facilisis, ultrices quam ad eu consequat dictumst, himenaeos suspendisse ut nostra leo. 

	Et pretium gravida ut felis sapien per cursus volutpat posuere curae, fames porta class inceptos metus nisi et sollicitudin viverra auctor, bibendum integer condimentum facilisis consequat tellus quam ornare mattis. sapien suscipit cursus nullam scelerisque vivamus mollis est tellus condimentum, mollis curae enim quisque interdum rutrum ornare laoreet accumsan, molestie eleifend risus ut fringilla quisque iaculis id. ullamcorper curabitur sed curabitur torquent pulvinar cras odio aenean, ante elementum erat rhoncus fringilla commodo suscipit quisque metus, eros pretium integer sed commodo condimentum egestas. praesent fermentum euismod convallis sociosqu convallis ullamcorper placerat adipiscing mauris, dictumst litora donec libero habitant tristique vel eleifend, non porta dictum senectus nunc varius molestie nec. 
"""

def soma(x: int | float, y: int | float) -> int | float:
    """
    soma x + y 

    Esse metodo recebe dois valores e depois soma os valores, para cada
    valor existe x e y, permitindo ser passado dois valores como argumentos
    cada valor pode ser do tipo int ou float

    :param x: numero 1
    :type x: int or float
    :param y: numero 2
    :type y: int or float
    :return: Soma de x+y
    :rtype: int or float
    """
    return x + y


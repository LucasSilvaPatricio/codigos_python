# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:55:09 2023

@author: Lucas
"""

"""
    f-strings
"""

contador = 0

while (contador < 10):
    print(f'{contador * ".": ^10}')
    contador += 1

print(f'{"ABC": ^9}')
print(f'{"ABC": ^9}')
print(f'{"ABC": ^9}')

print(f'{"ABC": >10}')
print(f'{"ABC": <10}')

print(f'{1024:08X}')
